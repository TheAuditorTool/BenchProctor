# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import socket
import urllib.parse


def BenchmarkTest00108(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
