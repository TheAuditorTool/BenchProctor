# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50206(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
