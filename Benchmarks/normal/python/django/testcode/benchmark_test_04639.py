# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest04639(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    processed = shlex.quote(origin_value)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
