# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13555(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
