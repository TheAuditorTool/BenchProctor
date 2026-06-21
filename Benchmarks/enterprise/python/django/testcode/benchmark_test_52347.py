# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52347(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    eval(str(data))
    return JsonResponse({"saved": True})
