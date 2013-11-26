# coding=utf-8
from contextlib import contextmanager
import Queue
from threading import Lock
import zmq
import response_pb2
import logging

class Instance(object):
    def __init__(self, context):
        self.geom = None
        self._sockets = Queue.Queue()
        self.socket_path = None
        self.script = None
        self.nb_created_socket = 0
        self.lock = Lock()
        self.context = context


    @contextmanager
    def socket(self, context):
        socket = None
        try:
            socket = self._sockets.get(block=False)
        except Queue.Empty:
            socket = context.socket(zmq.REQ)
            socket.connect(self.socket_path)
            self.lock.acquire()
            self.nb_created_socket += 1
            self.lock.release()
        try:
            yield socket
        finally:
            if not socket.closed:
                self._sockets.put(socket)


    def send_and_receive(self, request, timeout=10000):
        with self.socket(self.context) as socket:
            socket.send(request.SerializeToString())
            if socket.poll(timeout=timeout) > 0:
                pb = socket.recv()
                resp = response_pb2.Response()
                resp.ParseFromString(pb)
                return resp
            else :
                socket.setsockopt(zmq.LINGER, 0)
                socket.close()
                logging.error(u"La requête : " + unicode(request)
                        + u" a echoue " + self.socket_path)
                raise DeadSocketException(region, self.socket_path)

