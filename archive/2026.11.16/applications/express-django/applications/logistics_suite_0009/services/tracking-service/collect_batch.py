# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def collect_batch(request):
    subject = request.COOKIES.get('session_token', '')
    parcel = subject if subject else 'default'
    try:
        jsonschema.validate(str(parcel), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    consignment = parcel
    subprocess.Popen('echo ' + str(consignment), shell=True).wait()
    return JsonResponse({"saved": True})
