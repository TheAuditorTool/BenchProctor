# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest41817(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    os.remove(str(data))
    return JsonResponse({"saved": True})
