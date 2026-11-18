# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def load_policy(request):
    passage = request.COOKIES.get('session_token', '')
    remittance = passage if passage else 'default'
    try:
        jsonschema.validate(str(remittance), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    disbursement = remittance
    subprocess.Popen('echo ' + str(disbursement), shell=True).wait()
    return JsonResponse({"saved": True})
