from grpctunnel.options import TunnelOption, tunnelOpts
from tunnelpb import tunnel_pb2_grpc
from tunnelpb import tunnel_pb2 as tunnelpb


class tunnelStreamClient:
    def Context(self):
        pass

    def Send(self, obj: tunnelpb.ClientToServer) -> int:
        pass

    def Recv(self, obj: tunnelpb.ServerToClient) -> int:
        pass


class tunnelChannel:
    def __init__(self) -> None:
        self.stream: tunnelStreamClient


# 	stream              tunnelStreamClient
# 	tunnelMetadata      metadata.MD
# 	serverSendsSettings bool
# 	tunnelOpts          *tunnelOpts
# 	ctx                 context.Context
# 	cancel              context.CancelFunc
# 	tearDown            func(*tunnelChannel)

# 	awaitSettings chan struct{}
# 	settings      *tunnelpb.Settings
# 	useRevision   tunnelpb.ProtocolRevision

# 	mu            sync.RWMutex
# 	streams       map[int64]*tunnelClientStream
# 	lastStreamID  int64
# 	streamCreated bool
# 	err           error
# 	finished      bool

# 	streamCreation sync.Mutex
# }


class TunnelChannel:
    def __init__(self) -> None:
        pass


class pendingChannel:
    def __init__(self, stub: tunnelpb.TunnelServiceClient) -> None:
        self.__stub: tunnelpb.TunnelServiceClient = stub
        self.opts: tunnelOpts


#  PendingChannel is an un-started channel. Calling Start will establish the
#  tunnel and returns a value that implements [grpc.ClientConnInterface], so it
#  can be used to create stubs and issue other RPCs that are all carried over a
#  single tunnel stream.


#  The given context defines the lifetime of the stream and therefore of the
#  channel; if the context times out or is cancelled, the channel will be closed.
class PendingChannel:
    def __init__(
        self, sub: tunnel_pb2_grpc.TunnelServiceStub, opts: list[TunnelOption]
    ) -> None:
        for opt in opts:
            opt.apply()


def NewChannel(stub: tunnel_pb2_grpc.TunnelServiceStub) -> PendingChannel:
    return (PendingChannel(stub), 0)
