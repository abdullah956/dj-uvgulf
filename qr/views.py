from django.shortcuts import render, redirect, get_object_or_404
from .forms import OperatorCertificationForm
from .models import OperatorCertification
import qrcode
from io import BytesIO
from django.http import HttpResponse

def add_certification(request):
    if request.method == 'POST':
        form = OperatorCertificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('certification_list')  # Ensure 'certification_list' is the correct URL name
    else:
        form = OperatorCertificationForm()

    return render(request, 'add_certification.html', {'form': form})

def certification_list(request):
    certifications = OperatorCertification.objects.all()
    return render(request, 'certification_list.html', {'certifications': certifications})

def generate_qr_code(request, tac_number):
    # Retrieve the certificate using the TAC number
    certificate = get_object_or_404(OperatorCertification, tac_number=tac_number)
    
    # Generate a URL to the certificate details page
    certificate_url = request.build_absolute_uri(f'/certificate/{tac_number}/')

    # Generate QR code with the URL to the certificate
    img = qrcode.make(certificate_url)

    # Save the image to a BytesIO object
    qr_io = BytesIO()
    img.save(qr_io)
    qr_io.seek(0)

    # Return the image as an HTTP response
    return HttpResponse(qr_io, content_type='image/png')


def certificate_details(request, tac_number):
    # Retrieve the certificate using the TAC number
    certificate = get_object_or_404(OperatorCertification, tac_number=tac_number)
    
    # Render the certificate details page
    return render(request, 'certificate_details.html', {'certificate': certificate})
