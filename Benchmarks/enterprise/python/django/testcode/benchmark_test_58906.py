# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest58906(request):
    raw_body = request.body.decode('utf-8')
    os.system('echo ' + str(raw_body))
    return JsonResponse({"saved": True})
