# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def normalize_profile(request):
    citation = request.POST.get('field', '')
    if citation:
        dossier = citation
    else:
        dossier = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': dossier})))
