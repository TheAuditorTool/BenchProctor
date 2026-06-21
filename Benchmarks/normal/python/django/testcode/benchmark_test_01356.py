# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest01356(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', header_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = header_value
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return JsonResponse({'lookup': arr[idx]}, status=200)
