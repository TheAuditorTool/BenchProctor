# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def verify_config(request):
    snippet = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    persona = normalize(snippet)
    yaml.load(persona, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
