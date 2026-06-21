# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39057(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
