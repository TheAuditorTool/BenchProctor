# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def annotate_summary(request, path_param):
    footnote = request.path.split('/')[-1]
    reader = make_reader(footnote)
    byline = reader()
    db.execute("SELECT * FROM users WHERE id = '" + str(byline) + "'")
    return JsonResponse({"saved": True})
