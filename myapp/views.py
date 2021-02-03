from django.shortcuts import render
from myapp.form import StudentForm
from myapp.models import Employee
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from myapp.functions.functions import handle_uploaded_file
import csv


def getpdf(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment'; filename="file.pdf"
	p = canvas.Canvas(response)
	p.setFont("Times-Roman",55)
	p.drawString(100,700,"hello, jemin!!")
	p.showPage()
	p.save()
	return response

def index(request):
	return render(request, 'index.html')
# def index(request):
# 	template = loader.get_template('index.html')
# 	name = {
# 		'student' : 'jemin'

# 	}
# 	return HttpResponse(template.render(name))

# def image(request):
# 	return render(request,'index.html')


# def index2(request):
# 	stu = StudentForm()
# 	return render(request,"index.html",{'form':student})
		

# @require_http_methods(["GET"])
# def show(request):
# 	return HttpResponse('<h1>this is http get request.</h1>')