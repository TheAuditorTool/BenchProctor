# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest34719(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
