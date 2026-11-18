# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def BenchmarkTest00495(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
