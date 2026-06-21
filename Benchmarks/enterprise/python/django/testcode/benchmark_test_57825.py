# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57825(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    int(str(data))
    return JsonResponse({"saved": True})
