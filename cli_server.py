import asyncio
from typing import AsyncIterable
from loguru import logger
import grpc
from grpctunnel.tunnelpb import tunnel_pb2_grpc, tunnel_pb2

# Coroutines to be invoked when the event loop is shutting down.
_cleanup_coroutines = []


class TunnelServiceServicer(tunnel_pb2_grpc.TunnelServiceServicer):
    async def OpenTunnel(
        self, request_iterator: AsyncIterable[tunnel_pb2.ClientToServer], unused_context
    ):
        logger.info("OpenTunnel")
        # return_iterator: AsyncIterable[tunnel_pb2.ServerToClient] = []
        return_val: tunnel_pb2.ServerToClient
        async for client_to_server in request_iterator:
            return_val = tunnel_pb2.ServerToClient(stream_id=client_to_server.stream_id)
            yield return_val

    async def OpenReverseTunnel(
        self, request_iterator: AsyncIterable[tunnel_pb2.ServerToClient], unused_context
    ):
        return_val: tunnel_pb2.ClientToServer
        async for client_to_server in request_iterator:
            return_val = tunnel_pb2.ClientToServer(client_to_server.stream_id)
            yield return_val

    async def PingPong(
        self, request: tunnel_pb2.Ping, unused_context
    ) -> tunnel_pb2.Pong:
        ret = tunnel_pb2.Pong(id=request.id + 15)
        return ret


async def serve() -> None:
    server = grpc.aio.server()
    tunnel_pb2_grpc.add_TunnelServiceServicer_to_server(TunnelServiceServicer(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logger.info(f"Starting server at {listen_addr}")
    await server.start()

    async def server_graceful_shutdown():
        logger.info("Starting graceful shutdown...")
        # Shuts down the server with 5 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(5)

    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()


if __name__ == "__main__":
    logger.info("Start")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(serve())
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt")
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()
    logger.info("End")
