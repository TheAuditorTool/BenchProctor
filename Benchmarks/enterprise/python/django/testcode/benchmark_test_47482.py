# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47482(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
