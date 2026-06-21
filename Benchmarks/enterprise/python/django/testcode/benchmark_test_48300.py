# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest48300(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
