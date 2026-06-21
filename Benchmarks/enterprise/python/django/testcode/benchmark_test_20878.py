# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest20878(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return JsonResponse({'lookup': arr[idx]}, status=200)
