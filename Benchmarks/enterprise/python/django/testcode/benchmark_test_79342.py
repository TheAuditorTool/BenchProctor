# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from urllib.parse import unquote


def BenchmarkTest79342(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
