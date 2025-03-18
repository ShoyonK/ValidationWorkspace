import grpc
from concurrent import futures
import harness_service_pb2
import harness_service_pb2_grpc
from dut import dut_service_pb2
from dut import dut_service_pb2_grpc

SOCKET_PATH = "/tmp/harness_service.sock"


class HarnessService(harness_service_pb2_grpc.HarnessServiceServicer):

    def RunTest(self, request, context):
        channel = grpc.insecure_channel("unix:///tmp/dut_service.sock")
        stub = dut_service_pb2_grpc.DUTServiceStub(channel)

        # Send a connection request to the DUT service
        connection = stub.ConnectToDUT(dut_service_pb2.ConnectRequest())
        if connection.success == True:
            print("SUCCESS")

        return harness_service_pb2.TestResponse(
            test_name="Test", status="DUT Connected successfully through harness service and have run test", execution_time=2.0
        )

    def ConnectToDUT(self, request, context):
        """Handles DUT connection request and forwards it to the DUT Service."""
        pass



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    harness_service_pb2_grpc.add_HarnessServiceServicer_to_server(HarnessService(), server)
    server.add_insecure_port(f"unix://{SOCKET_PATH}")
    server.start()
    print("Harness Service running...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
