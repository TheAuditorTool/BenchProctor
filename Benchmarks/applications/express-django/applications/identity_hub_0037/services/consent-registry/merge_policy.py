# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def merge_policy(request):
    remark = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    reader = make_reader(remark)
    persona = reader()
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
