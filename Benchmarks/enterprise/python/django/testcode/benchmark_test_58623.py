# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58623(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
