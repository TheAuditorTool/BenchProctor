# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest51797(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
