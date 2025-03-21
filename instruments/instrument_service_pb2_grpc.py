# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import instrument_service_pb2 as instrument__service__pb2


class InstrumentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitializeInstruments = channel.unary_unary(
                '/instrument.InstrumentService/InitializeInstruments',
                request_serializer=instrument__service__pb2.InitRequest.SerializeToString,
                response_deserializer=instrument__service__pb2.InitResponse.FromString,
                )


class InstrumentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InitializeInstruments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InstrumentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitializeInstruments': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeInstruments,
                    request_deserializer=instrument__service__pb2.InitRequest.FromString,
                    response_serializer=instrument__service__pb2.InitResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'instrument.InstrumentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InstrumentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InitializeInstruments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/instrument.InstrumentService/InitializeInstruments',
            instrument__service__pb2.InitRequest.SerializeToString,
            instrument__service__pb2.InitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
