# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest63976(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
