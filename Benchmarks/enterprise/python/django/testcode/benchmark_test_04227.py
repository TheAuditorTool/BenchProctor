# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04227(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
