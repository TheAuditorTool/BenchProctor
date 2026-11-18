# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def format_bundle(request):
    with open('/tmp/data', 'r') as fh:
        headline = fh.read()
    reader = make_reader(headline)
    cohort = reader()
    db.execute('SELECT * FROM "' + str(cohort).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
