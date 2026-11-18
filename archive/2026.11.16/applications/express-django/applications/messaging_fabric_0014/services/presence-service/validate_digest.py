# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def validate_digest(request):
    summary = request.COOKIES.get('session_token', '')
    bulletin = summary if summary else 'default'
    try:
        jsonschema.validate(str(bulletin), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    notice = bulletin
    subprocess.Popen('echo ' + str(notice), shell=True).wait()
    return JsonResponse({"saved": True})
