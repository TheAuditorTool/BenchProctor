# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15637(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
