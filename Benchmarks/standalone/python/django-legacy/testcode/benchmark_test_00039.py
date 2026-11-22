# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache


def BenchmarkTest00039(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value!s}'
    cache.set('active_tenant', str(data), None)
    return JsonResponse({"saved": True})
