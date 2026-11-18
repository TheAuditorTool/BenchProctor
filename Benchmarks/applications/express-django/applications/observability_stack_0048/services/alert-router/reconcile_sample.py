# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def reconcile_sample(request):
    excerpt = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(excerpt).split(',')
    gauge = ' '.join(parts)
    try:
        jsonschema.validate(str(gauge), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    cohort = gauge
    subprocess.Popen('echo ' + str(cohort), shell=True).wait()
    return JsonResponse({"saved": True})
