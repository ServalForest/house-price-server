from http import HTTPStatus
import socketserver
import http.server
from model import get_price
import json
from urllib.parse import urlparse, parse_qs


def query_param_to_int(query_component, param_name):
    return int(query_component[param_name][0])


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        query_components = parse_qs(urlparse(self.path).query)
        # ask model for price
        price = get_price([
            query_param_to_int(query_components, 'LotArea'),
            query_param_to_int(query_components, 'YearBuilt'),
            query_param_to_int(query_components, '1stFlrSF'),
            query_param_to_int(query_components, '2ndFlrSF'),
            query_param_to_int(query_components, 'FullBath'),
            query_param_to_int(query_components, 'BedroomAbvGr'),
            query_param_to_int(query_components, 'TotRmsAbvGrd')
        ])

        # create JSON response with price
        response = {
            "price": price,
        }

        # Encode the JSON response into a string
        output = json.dumps(response).encode("utf-8")
        self.wfile.write(output)


# Start the server
httpd = socketserver.TCPServer(('', 8000), Handler)
print('* Server started on port', 8000)
httpd.serve_forever()
