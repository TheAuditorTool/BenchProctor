# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest72704(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
