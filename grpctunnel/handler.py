from .options import tunnelOpts
from .tunnel_client import TunnelChannel
from threading import Thread, Lock

grpctunnelNegotiateKey = "grpctunnel-negotiate"
grpctunnelNegotiateVal = "on"


class reverseChannelEntry:
    def __init__(self) -> None:
        self.ch: TunnelChannel
        self.key: str = ""


class reverseChannels:
    def __init__(self) -> None:
        self.__mu: Lock = Lock()
        self.__avail: dict = {}
        self.__chans: list(reverseChannelEntry) = []
        self.__idx: int = 0


#  TunnelServiceHandler provides an implementation for TunnelServiceServer. You
#  can register handlers with it, and it will then expose those handlers for
#  incoming tunnels. If no handlers are registered, the server will reply to
#  OpenTunnel requests with an "Unimplemented" error code. The server may still
#  be used for reverse tunnels
#
#  For reverse tunnels, if supported, all connected channels (e.g. all clients
#  that have created reverse tunnels) are available. You can also configure a
#  listener to receive notices when channels are connected and disconnected.
#
class TunnelServiceHandler:
    def __init__(self) -> None:
        self.__handlers: dict = {}
        self.__noReverseTunnels: bool = False
        self.__onReverseTunnelConnect: TunnelChannel | None = None
        self.__onReverseTunnelDisconnect: TunnelChannel | None = None
        self.__affinityKey: TunnelChannel | None = None
        self.__tunnelOpts: tunnelOpts | None = None

        self.__stopping: bool = False
