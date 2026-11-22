# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema
import json


@csrf_exempt
def update_profile(request):
    phrase = json.loads(request.body or b'{}').get("identity_payload", "")
    try:
        jsonschema.validate(str(phrase), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    blurb = phrase
    subprocess.run('echo ' + str(blurb), shell=True)
    return JsonResponse({"saved": True})
