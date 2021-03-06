from App.ext import db
# 报错解决方法https://blog.csdn.net/w18306890492/article/details/83865204


class AllData(db.Model):
    dbid = db.Column(db.INTEGER, primary_key=True)
    DBDSMID = db.Column(db.String(100))
    Disease = db.Column(db.String(100))
    DOID = db.Column(db.String(100))
    Gene = db.Column(db.String(100))
    GeneID = db.Column(db.String(100))
    MIM = db.Column(db.String(100))
    Map_Location = db.Column(db.String(100))
    VariantType = db.Column(db.String(100))
    Protein = db.Column(db.String(100))
    cDNA = db.Column(db.String(100))
    SNPID = db.Column(db.String(100))
    CodonChange = db.Column(db.String(100))
    RefseqTranscript = db.Column(db.String(255))
    P_Value = db.Column(db.String(100))
    Strand = db.Column(db.String(100))
    GRCh38_Position = db.Column(db.String(100))
    GRCh37_Position = db.Column(db.String(100))
    Ref = db.Column(db.String(100))
    Alt = db.Column(db.String(100))
    Year = db.Column(db.String(100))
    PMID = db.Column(db.String(100))
    Ethnicity = db.Column(db.String(100))
    Classification = db.Column(db.String(100))
    StrengthOfEvidence =db.Column(db.String(255))
    KeySentence = db.Column(db.Text())
    Source = db.Column(db.String(100))
    Score = db.Column(db.String(100))
    Vote = db.Column(db.String(100))
    PrDSM = db.Column(db.String(100))
    TraP = db.Column(db.String(100))
    SilVA = db.Column(db.String(100))
    PhD_SNPg = db.Column(db.String(100))
    FATHMM_MKL = db.Column(db.String(100))
    CADD = db.Column(db.String(100))
    DANN = db.Column(db.String(100))
    FATHMM_XF = db.Column(db.String(100))
    priPhCons = db.Column(db.String(100))
    mamPhCons = db.Column(db.String(100))
    verPhCons = db.Column(db.String(100))
    priPhyloP = db.Column(db.String(100))
    mamPhyloP = db.Column(db.String(100))
    verPhyloP = db.Column(db.String(100))
    GerpS = db.Column(db.String(100))
    TFBs = db.Column(db.String(100))
    TE = db.Column(db.String(100))
    dPSIZ = db.Column(db.String(100))
    DSP = db.Column(db.String(100))

    RSCU = db.Column(db.String(100))
    dRSCU = db.Column(db.String(100))
    CpG_mark = db.Column(db.String(100))
    CpG_exon = db.Column(db.String(100))
    SR_minus = db.Column(db.String(100))
    SR_plus = db.Column(db.String(100))
    FAS6_minus = db.Column(db.String(100))
    FAS6_plus = db.Column(db.String(100))
    MES = db.Column(db.String(100))
    dMES = db.Column(db.String(100))
    MES_plus = db.Column(db.String(100))
    MES_minus = db.Column(db.String(100))
    MEC_MC_mark = db.Column(db.String(100))
    MEC_CS_mark = db.Column(db.String(100))
    MES_KM_mark = db.Column(db.String(100))
    PESE_minus = db.Column(db.String(100))
    PESE_plus = db.Column(db.String(100))
    PESS_minus = db.Column(db.String(100))
    PESS_plus = db.Column(db.String(100))
    f_premrna = db.Column(db.String(100))
    f_mrna = db.Column(db.String(100))

    Chromosome = db.Column(db.String(100))



class AllDataAnnotation(db.Model):
    dbid = db.Column(db.INTEGER, primary_key=True)
    DBDSMID = db.Column(db.String(100))
    Disease = db.Column(db.String(100))
    DOID = db.Column(db.String(100))
    Gene = db.Column(db.String(100))
    GeneID = db.Column(db.String(100))
    MIM = db.Column(db.String(100))
    Map_Location = db.Column(db.String(100))
    VariantType = db.Column(db.String(100))
    Protein = db.Column(db.String(100))
    cDNA = db.Column(db.String(100))
    SNPID = db.Column(db.String(100))
    CodonChange = db.Column(db.String(100))
    RefseqTranscript = db.Column(db.String(255))
    P_Value = db.Column(db.String(100))
    Strand = db.Column(db.String(100))
    GRCh38_Position = db.Column(db.String(100))
    GRCh37_Position = db.Column(db.String(100))
    Ref = db.Column(db.String(100))
    Alt = db.Column(db.String(100))
    Year = db.Column(db.String(100))
    PMID = db.Column(db.String(100))
    Ethnicity = db.Column(db.String(100))
    Classification = db.Column(db.String(100))
    StrengthOfEvidence =db.Column(db.String(255))
    KeySentence = db.Column(db.Text())
    Source = db.Column(db.String(100))
    Score = db.Column(db.String(100))
    Vote = db.Column(db.String(100))
    PrDSM = db.Column(db.String(100))
    TraP = db.Column(db.String(100))
    SilVA = db.Column(db.String(100))
    PhD_SNPg = db.Column(db.String(100))
    FATHMM_MKL = db.Column(db.String(100))
    CADD = db.Column(db.String(100))
    DANN = db.Column(db.String(100))
    FATHMM_XF = db.Column(db.String(100))
    priPhCons = db.Column(db.String(100))
    mamPhCons = db.Column(db.String(100))
    verPhCons = db.Column(db.String(100))
    priPhyloP = db.Column(db.String(100))
    mamPhyloP = db.Column(db.String(100))
    verPhyloP = db.Column(db.String(100))
    GerpS = db.Column(db.String(100))
    TFBs = db.Column(db.String(100))
    TE = db.Column(db.String(100))
    dPSIZ = db.Column(db.String(100))
    DSP = db.Column(db.String(100))

    RSCU = db.Column(db.String(100))
    dRSCU = db.Column(db.String(100))
    CpG_mark = db.Column(db.String(100))
    CpG_exon = db.Column(db.String(100))
    SR_minus = db.Column(db.String(100))
    SR_plus = db.Column(db.String(100))
    FAS6_minus = db.Column(db.String(100))
    FAS6_plus = db.Column(db.String(100))
    MES = db.Column(db.String(100))
    dMES = db.Column(db.String(100))
    MES_plus = db.Column(db.String(100))
    MES_minus = db.Column(db.String(100))
    MEC_MC_mark = db.Column(db.String(100))
    MEC_CS_mark = db.Column(db.String(100))
    MES_KM_mark = db.Column(db.String(100))
    PESE_minus = db.Column(db.String(100))
    PESE_plus = db.Column(db.String(100))
    PESS_minus = db.Column(db.String(100))
    PESS_plus = db.Column(db.String(100))
    f_premrna = db.Column(db.String(100))
    f_mrna = db.Column(db.String(100))

    Chromosome = db.Column(db.String(100))


class Tbsubmit(db.Model):
    tbid = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(200))
    joumal = db.Column(db.String(200))
    gene = db.Column(db.String(200))
    email = db.Column(db.String(200))
    mutation = db.Column(db.String(200))
    more = db.Column(db.String(500))



