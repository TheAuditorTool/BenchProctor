# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import socket


@csrf_exempt
def raise_escalation(request):
    notice = json.loads(request.body or b'{}').get("support_payload", "")
    s = socket.create_connection((str(notice), 80))
    s.close()
    return JsonResponse({"saved": True})
