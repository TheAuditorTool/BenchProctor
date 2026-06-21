# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest67817(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value}'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
