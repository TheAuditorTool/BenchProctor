# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76157(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
