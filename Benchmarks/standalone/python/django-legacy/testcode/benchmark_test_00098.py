# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00098(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ' '.join(str(forwarded_ip).split())
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
