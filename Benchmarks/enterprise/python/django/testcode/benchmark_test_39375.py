# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest39375(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
