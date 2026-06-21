# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest28900(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
