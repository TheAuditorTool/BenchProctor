# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def merge_summary(request):
    phrase = request.COOKIES.get('session_token', '')
    backorder = phrase if phrase else 'default'
    try:
        jsonschema.validate(str(backorder), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    restock = backorder
    subprocess.Popen('echo ' + str(restock), shell=True).wait()
    return JsonResponse({"saved": True})
