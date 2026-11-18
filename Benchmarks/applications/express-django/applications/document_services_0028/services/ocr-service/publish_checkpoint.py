# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def publish_checkpoint(request):
    note = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(note)
    yaml.load(addendum, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
