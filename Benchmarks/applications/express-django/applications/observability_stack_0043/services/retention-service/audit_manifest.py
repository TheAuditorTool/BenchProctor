# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def audit_manifest(request):
    note = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(note)
    gauge = reader()
    return HttpResponse(mark_safe('<div>' + str(gauge) + '</div>'))
