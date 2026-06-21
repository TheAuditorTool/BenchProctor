# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81087(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
