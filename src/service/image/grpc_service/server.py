import pickle
import time

import grpc
from concurrent import futures
import grpc_service.structure_pb2 as pb2
import grpc_service.structure_pb2_grpc as pb2_grpc

from config import URL, count_workers


class GExchange(pb2_grpc.CheckServiceServicer):
    def SendCheck(self, request, context):
        data = pickle.loads(request.check)
        print(data)
        return pb2.Response(answer="good")


def serve():
    print("running the gRPC server")
    options = [('grpc.max_receive_message_length', 5 * 1024 * 1024)]

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=count_workers), options=options)
    pb2_grpc.add_CheckServiceServicer_to_server(GExchange(), server)
    server.add_insecure_port(URL)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
