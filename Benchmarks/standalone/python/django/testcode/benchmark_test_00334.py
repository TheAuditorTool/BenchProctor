# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def BenchmarkTest00334(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % str(header_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
