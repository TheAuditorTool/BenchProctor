# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import base64


def BenchmarkTest00003(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    if match is None:
        return JsonResponse({'error': 'not an email address'}, status=400)
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
