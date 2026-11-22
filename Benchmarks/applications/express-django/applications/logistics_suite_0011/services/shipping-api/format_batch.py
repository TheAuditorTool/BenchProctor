# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def format_batch(request):
    citation = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    reader = make_reader(citation)
    consignment = reader()
    with open('/var/app/data/' + str(consignment), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
