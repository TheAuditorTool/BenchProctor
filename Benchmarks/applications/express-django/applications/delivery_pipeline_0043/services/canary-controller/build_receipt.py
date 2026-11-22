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
def build_receipt(request):
    remark = request.META.get('HTTP_REFERER', '')
    reader = make_reader(remark)
    note = reader()
    try:
        jsonschema.validate(str(note), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    phrase = note
    subprocess.run('echo ' + str(phrase), shell=True)
    return JsonResponse({"saved": True})
