# SPDX-License-Identifier: Apache-2.0
import json
from django.http import HttpResponse


def BenchmarkTest00181(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = json.loads(json_value).get('value', '')
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(data) + '</div>')
    return resp
