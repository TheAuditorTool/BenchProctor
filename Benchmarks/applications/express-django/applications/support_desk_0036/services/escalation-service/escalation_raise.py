# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from pathlib import Path


@csrf_exempt
def raise_escalation(request):
    quotation = json.loads(request.body or b'{}').get("support_payload", "")
    if not re.fullmatch("^(asc|desc|name|created)$", str(quotation)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    inquiry = quotation
    Path('/var/app/data/' + str(inquiry)).write_text('data')
    return JsonResponse({"saved": True})
