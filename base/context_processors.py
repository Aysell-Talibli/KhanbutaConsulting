from .models import *
from .forms import SuscribeForm
def base_data(request):
    main_info=Main.objects.last()
    apps=SocialMedia.objects.all()
    images=BackgroundImage.objects.last()
    openinghours=OpeningHours.objects.all()
    social_medias=SocialMedia.objects.all()
    map=Map.objects.last()
    form=SuscribeForm()
    if request.method == 'POST':
        form=SuscribeForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            form.save()
    return {'apps':apps, 'main_info':main_info, 'images':images, 'map':map,
            'openinghours':openinghours, 'social_medias':social_medias, 'form':form}