# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26632(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
