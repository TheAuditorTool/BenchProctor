# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest20221(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
