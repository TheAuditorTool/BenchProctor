# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest20261(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
