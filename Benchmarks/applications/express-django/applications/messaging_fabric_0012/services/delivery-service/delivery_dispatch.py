# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def dispatch_delivery(request):
    remark = json.loads(request.body or b'{}').get("messaging_payload", "")
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, remark))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    citation = full_path
    os.unlink(citation)
    return JsonResponse({"saved": True})
