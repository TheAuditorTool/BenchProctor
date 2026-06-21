# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59819(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
