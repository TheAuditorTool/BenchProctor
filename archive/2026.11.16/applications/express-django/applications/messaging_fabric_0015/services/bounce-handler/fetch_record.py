# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def fetch_record(request):
    heading = request.COOKIES.get('session_token', '')
    bulletin = heading if heading else 'default'
    try:
        jsonschema.validate(str(bulletin), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    excerpt = bulletin
    subprocess.Popen('echo ' + str(excerpt), shell=True).wait()
    return JsonResponse({"saved": True})
