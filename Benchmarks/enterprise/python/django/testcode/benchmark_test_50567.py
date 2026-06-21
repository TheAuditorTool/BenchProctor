# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50567(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
