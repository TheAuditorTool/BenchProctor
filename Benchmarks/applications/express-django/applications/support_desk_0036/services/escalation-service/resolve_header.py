# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import jsonschema


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def resolve_header(request):
    preface = request.META.get('HTTP_REFERER', '')
    reader = make_reader(preface)
    grievance = reader()
    try:
        jsonschema.validate(str(grievance), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    inquiry = grievance
    subprocess.run('echo ' + str(inquiry), shell=True)
    return JsonResponse({"saved": True})
