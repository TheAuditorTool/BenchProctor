# SPDX-License-Identifier: Apache-2.0
import bleach
import json
from django.http import HttpResponse


def BenchmarkTest00086(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    processed = bleach.clean(data)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(processed) + '</div>')
    return resp
