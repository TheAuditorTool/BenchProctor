# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest10415(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', auth_header):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = auth_header
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return JsonResponse({'lookup': arr[idx]}, status=200)
