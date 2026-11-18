# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def resolve_ledger(request):
    notice = request.COOKIES.get('session_token', '')
    persona = notice if notice else 'default'
    try:
        jsonschema.validate(str(persona), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    handshake = persona
    subprocess.Popen('echo ' + str(handshake), shell=True).wait()
    return JsonResponse({"saved": True})
