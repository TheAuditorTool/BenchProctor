# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12816(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
