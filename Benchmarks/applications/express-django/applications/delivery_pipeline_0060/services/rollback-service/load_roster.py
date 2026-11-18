# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def load_roster(request):
    wording = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    remark = normalize(wording)
    yaml.load(remark, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
