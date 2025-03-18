import grpc
from concurrent import futures
import dut_service_pb2
import dut_service_pb2_grpc
import os
import time

SOCKET_PATH = "/tmp/dut_service.sock"

DUT_CONNECTED = False
DUT_DATA = {
    "temperature": "45°C",
    "voltage": "3.3V",
    "firmware_version": "1.2.3"
}

if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)


class DUTService(dut_service_pb2_grpc.DUTServiceServicer):
    def ConnectToDUT(self, request, context):
        """ Simulate connecting to the DUT """
        global DUT_CONNECTED
        DUT_CONNECTED = True
        return dut_service_pb2.ConnectResponse(success=True, message="DUT Connected Successfully")

    def ReadDUTInfo(self, request, context):
        """ Read a parameter from the DUT """
        if not DUT_CONNECTED:
            return dut_service_pb2.ReadResponse(parameter=request.parameter, value="Error: DUT not connected")

        value = DUT_DATA.get(request.parameter, "Unknown Parameter")
        return dut_service_pb2.ReadResponse(parameter=request.parameter, value=value)

    def CallFirmwareFunction(self, request, context):
        """ Simulate making an RPC call into the DUT firmware """
        if not DUT_CONNECTED:
            return dut_service_pb2.FirmwareResponse(success=False, message="DUT not connected")

        response_msg = f"Firmware function '{request.function_name}' executed with args: {request.arguments}"
        return dut_service_pb2.FirmwareResponse(success=True, message=response_msg)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    dut_service_pb2_grpc.add_DUTServiceServicer_to_server(DUTService(), server)
    server.add_insecure_port(f"unix://{SOCKET_PATH}")
    server.start()
    print("DUT Service running...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
