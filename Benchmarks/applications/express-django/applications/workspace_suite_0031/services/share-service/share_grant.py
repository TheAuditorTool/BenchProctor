# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def grant_share(request):
    quotation = json.loads(request.body or b'{}').get("workspace_payload", "")
    parsed = json.loads(quotation)
    return JsonResponse({'parsed': str(parsed)}, status=200)
