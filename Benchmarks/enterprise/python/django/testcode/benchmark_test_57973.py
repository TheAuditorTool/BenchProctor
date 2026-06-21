# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57973(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    eval(str(data))
    return JsonResponse({"saved": True})
