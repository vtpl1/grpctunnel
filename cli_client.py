import asyncio
from typing import AsyncIterable, Iterable, List
from loguru import logger
import grpc
from grpctunnel.tunnelpb import tunnel_pb2_grpc, tunnel_pb2

# from grpctunnel.internal.cmd.tunneltestclient.main import main


async def generate_client_to_server_messages() -> AsyncIterable[
    tunnel_pb2.ClientToServer
]:
    messages: List[tunnel_pb2.ClientToServer] = [tunnel_pb2.ClientToServer(stream_id=1)]
    for msg in messages:
        logger.info(
            f"generate_client_to_server_messages {msg.stream_id}{msg.new_stream}"
        )
        yield msg


async def generate_server_to_client() -> AsyncIterable[tunnel_pb2.ServerToClient]:
    pass

async def call_open_tunnel(stub: tunnel_pb2_grpc.TunnelServiceStub):
    logger.info("Calling open client")
    async for response in stub.OpenTunnel(generate_client_to_server_messages()):
        logger.info(f"Received message {response.stream_id} ")
    logger.info("Called open client")


async def call_open_reverse_tunnel(stub: tunnel_pb2_grpc.TunnelServiceStub):
    async for response in stub.OpenReverseTunnel(generate_client_to_server_messages()):
        pass
    pass


async def call_ping_pong(stub: tunnel_pb2_grpc.TunnelServiceStub):
    ping = tunnel_pb2.Ping()
    ping.id = 11
    ret = await stub.PingPong(ping)
    logger.info(f"Here {ret.id}")


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = tunnel_pb2_grpc.TunnelServiceStub(channel)
        await call_open_tunnel(stub)
        await call_ping_pong(stub)


if __name__ == "__main__":
    logger.info("Start")
    asyncio.run(run())
    logger.info("End")
