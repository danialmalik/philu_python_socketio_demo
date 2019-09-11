import socketio


sio = socketio.Client()


PHILU_SOCKET_URL = 'wss://community.philanthropyu.org/socket.io'
SOCKET_EVENT =  'categories.loadMoreCategories'
# PROXY_PASS = 'community.philanthropyu.org'
# PROXY_PORT = 443

# JWT_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWQiOjcsImVtYWlsIjoiYWRtaW5AcGhpbGFudGhyb3B5dS5vcmcifQ.ZEPi5-tC_1cC4nIUFYpKJBo3RzG9xPXwpivMAnKl72s'


@sio.event
def connect():
    print('connection established')

# @sio.on(SOCKET_EVENT)
# def loadCategories(data):
#     print('message received with ', data)

@sio.event
def disconnect():
    print('disconnected from server')


def callback(error, data2):
   print(error, data2)

sio.connect(PHILU_SOCKET_URL, headers={
    # 'token': '{}'.format(JWT_TOKEN)
}, transports='websocket')
print('CONNECTED')


payload = {
            'after': 0, # "12" -> "24" ...
            'queryParams': ''
        }

print("SENDING DATA")
sio.emit(SOCKET_EVENT, payload, callback=callback)
print("DATA SENT")
