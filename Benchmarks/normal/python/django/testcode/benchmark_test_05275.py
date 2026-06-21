# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05275(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
