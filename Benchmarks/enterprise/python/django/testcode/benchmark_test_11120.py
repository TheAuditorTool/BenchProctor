# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest11120(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
