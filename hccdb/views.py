from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from hccdb.models import *


def index(request):

    return render(request,'index.html',)

def gene(request,gene_number):
    name = Gene.objects.filter(Number=gene_number)[0].Name
    gene_list = Gene.objects.filter(Number=gene_number)
    genedisease_list = GeneDisease.objects.filter(GeneName=gene_number)
    genepathway_list = GenePathway.objects.filter(GeneNumber=gene_number)
    genesequence_list = GeneSeq.objects.filter(GeneNumber=gene_number)
    return render(request,'Gene.html',{'name':name,
                                        'gene_list':gene_list,
                                       'genedisease_list':genedisease_list,
                                       'genepathway_list':genepathway_list,
                                       'genesequence_list':genesequence_list})

def genelist(request):
    gene_list = Gene.objects.all()
    page_num = int(request.GET.get('page',1))
    paginator = Paginator(gene_list,10)
    gene_list = paginator.page(page_num)
    return render(request,'GeneList.html',{'gene_list':gene_list})


# drug
def drug(request,drug_number):
    name = Drug.objects.filter(Number=drug_number)[0].Name
    drug_list = Drug.objects.filter(Number=drug_number)
    atc_list = DrugATC.objects.filter(DrugID=drug_number)  # 列表
    bankenzymes_list = DrugBankEnzymes.objects.filter(DrugID=drug_number)
    Indications_list = Indications.objects.filter(DrugID=drug_number)
    se_list = Se.objects.filter(DrugID=drug_number)
    targetpathway_list = DrugTargetPathway.objects.filter(DrugNumber=drug_number)
    targets_list = DrugBankTargets.objects.filter(DrugID=drug_number)
    MoA_list = DrugMoA.objects.filter(DrugID=drug_number)
    print(targets_list)
    return render(request,'Drug.html',{'name':name,
                                       'drug_list':drug_list,
                                       'atc_list':atc_list,
                                       'bankenzymes_list':bankenzymes_list,
                                       'Indications_list':Indications_list,
                                       'se_list':se_list,
                                       'targetpathway_list':targetpathway_list,
                                       'targets_list':targets_list,
                                       'MoA_list':MoA_list})

def druglist(request):
    drug_list = Drug.objects.all()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(drug_list, 10)
    drug_list = paginator.page(page_num)
    return render(request,'DrugList.html',{'drug_list':drug_list})

# literature
def literature(request):
    return render(request,'Literature.html')

def literaturelist(request):
    literature_list = Literature.objects.all()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(literature_list, 10)
    literature_list = paginator.page(page_num)
    return render(request,'LiteratureList.html',{'literature_list':literature_list})

#About
def About(request):
    return render(request,'About.html')

def Gene_Disease(request):
    return render(request,'Gene_Disease.html')

def Gene_Pathway(request):
    return render(request,'Gene_Pathway.html')

# pathway
def pathway(request):
    return render(request,'Pathway.html')

def pathwaylist(request):
    pathway_list = Pathway.objects.all()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(pathway_list, 10)
    pathway_list = paginator.page(page_num)
    return render(request,'PathwayList.html',{'pathway_list':pathway_list})

# patientSample
def patientSamplelist(request):
    geo_list = GEO.objects.all()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(geo_list, 10)
    geo_list = paginator.page(page_num)
    return render(request,'PatientSampleList.html',{'geo_list':geo_list})

def patientsample(request,patient_id):
    geo_list = GEO.objects.filter(ReferenceSeries=patient_id)
    geoplatforms_list = GEOPlatforms.objects.filter(SeriesID=patient_id)
    geosamples_list = GEOSamples.objects.filter(SerisesID=patient_id)
    return render(request,'PatientSample.html',{'geo_list':geo_list,
                                                'geoplatforms_list':geoplatforms_list,
                                                'geosamples_list':geosamples_list})

def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键字'
        return render(request,'Search_list.html',{'error_msg':error_msg})

    gene_list = Gene.objects.filter(Number__icontains=q)
    gene_list1 = Gene.objects.filter(Name__icontains=q)
    gene_list2 = Gene.objects.filter(OtherName__icontains=q)
    genedisease = GeneDisease.objects.filter(GeneName__icontains=q)
    genedisease1 = GeneDisease.objects.filter(DiseaseNumber__icontains=q)
    genedisease2 = GeneDisease.objects.filter(DiseaseName__icontains=q)
    genepathway = GenePathway.objects.filter(GeneNumber__icontains=q)
    genepathway1 = GenePathway.objects.filter(PathwayNumber__icontains=q)
    genepathway2 = GenePathway.objects.filter(PathwayName__icontains=q)
    genesequence = GeneSeq.objects.filter(GeneNumber__icontains=q)
    genesequence1 = GeneSeq.objects.filter(AAseq__icontains=q)
    genesequence2 = GeneSeq.objects.filter(NTseq__icontains=q)
    pathway = Pathway.objects.filter(Number__icontains=q)
    pathway1 = Pathway.objects.filter(Name__icontains=q)
    atc = DrugATC.objects.filter(DrugID__icontains=q)
    atc1 = DrugATC.objects.filter(ATCCode__icontains=q)
    bankenzymes = DrugBankEnzymes.objects.filter(DrugID__icontains=q)
    bankenzymes1 = DrugBankEnzymes.objects.filter(Name__icontains=q)
    bankenzymes2 = DrugBankEnzymes.objects.filter(GeneName__icontains=q)
    bankenzymes3 = DrugBankEnzymes.objects.filter(UniprotID__icontains=q)
    bankenzymes4 = DrugBankEnzymes.objects.filter(UniprotName__icontains=q)
    drug = Drug.objects.filter(Number__icontains=q)
    drug1 = Drug.objects.filter(Name__icontains=q)
    drug2 = Drug.objects.filter(Formula__icontains=q)
    indications = Indications.objects.filter(CID__icontains=q)
    indications1 = Indications.objects.filter(indications__icontains=q)
    indications2 = Indications.objects.filter(DrugID__icontains=q)
    se = Se.objects.filter(CID__icontains=q)
    se1 = Se.objects.filter(se__icontains=q)
    se2 = Se.objects.filter(DrugID__icontains=q)
    targetpathway = DrugTargetPathway.objects.filter(DrugNumber__icontains=q)
    targetpathway1 = DrugTargetPathway.objects.filter(PathwayNumber__icontains=q)
    targetpathway2= DrugTargetPathway.objects.filter(PathwayName__icontains=q)
    targets = DrugBankTargets.objects.filter(DrugID__icontains=q)
    targets1 = DrugBankTargets.objects.filter(Name__icontains=q)
    targets2 = DrugBankTargets.objects.filter(GeneName__icontains=q)
    targets3 = DrugBankTargets.objects.filter(UniprotID__icontains=q)
    targets4 = DrugBankTargets.objects.filter(UniprotName__icontains=q)
    moa = DrugMoA.objects.filter(DrugID__icontains=q)
    moa1 = DrugMoA.objects.filter(Categories__icontains=q)
    moa2 = DrugMoA.objects.filter(MoA__icontains=q)
    geo = GEO.objects.filter(ReferenceSeries__icontains=q)
    geoplatforms = GEOPlatforms.objects.filter(SeriesID__icontains=q)
    geoplatforms1 = GEOPlatforms.objects.filter(PlatformsID__icontains=q)
    geoplatforms2 = GEOPlatforms.objects.filter(Platforms__icontains=q)
    geosamples = GEOSamples.objects.filter(SerisesID__icontains=q)
    geosamples1 = GEOSamples.objects.filter(SamplesID__icontains=q)
    geosamples2 = GEOSamples.objects.filter(Samples__icontains=q)
    literature = Literature.objects.filter(name__icontains=q)

    return render(request,'Search_list.html',{'genedisease_list':genedisease,
                                              'genedisease_list1': genedisease1,
                                              'genedisease_list2': genedisease2,
                                       'genepathway_list':genepathway,
                                              'genepathway_list1': genepathway1,
                                              'genepathway_list2': genepathway2,
                                              'genesequence_list':genesequence,
                                              'genesequence_list1': genesequence1,
                                              'genesequence_list2': genesequence2,
                                              'gene_list':gene_list,
                                              'gene_list1': gene_list1,
                                              'gene_list2': gene_list2,
                                              'atc_list': atc,
                                              'atc_list1': atc1,
                                              'bankenzymes_list': bankenzymes,
                                              'bankenzymes_list1': bankenzymes1,
                                              'bankenzymes_list2': bankenzymes2,
                                              'bankenzymes_list3': bankenzymes3,
                                              'bankenzymes_list4': bankenzymes4,
                                              'Indications_list': indications,
                                              'Indications_list1': indications1,
                                              'Indications_list2': indications2,
                                              'se_list': se,
                                              'se_list1': se1,
                                              'se_list2': se2,
                                              'targetpathway_list': targetpathway,
                                              'targetpathway_list1': targetpathway1,
                                              'targetpathway_list2': targetpathway2,
                                              'targets_list': targets,
                                              'targets_list1': targets1,
                                              'targets_list2': targets2,
                                              'targets_list3': targets3,
                                              'targets_list4': targets4,
                                              'drug_list': drug,
                                              'drug_list1': drug1,
                                              'drug_list2': drug2,
                                              'MoA_list':moa,
                                              'MoA_list1':moa1,
                                              'MoA_list2':moa2,
                                              'pathway_list': pathway,
                                              'pathway_list1': pathway1,
                                              'geo_list': geo,
                                              'geoplatforms_list': geoplatforms,
                                              'geoplatforms_list1': geoplatforms1,
                                              'geoplatforms_list2': geoplatforms2,
                                              'geosamples_list': geosamples,
                                              'geosamples_list1': geosamples1,
                                              'geosamples_list2': geosamples2,
                                              'literature_list':literature,
                                              'error_msg':error_msg,
                                              })
