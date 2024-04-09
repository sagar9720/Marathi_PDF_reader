from PyPDF2 import PdfReader
import re

# views.py
from django.shortcuts import render, redirect
from .forms import PDFUploadForm

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            # Save the uploaded file to disk
            with open('uploaded_file.pdf', 'wb') as f:
                for chunk in pdf_file.chunks():
                    f.write(chunk)
            return redirect('show_summary')
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})

def show_summary(request):
    # Process the uploaded PDF (you can do your processing here)
    # For demonstration purposes, let's assume we're just displaying the file name
    uploaded_file_name = 'uploaded_file.pdf'
    extracted_text = extract_text_from_pdf(uploaded_file_name)
    marathi_words = extract_marathi_words(extracted_text)

    return render(request, 'show_summary.html', {'marathi_words': marathi_words})




def extract_text_from_pdf(pdf_file_name):
    text = ''
    with open(pdf_file_name, 'rb') as file:
        reader = PdfReader(file)
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            text += page.extract_text()
    return text


def extract_marathi_words(text):
    # Define a regular expression pattern to match Marathi words
    # Here, \u0900-\u097F represents the Unicode range for Marathi characters
    # marathi_pattern = re.compile(r'[\u0900-\u097F]+')
    # marathi_pattern = re.compile(r'[\u0900-\u097F]+')
    marathi_pattern = re.compile(r'[\u0900-\u094F\u0951-\u097F]+')
    # marathi_pattern = re.compile(r'[^\u0966-\u096F\u0900-\u0963\u0965-\u097F\s]+')
    # marathi_pattern = re.compile(r'[\u0900-\u097F]+\D+')

    # Find all matches of the pattern in the text
    marathi_words = marathi_pattern.findall(text)

    # Join the matches to form a single string
    marathi_text = ' '.join(marathi_words)

    return marathi_text


















# from rest_framework import viewsets
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework.views import APIView
# from django.conf import settings
# #================
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .utils import generate_summary  # Assuming you have a function to generate summary
# from .forms import PDFUploadForm  # Assuming you have a form for uploading PDF


# # from restfilesupload.serializers import FileSerializer

# # file = serializers.FileField(upload_to='/..')

# # class get_pdf_summary(APIView):
# #     def post(self, request):
# #         print("hiii ajay")
# #         return Response([{'Status': "Success"}], status=status.HTTP_200_OK)
    

# # class HelloWorldView(APIView):
# #     def get(self, request):
# #         return render(request, 'home.html', {'message': 'Hello World!'})

# def get_pdf_summary(request):
#     return render(request, 'home.html', {'message': 'Hello World!'})
