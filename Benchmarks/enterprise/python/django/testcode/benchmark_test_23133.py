# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest23133(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    json.loads(forwarded_ip)
    return JsonResponse({"saved": True})
