# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def format_header(request):
    caption = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(caption)
    yaml.load(gauge, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
