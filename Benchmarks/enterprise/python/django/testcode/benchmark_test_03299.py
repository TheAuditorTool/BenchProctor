# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03299(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
