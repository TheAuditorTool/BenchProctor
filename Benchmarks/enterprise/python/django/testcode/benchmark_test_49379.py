# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49379(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
