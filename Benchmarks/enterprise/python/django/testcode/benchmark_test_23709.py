# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest23709(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
