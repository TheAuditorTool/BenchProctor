# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02052(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
