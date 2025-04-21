from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import UploadedImage, Diagnosis, Product
from .forms import UploadForm
from .ai import analyze_image


def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.save()
            result = analyze_image(uploaded.image.path)

            diagnosis = Diagnosis.objects.create(
                image=uploaded,
                result=", ".join(result['conditions']),
                recommended_products=", ".join(map(str, result['products']))
            )
            return redirect('result', diagnosis_id=diagnosis.id)
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})


def result_view(request, diagnosis_id):
    diagnosis = Diagnosis.objects.get(id=diagnosis_id)
    product_ids = map(int, diagnosis.recommended_products.split(','))
    products = Product.objects.filter(id__in=product_ids)
    return render(request, 'result.html', {'diagnosis': diagnosis, 'products': products})
