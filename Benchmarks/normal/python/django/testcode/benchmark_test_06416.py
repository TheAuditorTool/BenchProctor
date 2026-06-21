# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from urllib.parse import unquote


def BenchmarkTest06416(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
