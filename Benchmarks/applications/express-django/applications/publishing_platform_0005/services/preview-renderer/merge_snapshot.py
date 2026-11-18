# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def merge_snapshot(request):
    footnote = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(footnote).split(',')
    byline = ' '.join(parts)
    try:
        jsonschema.validate(str(byline), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    addendum = byline
    subprocess.Popen('echo ' + str(addendum), shell=True).wait()
    return JsonResponse({"saved": True})
