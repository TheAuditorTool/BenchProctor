# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19523(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
