# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse


def relay_value(value):
    return value

def BenchmarkTest02242(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = relay_value(forwarded_ip)
    if not re.fullmatch('^[\\w\\s.\\-:/=\\r\\n]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse('<html><body><h1>' + str(processed) + '</h1></body></html>', content_type='text/html')
