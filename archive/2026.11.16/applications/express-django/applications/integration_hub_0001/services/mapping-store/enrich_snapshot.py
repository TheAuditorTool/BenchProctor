# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def enrich_snapshot(request):
    quotation = request.COOKIES.get('session_token', '')
    handshake = quotation if quotation else 'default'
    try:
        jsonschema.validate(str(handshake), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    preface = handshake
    subprocess.Popen('echo ' + str(preface), shell=True).wait()
    return JsonResponse({"saved": True})
