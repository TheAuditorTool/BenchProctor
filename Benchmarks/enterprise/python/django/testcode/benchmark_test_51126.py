# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest51126(request):
    user_id = request.GET.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
