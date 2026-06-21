# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest10998(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    os.system('echo ' + str(referer_value))
    return JsonResponse({"saved": True})
