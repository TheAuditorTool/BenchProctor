# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48932(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
