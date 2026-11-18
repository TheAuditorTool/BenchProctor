# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def merge_roster(request):
    synopsis = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(synopsis).split(',')
    verdict = ' '.join(parts)
    try:
        jsonschema.validate(str(verdict), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    grievance = verdict
    subprocess.Popen('echo ' + str(grievance), shell=True).wait()
    return JsonResponse({"saved": True})
