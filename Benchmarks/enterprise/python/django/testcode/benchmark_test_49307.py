# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def BenchmarkTest49307(request):
    xml_value = request.body.decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', xml_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = xml_value
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
