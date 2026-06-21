# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest04471(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    os.remove(str(data))
    return JsonResponse({"saved": True})
