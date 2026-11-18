# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema
import json


@csrf_exempt
def lookup_sku(request):
    memo = json.loads(request.body or b'{}').get("inventory_payload", "")
    try:
        jsonschema.validate(str(memo), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    restock = memo
    subprocess.Popen('echo ' + str(restock), shell=True).wait()
    return JsonResponse({"saved": True})
