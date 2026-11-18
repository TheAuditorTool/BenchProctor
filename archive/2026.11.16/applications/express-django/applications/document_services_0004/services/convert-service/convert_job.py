# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema
import json


@csrf_exempt
def run_conversion(request):
    headline = json.loads(request.body or b'{}').get("documents_payload", "")
    try:
        jsonschema.validate(str(headline), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    addendum = headline
    subprocess.Popen('echo ' + str(addendum), shell=True).wait()
    return JsonResponse({"saved": True})
