# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18927(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
