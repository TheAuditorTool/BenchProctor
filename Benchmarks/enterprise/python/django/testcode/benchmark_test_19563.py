# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19563(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
