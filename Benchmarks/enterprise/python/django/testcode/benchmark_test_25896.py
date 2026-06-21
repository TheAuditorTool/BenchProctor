# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time
import ast


def BenchmarkTest25896(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    if time.time() > 1000000000:
        os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
