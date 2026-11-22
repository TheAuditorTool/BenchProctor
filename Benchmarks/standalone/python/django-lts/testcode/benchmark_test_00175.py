# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00175(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
