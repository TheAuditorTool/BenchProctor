# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


@csrf_exempt
def rotate_document(request):
    remark = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(remark).split(',')
    synopsis = ' '.join(parts)
    try:
        jsonschema.validate(str(synopsis), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    quotation = synopsis
    subprocess.Popen('echo ' + str(quotation), shell=True).wait()
    return JsonResponse({"saved": True})
