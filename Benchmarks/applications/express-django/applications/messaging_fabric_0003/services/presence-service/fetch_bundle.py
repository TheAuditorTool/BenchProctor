# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def fetch_bundle(request):
    with open('/tmp/data', 'r') as fh:
        subject = fh.read()
    reader = make_reader(subject)
    bulletin = reader()
    db.execute('SELECT * FROM "' + str(bulletin).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
