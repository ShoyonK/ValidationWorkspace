import sys
import grpc
from harness import harness_service_pb2
from harness import harness_service_pb2_grpc
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

SOCKET_PATH = "/tmp/harness_service.sock"

class TestGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("RF/MCU Test Runner")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Enter Test Name:")
        layout.addWidget(self.label)

        self.test_input = QLineEdit(self)
        layout.addWidget(self.test_input)

        self.connect_button = QPushButton("Run Test", self)
        self.connect_button.clicked.connect(self.run_test)
        layout.addWidget(self.connect_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def run_test(self):
        channel = grpc.insecure_channel(f"unix://{SOCKET_PATH}")
        stub = harness_service_pb2_grpc.HarnessServiceStub(channel)
        request = harness_service_pb2.TestRequest(test_name="Test")
        response = stub.RunTest(request)
        self.result_label.setText(response.status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = TestGUI()
    gui.show()
    sys.exit(app.exec_())