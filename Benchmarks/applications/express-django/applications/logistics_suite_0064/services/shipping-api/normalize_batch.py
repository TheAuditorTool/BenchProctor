# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def normalize_batch(request):
    transcript = request.body.decode('utf-8')
    parcel = transcript if transcript else 'default'
    consignment = bleach.clean(parcel)
    return HttpResponse(mark_safe('<div>' + str(consignment) + '</div>'))
