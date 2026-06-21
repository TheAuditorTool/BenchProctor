# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73327(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
