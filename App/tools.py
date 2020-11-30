import uuid
import os
import numpy
import pandas
from .models import db, AllData,AllDataAnnotation
from sqlalchemy import or_, and_,text
from pathlib import Path


def sQLAlchemyToCsv(result):
    outList = []
    for dataObj in result:
        outList.append([dataObj.DBDSMID
                           , dataObj.Disease
                           , dataObj.DOID
                           , dataObj.Gene
                           , dataObj.GeneID
                           , dataObj.MIM
                           , dataObj.Map_Location
                           , dataObj.VariantType
                           , dataObj.Protein
                           , dataObj.cDNA
                           , dataObj.SNPID
                           , dataObj.CodonChange
                           , dataObj.RefseqTranscript
                           , dataObj.P_Value
                           , dataObj.Strand
                           , dataObj.GRCh38_Position
                           , dataObj.GRCh37_Position
                           , dataObj.Ref
                           , dataObj.Alt
                           , dataObj.Year
                           , dataObj.PMID
                           , dataObj.Ethnicity
                           , dataObj.Classification
                           , dataObj.StrengthOfEvidence
                           , dataObj.KeySentence
                           , dataObj.Source
                           , dataObj.Score
                           , dataObj.Vote
                           , dataObj.PrDSM
                           , dataObj.TraP
                           , dataObj.SilVA
                           , dataObj.PhD_SNPg
                           , dataObj.FATHMM_MKL
                           , dataObj.CADD
                           , dataObj.DANN
                           , dataObj.FATHMM_XF
                           , dataObj.priPhCons
                           , dataObj.mamPhCons
                           , dataObj.verPhCons
                           , dataObj.priPhyloP
                           , dataObj.mamPhyloP
                           , dataObj.verPhyloP
                           , dataObj.GerpS
                           , dataObj.TFBs
                           , dataObj.TE
                           , dataObj.dPSIZ
                           , dataObj.DSP
                           , dataObj.RSCU
                           , dataObj.dRSCU
                           , dataObj.CpG_mark
                           , dataObj.CpG_exon
                           , dataObj.SR_minus
                           , dataObj.SR_plus
                           , dataObj.FAS6_minus
                           , dataObj.FAS6_plus
                           , dataObj.MES
                           , dataObj.dMES
                           , dataObj.MES_plus
                           , dataObj.MES_minus
                           , dataObj.MEC_MC_mark
                           , dataObj.MEC_CS_mark
                           , dataObj.MES_KM_mark
                           , dataObj.PESE_minus
                           , dataObj.PESE_plus
                           , dataObj.PESS_minus
                           , dataObj.PESS_plus
                           , dataObj.f_premrna
                           , dataObj.f_mrna
                        ])
    df = pandas.DataFrame(outList)
    df.columns = 'dbDSM Number	Disease	DOID	Gene	GeneID	MIM	Map Location	Variant Type	Protein	cDNA	SNPID	Codon Change	Refseq Transcript 	P-value	Strand	GRCh38 Position	GRCh37 Position	Ref	Alt	Year	PMID	Ethnicity	Classification	Strength of Evidence	Key Sentence	Source	Score	Vote	PrDSM	TraP	SilVA	PhD-SNPg	FATHMM-MKL	CADD	DANN	FATHMM-XF	priPhCons	mamPhCons	verPhCons	priPhyloP	mamPhyloP	verPhyloP	GerpS	TFBs	TE	dPSIZ	DSP	RSCU	dRSCU	CpG?	CpG_exon	SR-	SR+	FAS6-	FAS6+	MES	dMES	MES+	MES-	MEC-MC?	MEC-CS?	MES-KM?	PESE-	PESE+	PESS-	PESS+	f_premrna	f_mrna'.split(
        '\t')
    return df





def showTable(indata, page, limit, flag='AllData'):
    '''
    为普通搜索进行sql查询，分页
    :param indata: searchBy，和userinput
    :param page: 当前页
    :param limit: 每页个数
    :return: 返回查询分页结果
    '''
    if flag == 'AllData':
        flag = 'AllData'
    else:
        flag = 'AllDataAnnotation'
    searchBy = indata[0]
    userinput = indata[1]
    if searchBy == 'Disease':
        paginate = eval(flag).query.filter(eval(flag).Disease.like('%' + userinput + '%')).paginate(page, limit, False)
    elif searchBy == 'Gene':
        paginate = eval(flag).query.filter(eval(flag).Gene.like('%' + userinput + '%')).paginate(page, limit, False)
    elif searchBy == 'GRCh38_Position':
        paginate = eval(flag).query.filter(eval(flag).GRCh38_Position.like('%' + userinput + '%')).paginate(page, limit,
                                                                                                      False)
    elif searchBy == 'Mutation':
        paginate = eval(flag).query.filter(or_(eval(flag).Protein.like('%' + userinput + '%'),
                                            eval(flag).cDNA.like('%' + userinput + '%'),
                                            eval(flag).SNPID.like('%' + userinput + '%'))).paginate(page, limit, False)
    else:
        paginate = []
    return paginate

def showAnnotationTable(indata, page, limit):
    '''
    为普通搜索进行sql查询，分页
    :param indata: searchBy，和userinput
    :param page: 当前页
    :param limit: 每页个数
    :return: 返回查询分页结果
    '''
    searchBy = indata[0]
    userinput = indata[1]
    if searchBy == 'Gene':
        paginate = AllDataAnnotation.query.filter(AllDataAnnotation.Gene.like('%' + userinput + '%')).paginate(page, limit, False)
    elif searchBy == 'GRCh38_Position':
        paginate = AllDataAnnotation.query.filter(AllDataAnnotation.GRCh38_Position.like('%' + userinput + '%')).paginate(page, limit, False)
    elif searchBy == 'Mutation':
        paginate = AllDataAnnotation.query.filter(or_(AllDataAnnotation.Protein.like('%' + userinput + '%'),
                                            AllDataAnnotation.cDNA.like('%' + userinput + '%'),
                                            AllDataAnnotation.SNPID.like('%' + userinput + '%'))).paginate(page, limit, False)
    else:
        paginate = []
    return paginate


def downAnnotationShowTable(indata):
    '''
    为普通搜索下载进行sql查询
    :param indata: searchBy，和userinput
    :param page: 当前页
    :param limit: 每页个数
    :return: 返回查询分页结果
    '''
    searchBy = indata[0]
    userinput = indata[1]
    if searchBy == 'Gene':
        searchresult = AllDataAnnotation.query.filter(AllDataAnnotation.Gene.like('%' + userinput + '%')).all()
    elif searchBy == 'GRCh38_Position':
        searchresult = AllDataAnnotation.query.filter(AllDataAnnotation.GRCh38_Position.like('%' + userinput + '%')).all()
    elif searchBy == 'Mutation':
        searchresult = AllDataAnnotation.query.filter(or_(AllDataAnnotation.Protein.like('%' + userinput + '%'),
                                            AllDataAnnotation.cDNA.like('%' + userinput + '%'),
                                            AllDataAnnotation.SNPID.like('%' + userinput + '%'))).all()
    else:
        searchresult = []
    return searchresult


def downShowTable(indata):
    '''
    为普通搜索下载进行sql查询
    :param indata: searchBy，和userinput
    :param page: 当前页
    :param limit: 每页个数
    :return: 返回查询分页结果
    '''
    searchBy = indata[0]
    userinput = indata[1]
    if searchBy == 'Disease':
        searchresult = AllData.query.filter(AllData.Disease.like('%' + userinput + '%')).all()
    elif searchBy == 'Gene':
        searchresult = AllData.query.filter(AllData.Gene.like('%' + userinput + '%')).all()
    elif searchBy == 'GRCh38_Position':
        searchresult = AllData.query.filter(AllData.GRCh38_Position.like('%' + userinput + '%')).all()
    elif searchBy == 'Mutation':
        searchresult = AllData.query.filter(or_(AllData.Protein.like('%' + userinput + '%'),
                                            AllData.cDNA.like('%' + userinput + '%'),
                                            AllData.SNPID.like('%' + userinput + '%'))).all()
    else:
        searchresult = []
    return searchresult


def downShowAdvancedTable(dict):
    '''
    高级搜索，sql查询,下载
    :param dict:
    :param page:
    :param limit:
    :return:
    '''
    Disease = dict['Disease']
    Gene = dict['Gene']
    Chromosome = dict['Chromosome']
    Classification = dict['Classification']
    StrengthOfEvidence = dict['StrengthOfEvidence']

    if (Chromosome != "" or Chromosome != None) and (Gene == "" or Gene == None) and (
            Disease == "" or Disease == None) and (Classification == "" or Classification == None) and (
            StrengthOfEvidence == "" or StrengthOfEvidence == None):
        return AllData.query.filter_by(Chromosome="" if (Chromosome == "" or Chromosome == None) else Chromosome). \
            filter(AllData.Gene.like('%' + "" if (Gene == "" or Gene == None) else Gene + '%'),
                   AllData.Disease.like('%' + "" if (Disease == "" or Disease == None) else Disease + '%'),
                   AllData.Classification.like('%' + "" if (Classification == "" or Classification == None) else Classification + '%'),
                   AllData.StrengthOfEvidence.like('%' + "" if (StrengthOfEvidence == "" or StrengthOfEvidence == None) else StrengthOfEvidence + '%'))
    else:
        return AllData.query. \
            filter(AllData.Gene.like('%' + "" if (Gene == "" or Gene == None) else Gene + '%'),
                   AllData.Disease.like('%' + "" if (Disease == "" or Disease == None) else Disease + '%'),
                   AllData.Classification.like('%' + "" if (Classification == "" or Classification == None) else Classification + '%'),
                   AllData.StrengthOfEvidence.like('%' + "" if (StrengthOfEvidence == "" or StrengthOfEvidence == None) else StrengthOfEvidence + '%'))

def downAnnotationShowAdvancedTable(dict):
    '''
    高级搜索，sql查询,下载
    :param dict:
    :param page:
    :param limit:
    :return:
    '''
    Chromosome = dict['Chromosome']
    Vote = dict['Vote']

    if (Chromosome != "" or Chromosome != None) and (Vote == "" or Vote == None):
        return AllDataAnnotation.query.filter_by(Chromosome="" if (Chromosome == "" or Chromosome == None) else Chromosome). \
            filter(AllDataAnnotation.Vote.like('%' + "" if (Vote == "" or Vote == None) else Vote + '%'))
    else:
        return AllDataAnnotation.query. \
            filter(AllDataAnnotation.Vote.like('%' + "" if (Vote == "" or Vote == None) else Vote + '%'))



def showAdvancedTable(dict, page, limit):
    '''
    高级搜索，sql查询,分页
    :param dict:
    :param page:
    :param limit:
    :return:
    '''
    Disease = dict['Disease']
    Gene = dict['Gene']
    Chromosome = dict['Chromosome']
    Classification = dict['Classification']
    StrengthOfEvidence = dict['StrengthOfEvidence']
    if (Chromosome != "" or Chromosome != None) and (Gene == "" or Gene == None) and (
            Disease == "" or Disease == None) and (Classification == "" or Classification == None) and (
            StrengthOfEvidence == "" or StrengthOfEvidence == None):
        return AllData.query.filter_by(Chromosome="" if (Chromosome == "" or Chromosome == None) else Chromosome). \
            filter(AllData.Gene.like('%' + "" if (Gene == "" or Gene == None) else Gene + '%'),
                   AllData.Disease.like('%' + "" if (Disease == "" or Disease == None) else Disease + '%'),
                   AllData.Classification.like('%' + "" if (Classification == "" or Classification == None) else Classification + '%'),
                   AllData.StrengthOfEvidence.like('%' + "" if (StrengthOfEvidence == "" or StrengthOfEvidence == None) else StrengthOfEvidence + '%')).paginate(
            page, limit, False)
    else:
        return AllData.query. \
            filter(AllData.Gene.like('%' + "" if (Gene == "" or Gene == None) else Gene + '%'),
                   AllData.Disease.like('%' + "" if (Disease == "" or Disease == None) else Disease + '%'),
                   AllData.Classification.like('%' + "" if (Classification == "" or Classification == None) else Classification + '%'),
                   AllData.StrengthOfEvidence.like('%' + "" if (StrengthOfEvidence == "" or StrengthOfEvidence == None) else StrengthOfEvidence + '%')).paginate(
            page, limit, False)


def showAnnotationAdvancedTable(dict, page, limit):
    '''
    高级搜索，sql查询,分页
    :param dict:
    :param page:
    :param limit:
    :return:
    '''
    Chromosome = dict['Chromosome']
    Vote = dict['Vote']
    if (Chromosome != "" or Chromosome != None) and (Vote == "" or Vote == None):
        return AllDataAnnotation.query.filter_by(Chromosome="" if (Chromosome == "" or Chromosome == None) else Chromosome). \
            filter(AllDataAnnotation.Vote.like('%' + "" if (Vote == "" or Vote == None) else Vote + '%')).paginate(
            page, limit, False)
    else:
        return AllDataAnnotation.query. \
            filter(AllDataAnnotation.Vote.like('%' + "" if (Vote == "" or Vote == None) else Vote + '%')).paginate(page, limit, False)


def result_to_dictAnnotation(result, flags):
    '''
    把sql结果转换为对应的字典，方便json传输
    {unique去重，并且拦截nan}
    :param result:
    :param flags:
    :return:
    '''
    import numpy as np
    # print(flags)
    dict = {
        'Chromosome': []
        , 'Vote': []

    }
    result = np.array(list(result))
    i = 0
    for flagkey in flags.keys():
        if flags[flagkey] == 1:
            continue
        dict[flagkey] = [incom for incom in np.unique(result[:, i + 2]) if str(incom) != 'n/a' and str(incom) != 'Other']#unique去重，并且拦截nan   list(np.unique(result[:, i + 2]))#
        i += 1

    for key in list(dict.keys()):
        if len(dict[key]) == 0:
            dict.pop(key)
    print(dict)
    return dict


def result_to_dict(result, flags):
    '''
    把sql结果转换为对应的字典，方便json传输
    {unique去重，并且拦截nan}
    :param result:
    :param flags:
    :return:
    '''
    import numpy as np
    # print(flags)
    dict = {
        'Disease': []
        , 'Gene': []
        , 'Chromosome': []
        , 'Classification': []
        , 'StrengthOfEvidence': []
    }
    result = np.array(list(result))
    i = 0
    for flagkey in flags.keys():
        if flags[flagkey] == 1:
            continue
        dict[flagkey] = [incom for incom in np.unique(result[:, i + 2]) if str(incom) != 'n/a' and str(incom) != 'Other']#unique去重，并且拦截nan   list(np.unique(result[:, i + 2]))#
        i += 1

    for key in list(dict.keys()):
        if len(dict[key]) == 0:
            dict.pop(key)
    return dict



def changeHTML(input):
    '''
    html转义字符问题
    :param input: 弃用
    :return:
    '''
    return input.replace('&amp;','&').replace('&lt;','<').replace('&gt;','>').replace('&quto;','"').replace('&#39;','\'')





def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename












