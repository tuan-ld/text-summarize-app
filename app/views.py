from django.shortcuts import render,render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from .forms import Paragraph
from . import getSummary


def landing_view(request):
	result = []
	form1 = Paragraph(request.POST or None)
	# form2 = UploadFileForm(request.POST, request.FILES)
	if form1.is_valid():
		result = getSummary.main(form1.cleaned_data.get('Text'))
		form1 = Paragraph()
	else:
		form1 = Paragraph()
	context = {
		"form1" : form1,
		# "form2" : form2,
		"result" : result,
	}
	return render(request, "landing.html", context)


def index(request):
	context = RequestContext(request)
	return render(request, "index.html")	