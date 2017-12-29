import asyncio
import os
import webbrowser
import pickle

import websockets


class WebServer:
    @asyncio.coroutine
    def query_handler(self, websocket, path):
        review = yield from websocket.recv()
        with open('model.md', 'rb') as file_from:
            model = pickle.load(file_from)
        res = model.predict([review])[0]
        yield from websocket.send(str(res))

    def run_server(self):
        start_server = websockets.serve(self.query_handler, 'localhost', 9999)
        asyncio.get_event_loop().run_until_complete(start_server)

        filename = os.path.join(os.path.dirname(__file__), 'review.html')

        webbrowser.open_new_tab('file://' + os.path.realpath(filename))

        try:
            asyncio.get_event_loop().run_forever()
        except:
            pass

web_server = WebServer()
web_server.run_server()