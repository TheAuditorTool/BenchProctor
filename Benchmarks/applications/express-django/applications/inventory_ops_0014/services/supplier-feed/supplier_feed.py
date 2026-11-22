# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def pull_supplier_feed(request):
    memo = json.loads(request.body or b'{}').get("inventory_payload", "")
    if memo not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    backorder = memo
    os.system('echo ' + str(backorder))
    return JsonResponse({"saved": True})
