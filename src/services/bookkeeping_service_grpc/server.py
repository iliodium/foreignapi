import os
import pickle
import sys
from concurrent import futures

import grpc

sys.path.insert(1, os.path.join(sys.path[0], '..\\..\\..'))

from src.services.config import CountWorkersService, BookkeepingServiceResponce, StatusServer, URL
import src.services.bookkeeping_service_grpc.structure_pb2 as pb2
import src.services.bookkeeping_service_grpc.structure_pb2_grpc as pb2_grpc
from src.services.utils import calculate_tax


class BookkeepingServiceServer(pb2_grpc.BookkeepingServiceServicer):
    def SendCheck(self, request, context):
        data: dict = pickle.loads(request.check)
        tax = calculate_tax(data.values())

        return pb2.Response(
            answer=BookkeepingServiceResponce.pay_tax,
            tax=tax
        )


def run_server(url: str = "localhost:50123"):
    print(StatusServer.start.format(BookkeepingServiceServer.__name__))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=CountWorkersService.BookkeepingService))
    pb2_grpc.add_BookkeepingServiceServicer_to_server(BookkeepingServiceServer(), server)
    server.add_insecure_port(url)
    server.start()
    print(StatusServer.success.format(BookkeepingServiceServer.__name__))
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        run_server(URL)
    except Exception as e:
        print(StatusServer.error.format(BookkeepingServiceServer.__name__))
        print(e)
