# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45339(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
