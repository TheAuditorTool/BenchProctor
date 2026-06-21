# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34262(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    exec(str(data))
    return JsonResponse({"saved": True})
