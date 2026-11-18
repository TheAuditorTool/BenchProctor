# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def upload_asset(request):
    blurb = json.loads(request.body or b'{}').get("media_payload", "")
    parsed = json.loads(blurb)
    return JsonResponse({'parsed': str(parsed)}, status=200)
