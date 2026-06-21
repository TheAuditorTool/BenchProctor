# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43747(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    int(str(data))
    return JsonResponse({"saved": True})
