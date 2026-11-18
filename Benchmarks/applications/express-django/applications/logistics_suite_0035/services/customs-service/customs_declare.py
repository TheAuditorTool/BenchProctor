# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json
import re


@csrf_exempt
def declare_customs(request):
    summary = json.loads(request.body or b'{}').get("shipping_payload", "")
    if not re.fullmatch("^(asc|desc|name|created)$", str(summary)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    consignment = summary
    subprocess.run('echo ' + str(consignment), shell=True)
    return JsonResponse({"saved": True})
