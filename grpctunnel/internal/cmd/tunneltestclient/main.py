import grpc

# from grpctunnel.tunnelpb import tunnel_pb2_grpc
from ....tunnelpb import tunnel_pb2_grpc
# from ....tunnel_client import NewChannel

def main():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        tunnelClient = tunnel_pb2_grpc.TunnelServiceStub(channel)
        # tunnel, err = NewChannel(tunnelClient)
    print("client")

