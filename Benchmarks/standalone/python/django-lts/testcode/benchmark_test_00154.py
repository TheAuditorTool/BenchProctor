# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00154(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
