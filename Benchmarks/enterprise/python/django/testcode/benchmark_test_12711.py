# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64


def BenchmarkTest12711(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
