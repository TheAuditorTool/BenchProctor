# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def archive_snapshot(request):
    footnote = request.body.decode('utf-8')
    consignment = footnote if footnote else 'default'
    parcel = bleach.clean(consignment)
    return HttpResponse(mark_safe('<div>' + str(parcel) + '</div>'))
