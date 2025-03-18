# Instrument Service (instrument_service.py)
import grpc
from concurrent import futures
import instrument_service_pb2
import instrument_service_pb2_grpc

SOCKET_PATH = "/tmp/instrument_service.sock"

class InstrumentService(instrument_service_pb2_grpc.InstrumentServiceServicer):
    def InitializeInstruments(self, request, context):
        return instrument_service_pb2_grpc.InitResponse(success=True, message="Instruments Initialized")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    instrument_service_pb2_grpc.add_InstrumentServiceServicer_to_server(InstrumentService(), server)
    server.add_insecure_port(f"unix://{SOCKET_PATH}")
    server.start()
    print("Instrument Service running...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()