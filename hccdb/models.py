from django.db import models

# Create your models here.

# Gene
class Gene(models.Model):
    Name = models.CharField(max_length=255,primary_key=True)
    Number = models.CharField(max_length=255)
    OtherName = models.CharField(max_length=255)

    class Meta:
        db_table = "gene"

class GeneDisease(models.Model):
    id = models.IntegerField(primary_key=True)
    GeneName = models.CharField(max_length=255)
    DiseaseNumber = models.CharField(max_length=255)
    DiseaseName = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        db_table = 'genedisease'

class GenePathway(models.Model):
    id = models.IntegerField(primary_key=True)
    GeneNumber = models.CharField(max_length=255)
    PathwayNumber = models.CharField(max_length=255)
    PathwayName = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        db_table = 'genepathway'

class GeneSeq(models.Model):
    GeneNumber = models.CharField(max_length=255,primary_key=True)
    AAseq = models.TextField()
    NTseq = models.TextField()

    class Meta:
        db_table = 'geneseq'

# Pathway
class Pathway(models.Model):
    Number = models.CharField(max_length=255,primary_key=True)
    Name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        db_table = 'pathway'

#Drug
class DrugATC(models.Model):
    DrugID = models.CharField(max_length=255,primary_key=True)
    ATCCode = models.CharField(max_length=255)

    class Meta:
        db_table ='drugatc'

class DrugBankEnzymes(models.Model):
    id = models.IntegerField(primary_key=True)
    DrugID = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    GeneName = models.CharField(max_length=255)
    UniprotID = models.CharField(max_length=255)
    UniprotName = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        db_table = 'drugbankenzymes'

class Drug(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Number = models.CharField(max_length=255)
    Formula = models.CharField(max_length=255)

    class Meta:
        db_table = 'drug'

class Indications(models.Model):
    id = models.IntegerField(primary_key=True)
    CID = models.CharField(max_length=255)
    indications = models.CharField(max_length=255)
    DrugID = models.CharField(max_length=255)

    class Meta:
        db_table = 'indications'

class Se(models.Model):
    id = models.IntegerField(primary_key=True)
    CID = models.CharField(max_length=255)
    se = models.CharField(max_length=255)
    DrugID = models.CharField(max_length=255)

    class Meta:
        db_table = 'se'

class DrugTargetPathway(models.Model):
    id = models.IntegerField(primary_key=True)
    DrugNumber = models.CharField(max_length=255)
    PathwayNumber = models.CharField(max_length=255)
    PathwayName = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        db_table = 'drugtargetpathway'

class DrugBankTargets(models.Model):
    id = models.IntegerField(primary_key=True)
    DrugID = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    GeneName = models.CharField(max_length=255)
    UniprotID = models.CharField(max_length=255)
    UniprotName = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        db_table = 'drugbanktargets'

class DrugMoA(models.Model):
    id = models.IntegerField(primary_key=True)
    DrugID = models.CharField(max_length=255)
    Categories = models.CharField(max_length=255)
    MoA = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'drugmoa'

#patienSample
class GEO(models.Model):
    id = models.IntegerField(primary_key=True)
    ReferenceSeries = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Organism = models.CharField(max_length=255)
    ExperimentType = models.CharField(max_length=255)
    Summary = models.CharField(max_length=255)
    OverallDesign = models.CharField(max_length=255)
    Contributor = models.CharField(max_length=255)
    Citation = models.CharField(max_length=255)
    SubmissionDate = models.CharField(max_length=255)
    LastUpdateDate = models.CharField(max_length=255)
    ContactName = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    OrganizationName = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    Lab = models.CharField(max_length=255)
    StreetAddress = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    StateProvince = models.CharField(max_length=255)
    ZIPPostalCode = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        db_table = 'geo'

class GEOPlatforms(models.Model):
    id = models.IntegerField(primary_key=True)
    SeriesID = models.CharField(max_length=255)
    PlatformsID = models.CharField(max_length=255)
    Platforms = models.CharField(max_length=255)

    class Meta:
        db_table = 'geoplatforms'

class GEOSamples(models.Model):
    id = models.IntegerField(primary_key=True)
    SerisesID = models.CharField(max_length=255)
    SamplesID = models.CharField(max_length=255)
    Samples = models.CharField(max_length=255)

    class Meta:
        db_table = 'geosamples'

# Literature
class Literature(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        db_table = 'literature'
