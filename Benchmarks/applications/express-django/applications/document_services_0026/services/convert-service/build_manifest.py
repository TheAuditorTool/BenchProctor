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
def build_manifest(request):
    preface = request.META.get('HTTP_REFERER', '')
    reader = make_reader(preface)
    addendum = reader()
    try:
        jsonschema.validate(str(addendum), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    dossier = addendum
    subprocess.run('echo ' + str(dossier), shell=True)
    return JsonResponse({"saved": True})
