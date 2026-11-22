# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00014(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    if match is None:
        return JsonResponse({'error': 'not an email address'}, status=400)
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
