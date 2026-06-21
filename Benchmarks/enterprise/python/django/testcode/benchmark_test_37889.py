# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest37889(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
