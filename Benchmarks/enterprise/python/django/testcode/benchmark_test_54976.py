# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54976(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
