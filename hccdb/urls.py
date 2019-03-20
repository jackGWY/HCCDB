# @Author  : Fizzyi
from django.conf.urls import url

from hccdb.views import *

urlpatterns = [
    #首页
    url(r'index/',index,name='index'),
    #gene
    url(r'gene/(?P<gene_number>\S+)',gene,name='gene'),
    url(r'genelist/',genelist,name='genelist'),
    # drug
    url(r'drug/(?P<drug_number>\S+)',drug,name='drug'),
    url(r'druglist/',druglist,name='druglist'),
    # literature
    url(r'literature/',literature,name='literature'),
    url(r'literaturelist/',literaturelist,name='literaturelist'),
    #pathway
    url(r'pathway/',pathway,name='pathway'),
    url(r'pathwaylist',pathwaylist,name='pathwaylist'),
    #PatientSample
    url(r'patientSampleList/',patientSamplelist,name='patientSampleList'),
    url(r'patientSample/(?P<patient_id>\S+)',patientsample,name='patientsample'),
    # 搜索
    url(r'search/',search,name='search'),
    #About
    url(r'About/',About,name='About'),
    url(r'Gene_Disease/',Gene_Disease,name='Gene_Disease'),
    url(r'Gene_Pathway/',Gene_Pathway,name='Gene_Pathway')
]