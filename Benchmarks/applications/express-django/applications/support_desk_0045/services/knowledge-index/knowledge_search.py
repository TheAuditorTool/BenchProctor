# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml
import json


@csrf_exempt
def search_knowledge(request):
    tagline = json.loads(request.body or b'{}').get("support_payload", "")
    yaml.load(tagline, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
