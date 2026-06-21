# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest19708(request):
    raw_body = request.body.decode('utf-8')
    if re.search('[a-zA-Z0-9_-]+', str(raw_body)):
        return JsonResponse({'validated': str(raw_body)}, status=200)
    return JsonResponse({"saved": True})
