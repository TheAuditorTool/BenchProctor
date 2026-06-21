# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59655(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    int(str(data))
    return JsonResponse({"saved": True})
