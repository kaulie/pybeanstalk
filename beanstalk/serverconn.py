import socket, select
import protohandler

class ServerConn(object):
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.proto = protohandler.Proto()
        self.proto.job = dict
        self.__makeConn()

    def __makeConn(self):
        self._socket = socket.socket()
        self._socket.connect((self.server, self.port))

    def __writeline(self, line):
        return self._socket.send(line)

    def _get_command(self):
        data = ''
        while True:
            x = select.select([self._socket],[],[])[0][0]
            data += x.recv(1)
            if data.endswith('\r\n'):
                break
        return data

    def _get_response(self, handler):
        ''' keep in mind handler returns a tuple:
            (finished, satus, expected_data or result)
        '''
        command = self._get_command()
        status, result = handler(command)

        while status == 'i':
            remaining = result
            x = select.select([self._socket],[],[])[0]
            x = x[0]
            if not x is self._socket:
                raise Exception('erich done fucked up')
            get_amount = ((remaining < 20) and remaining) or 20
            data = self._socket.recv(get_amount)
            try:
                status, result = handler(data)
            except Exception, e:
                print 'got exception! error is: %s' % (e,)
                raise

        self.handle_status(status)
        return result

    def _do_interaction(self, line, handler):
        print 'line is: %s handler is %s' % (line.strip(), handler)
        self.__writeline(line)
        return self._get_response(handler)

    def handle_status(self, status):
        if status == 'b':
            print 'job burried'

    def put(self, data, pri=0, delay=0):
        return self._do_interaction(*self.proto.process_put(data, pri, delay))

    def reserve(self):
        return self._do_interaction(*self.proto.process_reserve())

if __name__ == '__main__':
    x = ServerConn('192.168.2.1', 11300)
    x.put('python test\nthings!')
    print x.reserve()
