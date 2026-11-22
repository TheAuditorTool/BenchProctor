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
def resolve_cart(request):
    subject = request.META.get('HTTP_REFERER', '')
    reader = make_reader(subject)
    voucher = reader()
    try:
        jsonschema.validate(str(voucher), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    backorder = voucher
    subprocess.run('echo ' + str(backorder), shell=True)
    return JsonResponse({"saved": True})
