# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00263(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % str(forwarded_ip)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
