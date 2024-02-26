import pickle

import grpc

import src.services.bookkeeping_service_grpc.structure_pb2 as pb2
import src.services.bookkeeping_service_grpc.structure_pb2_grpc as pb2_grpc
from src.config import BOOKKEEPING_GRPC_NAME, BOOKKEEPING_GRPC_PORT


class BookkeepingServiceClient:
    def __init__(self):
        self.__channel = grpc.insecure_channel(f"{BOOKKEEPING_GRPC_NAME}:{BOOKKEEPING_GRPC_PORT}")
        self.__stub = pb2_grpc.BookkeepingServiceStub(self.__channel)

    def send_check(self, data: dict):
        data = pickle.dumps(data)
        request = pb2.Check(check=data)
        response = self.__stub.SendCheck(request)
        return response
