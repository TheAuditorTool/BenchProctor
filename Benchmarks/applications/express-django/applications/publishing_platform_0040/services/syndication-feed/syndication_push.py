# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def push_syndication(request):
    subtitle = json.loads(request.body or b'{}').get("publishing_payload", "")
    parsed = json.loads(subtitle)
    return JsonResponse({'parsed': str(parsed)}, status=200)
