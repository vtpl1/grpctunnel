import grpc

from ....tunnelpb.tunnel_pb2_grpc import TunnelServiceStub
from ....tunnel_client import NewChannel

def main():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        tunnelClient = TunnelServiceStub(channel)
        tunnel, err = NewChannel(tunnelClient)
    print("client")
