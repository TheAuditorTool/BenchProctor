# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def invoke_connector(request):
    excerpt = json.loads(request.body or b'{}').get("integrations_payload", "")
    parsed = json.loads(excerpt)
    return JsonResponse({'parsed': str(parsed)}, status=200)
