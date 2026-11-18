# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def format_digest(request):
    citation = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(citation).split(',')
    backorder = ' '.join(parts)
    try:
        jsonschema.validate(str(backorder), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    restock = backorder
    subprocess.Popen('echo ' + str(restock), shell=True).wait()
    return JsonResponse({"saved": True})
