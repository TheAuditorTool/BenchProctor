# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def search_knowledge(request):
    note = json.loads(request.body or b'{}').get("support_payload", "")
    parsed = json.JSONDecoder().decode(str(note))
    return JsonResponse({'parsed': str(parsed)}, status=200)
