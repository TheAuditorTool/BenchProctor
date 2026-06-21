# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest77516(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    os.remove(str(data))
    return JsonResponse({"saved": True})
