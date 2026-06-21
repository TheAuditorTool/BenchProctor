# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest64504(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    json.loads(data)
    return JsonResponse({"saved": True})
