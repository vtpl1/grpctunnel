# grpctunnel
Python implementation inspired from https://github.com/jhump/grpctunnel

https://github.com/grpc/grpc/tree/master/examples/python/hellostreamingworld

git submodule update --init

python -m grpc_tools.protoc -I./protos/grpctunnel/v1 -I./third_party/googleapis --python_out=./grpctunnel/tunnelpb --pyi_out=./grpctunnel/tunnelpb --grpc_python_out=./grpctunnel/tunnelpb ./protos/grpctunnel/v1/tunnel.proto

