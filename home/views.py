from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import UploadedImage, Diagnosis, Product
from .forms import UploadForm
from .ai import analyze_image
import requests


def analyze_the_image(image_path):
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        response = requests.post(
            'https://us-central1-aurora-457407.cloudfunctions.net/predict',
            files=files
        )

    if response.status_code == 200:
        return response.json()  # Expecting {'conditions': [...], 'products': [...]}
    else:
        raise Exception(f"API error: {response.status_code} - {response.text}")



def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.save()

            try:
                # Send image to your AI model
                result = analyze_the_image(uploaded.image.path)
                # Store result in session
                request.session['result_data'] = result
                # Redirect to results page
                return redirect('result')

            except Exception as e:
                form.add_error(None, f"Error analyzing image: {str(e)}")

    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})



def result_view(request):
    result = request.session.get('result_data', {})
    print(result)
    products = Product.objects.all()
    return render(request, 'result.html', {'result': result, 'products': products})
