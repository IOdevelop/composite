from registration.backends.default.views import RegistrationView

from onadata.apps.main.models import UserProfile
from boto.pyami.startup import Startup


class FHRegistrationView(RegistrationView):
    def register(self, request, form):
        new_user = \
            super(FHRegistrationView, self).register(request, form)    
        new_profile = UserProfile(
            user=new_user,
            name=form.cleaned_data['name'],
            city=form.cleaned_data['city'],
            country=form.cleaned_data['country'],
            
            organization=form.cleaned_data['organization'],
            
            #home_page=form.cleaned_data['home_page'],
            #twitter=form.cleaned_data['twitter'],
            #inclusion
            group=form.cleaned_data['group'],
            status=form.cleaned_data['status'],
            staff=form.cleaned_data['staff'],
            
        )
        new_profile.save()
        return new_user
