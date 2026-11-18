# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00511(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
