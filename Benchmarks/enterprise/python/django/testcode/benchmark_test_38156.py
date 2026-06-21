# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38156(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
