# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def export_summary(request):
    summary = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(summary).split(',')
    cohort = ' '.join(parts)
    try:
        jsonschema.validate(str(cohort), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    gauge = cohort
    subprocess.Popen('echo ' + str(gauge), shell=True).wait()
    return JsonResponse({"saved": True})
