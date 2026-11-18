# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def compact_roster(request):
    summary = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(summary).split(',')
    grievance = ' '.join(parts)
    try:
        jsonschema.validate(str(grievance), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    verdict = grievance
    subprocess.Popen('echo ' + str(verdict), shell=True).wait()
    return JsonResponse({"saved": True})
