# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02531(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
