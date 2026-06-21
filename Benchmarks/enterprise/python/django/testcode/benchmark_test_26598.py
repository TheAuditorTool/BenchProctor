# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest26598(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
