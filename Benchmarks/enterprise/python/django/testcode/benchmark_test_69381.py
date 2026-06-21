# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69381(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
