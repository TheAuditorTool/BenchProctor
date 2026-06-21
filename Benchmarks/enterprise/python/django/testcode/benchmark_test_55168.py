# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest55168(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
