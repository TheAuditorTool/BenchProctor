# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02859(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
