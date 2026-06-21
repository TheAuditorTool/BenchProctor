# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56578(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
