# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00035(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(ua_value).strip()
        case _:
            data = str(ua_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session.update({'data': str(processed)})
    return JsonResponse({"saved": True})
