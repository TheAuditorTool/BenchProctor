# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01080(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
