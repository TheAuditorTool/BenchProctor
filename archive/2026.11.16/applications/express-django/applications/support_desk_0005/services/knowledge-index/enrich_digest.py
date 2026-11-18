# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def enrich_digest(request):
    phrase = request.COOKIES.get('session_token', '')
    inquiry = phrase if phrase else 'default'
    try:
        jsonschema.validate(str(inquiry), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    grievance = inquiry
    subprocess.Popen('echo ' + str(grievance), shell=True).wait()
    return JsonResponse({"saved": True})
