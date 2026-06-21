# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54830(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    int(str(data))
    return JsonResponse({"saved": True})
