# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from urllib.parse import unquote


def BenchmarkTest71785(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
