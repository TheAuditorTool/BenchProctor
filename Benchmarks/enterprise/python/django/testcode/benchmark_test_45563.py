# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest45563(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
