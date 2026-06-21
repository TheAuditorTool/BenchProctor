# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest24878(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
