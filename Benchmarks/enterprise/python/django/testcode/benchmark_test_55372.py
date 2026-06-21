# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55372(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    eval(str(data))
    return JsonResponse({"saved": True})
