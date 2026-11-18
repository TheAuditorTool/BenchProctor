# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def enrich_summary(request):
    paragraph = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(paragraph)
    yaml.load(bulletin, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
