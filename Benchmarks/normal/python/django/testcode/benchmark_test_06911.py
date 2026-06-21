# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest06911(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
