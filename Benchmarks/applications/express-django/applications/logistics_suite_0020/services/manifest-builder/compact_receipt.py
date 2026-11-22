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
def compact_receipt(request):
    transcript = request.META.get('HTTP_REFERER', '')
    reader = make_reader(transcript)
    consignment = reader()
    try:
        jsonschema.validate(str(consignment), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    parcel = consignment
    subprocess.run('echo ' + str(parcel), shell=True)
    return JsonResponse({"saved": True})
