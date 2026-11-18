# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def annotate_snapshot(request):
    paragraph = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(paragraph).split(',')
    bulletin = ' '.join(parts)
    try:
        jsonschema.validate(str(bulletin), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    synopsis = bulletin
    subprocess.Popen('echo ' + str(synopsis), shell=True).wait()
    return JsonResponse({"saved": True})
