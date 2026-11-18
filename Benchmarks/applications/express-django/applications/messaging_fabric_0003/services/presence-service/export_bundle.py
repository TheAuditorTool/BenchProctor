# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def export_bundle(request):
    subject = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(subject)
    bulletin = reader()
    os.unlink('/var/app/data/' + str(bulletin))
    return JsonResponse({"saved": True})
