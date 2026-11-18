# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def annotate_snapshot(request):
    subject = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(subject)
    ledger = reader()
    return HttpResponse(mark_safe('<div>' + str(ledger) + '</div>'))
