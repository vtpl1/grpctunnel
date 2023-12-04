import grpc
from tunnelpb import tunnel_pb2_grpc
# from tunnelpb.tunnel_pb2 import ClientToServer
channel = grpc.insecure_channel('localhost:50051')
tunnelStub = tunnel_pb2_grpc.TunnelServiceStub(channel=channel)