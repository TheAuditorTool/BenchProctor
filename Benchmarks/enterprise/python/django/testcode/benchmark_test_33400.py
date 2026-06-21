# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33400(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
