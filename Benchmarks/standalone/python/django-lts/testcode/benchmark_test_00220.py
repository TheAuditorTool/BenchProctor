# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import socket
import urllib.parse


def BenchmarkTest00220(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
