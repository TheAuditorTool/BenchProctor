# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def rotate_payout(request):
    subtitle = request.COOKIES.get('session_token', '')
    ledger = subtitle if subtitle else 'default'
    try:
        jsonschema.validate(str(ledger), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    remittance = ledger
    subprocess.Popen('echo ' + str(remittance), shell=True).wait()
    return JsonResponse({"saved": True})
