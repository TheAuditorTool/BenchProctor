# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest26010(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = normalise_input(referer_value)
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
