# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def export_article(request):
    note = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    reader = make_reader(note)
    byline = reader()
    with open('/var/app/data/' + str(byline), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
