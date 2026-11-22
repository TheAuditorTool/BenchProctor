# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00098(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session.update({'data': str(processed)})
    return JsonResponse({"saved": True})
