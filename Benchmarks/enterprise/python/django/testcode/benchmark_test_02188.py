# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest02188(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
