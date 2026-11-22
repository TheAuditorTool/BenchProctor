# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def render_secret(request):
    subtitle = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    reader = make_reader(subtitle)
    persona = reader()
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
