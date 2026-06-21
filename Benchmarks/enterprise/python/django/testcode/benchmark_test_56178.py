# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest56178(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
