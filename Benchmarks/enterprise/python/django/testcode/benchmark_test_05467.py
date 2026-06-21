# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05467(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
