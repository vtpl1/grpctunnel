# https://github.com/grpc/grpc/blob/v1.58.0/examples/python/route_guide/run_codegen.py

from grpc_tools import protoc

proto_files = ["protos/grpctunnel/v1/tunnel.proto"]
for proto_file in proto_files:
    protoc.main(
        (
            "",
            "--proto_path=./third_party/googleapis/",
            "--proto_path=./protos/grpctunnel/v1",
            "--python_out=./grpctunnel/tunnelpb",
            "--pyi_out=./grpctunnel/tunnelpb",
            "--grpc_python_out=./grpctunnel/tunnelpb",
            proto_file,
        )
    )
    # protoc.main(
    #     (
    #         "",
    #         "--proto_path=.",
    #         "--proto_path=./protos/grpctunnel/v1",
    #         "--proto_path=./third_party/googleapis",
    #         "--python_out=./grpctunnel/tunnelpb",
    #         "--pyi_out=./grpctunnel/tunnelpb",
    #         "--grpc_python_out=./grpctunnel/tunnelpb",
    #         proto_file,
    #     )
    # )
