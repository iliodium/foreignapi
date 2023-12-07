import grpc
from concurrent import futures
import structure_pb2 as pb2
import structure_pb2_grpc as pb2_grpc

import io
from PIL import Image

data = {
    "Vasya1": 1,
    "Vasya2": 2,
    "Vasya3": 3,
}


class GExchange(pb2_grpc.MyServiceServicer):
    def get_my_data(self, request, context):
        imageBinaryBytes = request.image
        imageStream = io.BytesIO(imageBinaryBytes)
        imageFile = Image.open(imageStream)
        # imageFile.show()

        return pb2.MyRes(answer=0)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MyServiceServicer_to_server(GExchange(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("running the gRPC server")
    serve()
