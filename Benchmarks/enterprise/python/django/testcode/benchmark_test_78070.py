# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest78070(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
