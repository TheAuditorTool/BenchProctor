# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest57258(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    os.remove(str(data))
    return JsonResponse({"saved": True})
