# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest08112(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    json.loads(data)
    return JsonResponse({"saved": True})
