"""larc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.decorators import renderer_classes
from django.contrib import admin
from django.urls import path, include
from larcauth.models import AECUser, academicyear, gender , parentutor, student_has_termsubjeval, evaluation,classroom_termsubject,natureparentutor, learner_has_termsubject
from rest_framework import routers, serializers, viewsets
from larcauth.views import index 
from larcauth import urls 
from oauth2_provider import urls
import larcauth

#--------------------------------------------------------
# Serializers define the API representation.
#--------------------------------------------------------

class parentutorSerializer(serializers.ModelSerializer ):
    class Meta:
        model = parentutor
        fields = ['aecuser_ptr_id','fk_parentutor_nature_id'] 

class natureparentutorSerializer(serializers.ModelSerializer ):
    class Meta:
        model = natureparentutor
        fields = ['id','label'] 

class genderSerializer(serializers.ModelSerializer ):
    class Meta:
        model = gender
        fields = ["id"] 

class learner_has_termsubjectSerializer(serializers.ModelSerializer ):
    class Meta:
        model = learner_has_termsubject
        fields = ['id','fk_student','fk_classroom_termsubject','enabled'] 

class classroom_termsubjectSerializer(serializers.ModelSerializer ):
    class Meta:
        model = classroom_termsubject
        fields = ['label','id'] 

class evaluationSerializer(serializers.ModelSerializer ):
    class Meta:
        model = evaluation
        fields = ['id','index_eval', 'label', 'nature', 'baremeNoteDP', 'baremeNoteCritere', 'crit_a', 'crit_b', 'crit_c', 'crit_d','nb_stud','nb_stud_a','nb_stud_b','nb_stud_c','nb_stud_d','nb_stud_a','average','average_a','average_b','average_c','average_d','maxim','maxim_a','maxim_b','maxim_c','maxim_d','minim','minim_a','minim_b','minim_c','minim_d', 'nb_mark','nb_mark_a','nb_mark_b','nb_mark_c','nb_mark_d', 'all_grades','all_grades_a','all_grades_b','all_grades_c','all_grades_d','updated','active','fk_classroom','fk_term'] 

class academicyearSerializer(serializers.ModelSerializer ):
    class Meta:
        model = academicyear
        fields = ["current_term_number","label"] 

class AECUserSerializer(serializers.ModelSerializer ):
    class Meta:
        model = AECUser
        fields = ['username','id', 'email', 'last_name', 'first_name','type_student', 'type_teacher', 'type_parentutor','type_coordonator','type_supervisor','type_director','fk_gender', 'fk_parent_id','picture2'] 

class student_has_termsubjevalSerialiser(serializers.ModelSerializer ):
    class Meta:
        model = student_has_termsubjeval
        fields = ['note','crit_a','crit_b','crit_c','crit_d','ref_idstudent','ref_evaluation','ref_term','mod_version' ]
 

#--------------------------------------------------------
# ViewSets define the view behavior.
#--------------------------------------------------------
class academicyearSet(viewsets.ReadOnlyModelViewSet):
#    permission_classes = (IsAuthenticated,)
    serializer_class = academicyearSerializer
    queryset = academicyear.objects.all()

class parentutorSet(viewsets.ReadOnlyModelViewSet):
#    permission_classes = (IsAuthenticated,)
    serializer_class = parentutorSerializer
    queryset = parentutor.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','fk_parentutor_nature_id' )

class natureparentutorSet(viewsets.ReadOnlyModelViewSet):
#    permission_classes = (IsAuthenticated,)
    serializer_class = natureparentutorSerializer
    queryset = natureparentutor.objects.all()

class genderSet(viewsets.ReadOnlyModelViewSet):
#    permission_classes = (IsAuthenticated,)
    serializer_class = genderSerializer
    queryset = gender.objects.all()

class learner_has_termsubjectSet(viewsets.ReadOnlyModelViewSet ):
#    #permission_classes = (IsAuthenticated,)
    serializer_class = learner_has_termsubjectSerializer
    queryset = learner_has_termsubject.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fk_student','enabled' )

class AECUserViewSet(viewsets.ReadOnlyModelViewSet):
#    permission_classes = (IsAuthenticated,)
    serializer_class = AECUserSerializer
    queryset = AECUser.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username','fk_parent_id' )

class student_has_termsubjevalSet(viewsets.ReadOnlyModelViewSet):
#    permission_classes = (IsAuthenticated,)
    serializer_class = student_has_termsubjevalSerialiser
    queryset = student_has_termsubjeval.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('ref_idstudent','ref_term','mod_version' )

class evaluationSet(viewsets.ReadOnlyModelViewSet):
#    permission_classes = (IsAuthenticated,)
    serializer_class = evaluationSerializer
    queryset = evaluation.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('fk_classroom','active','fk_term')
    ordering_fields = ['fk_classroom', 'id']

class classroom_termsubjectViewSet(viewsets.ReadOnlyModelViewSet):
#    permission_classes = (IsAuthenticated,)
    serializer_class = classroom_termsubjectSerializer
    queryset = classroom_termsubject.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('label')


# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'year', academicyearSet)
#router.register(r'gender', genderSet)
router.register(r'users', AECUserViewSet)
router.register(r'grades', student_has_termsubjevalSet)
router.register(r'evals', evaluationSet)
router.register(r'termsubjects', classroom_termsubjectViewSet)
router.register(r'links', learner_has_termsubjectSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = (
    path(r'admin/',admin.site.urls),
    path(r'auth/',include('oauth2_provider.urls', namespace ='oauth2_provider')),
    path('checkserver/',index ,name ='index'),
    path('', include(router.urls)),
    path('', include(larcauth.urls)),
)