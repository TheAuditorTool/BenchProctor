# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def reconcile_roster(request):
    transcript = request.META.get('HTTP_AUTHORIZATION', '')
    if transcript:
        parcel = transcript
    else:
        parcel = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': parcel})))
