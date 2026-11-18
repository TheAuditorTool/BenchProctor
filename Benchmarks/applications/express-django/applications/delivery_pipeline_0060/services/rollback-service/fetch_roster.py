# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def fetch_roster(request):
    wording = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(wording).split(',')
    remark = ' '.join(parts)
    try:
        jsonschema.validate(str(remark), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    phrase = remark
    subprocess.Popen('echo ' + str(phrase), shell=True).wait()
    return JsonResponse({"saved": True})
