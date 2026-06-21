# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest23853(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
