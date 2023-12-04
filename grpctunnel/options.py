from tunnelpb import tunnel_pb2 as tunnelpb


#  WithDisableFlowControl returns an option that disables the
#  use of flow control, even when the tunnel peer supports it.

#  NOTE: This should NOT be used in application code. This is
#  intended for test code, to verify that the tunnels work
#  without flow control, to make sure they can interop correctly
#  with older versions of this package, before flow control was
#  introduced.


#  Eventually, older versions that do not use flow control will
#  not be supported and this option will be removed.
def WithDisableFlowControl():
    return tunnelOptFunc(lambda opts: setattr(opts, "disableFlowControl", True))


class tunnelOpts:
    def __init__(self):
        self.disableFlowControl = False

    def supportedRevisions(self):
        if self.disableFlowControl:
            return [tunnelpb.ProtocolRevision.REVISION_ZERO]
        return [
            tunnelpb.ProtocolRevision.REVISION_ZERO,
            tunnelpb.ProtocolRevision.REVISION_ONE,
        ]


class tunnelOptFunc:
    def __init__(self, func):
        self.func = func

    def apply(self, opts: tunnelOpts):
        self.func(opts)


# TunnelOption is an option for configuring the behavior of
# a tunnel client or tunnel server.
class TunnelOption:
    def apply(self, tunnel_opts: tunnelOpts):
        pass
