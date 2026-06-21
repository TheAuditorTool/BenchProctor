# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79648(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
