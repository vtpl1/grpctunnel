# grpctunnel
Python implementation inspired from https://github.com/jhump/grpctunnel

https://github.com/grpc/grpc/tree/master/examples/python/hellostreamingworld

python -m grpc_tools.protoc -I./protos/grpctunnel/v1 -I./third_party/googleapis --python_out=./tunnelpb --pyi_out=./tunnelpb --grpc_python_out=./tunnelpb ./protos/grpctunnel/v1/tunnel.proto

