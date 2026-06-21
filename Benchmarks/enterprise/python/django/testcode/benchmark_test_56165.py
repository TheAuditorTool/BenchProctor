# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest56165(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
