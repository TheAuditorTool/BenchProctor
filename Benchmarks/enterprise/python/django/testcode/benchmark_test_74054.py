# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74054(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = auth_header
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
