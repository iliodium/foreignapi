# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src.services.bookkeeping_service_grpc import structure_pb2 as src_dot_services_dot_bookkeeping__service__grpc_dot_structure__pb2


class BookkeepingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendCheck = channel.unary_unary(
                '/BookkeepingService/SendCheck',
                request_serializer=src_dot_services_dot_bookkeeping__service__grpc_dot_structure__pb2.Check.SerializeToString,
                response_deserializer=src_dot_services_dot_bookkeeping__service__grpc_dot_structure__pb2.Response.FromString,
                )


class BookkeepingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookkeepingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.SendCheck,
                    request_deserializer=src_dot_services_dot_bookkeeping__service__grpc_dot_structure__pb2.Check.FromString,
                    response_serializer=src_dot_services_dot_bookkeeping__service__grpc_dot_structure__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BookkeepingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookkeepingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookkeepingService/SendCheck',
            src_dot_services_dot_bookkeeping__service__grpc_dot_structure__pb2.Check.SerializeToString,
            src_dot_services_dot_bookkeeping__service__grpc_dot_structure__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
