# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest12899(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
