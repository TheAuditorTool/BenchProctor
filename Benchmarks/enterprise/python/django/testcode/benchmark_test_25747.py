# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25747(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
