import uuid
import os
import numpy
import pandas
from .models import db, AllData
from sqlalchemy import or_, and_,text
from pathlib import Path

def sQLAlchemyToCsv(result):
    outList = []
    for dataObj in result:
        outList.append([dataObj.DBDSMID, dataObj.Disease, dataObj.DOID, dataObj.Gene, dataObj.GeneID, dataObj.MIM
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
                           , dataObj.PrDSM
                           , dataObj.TraP
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
                           , dataObj.Source
                        ])
    df = pandas.DataFrame(outList)
    df.columns = ['dbDSMAccNum','Disease','DOID','Gene','GeneID','MIM','Map_Location','VariantType','Protein','cDNA','SNPID','CodonChange','RefseqTranscript','P_Value','Strand','GRCh38_Position','GRCh37_Position','Ref','Alt','Year','PMID','Ethnicity','Classification','StrengthOfEvidenc','KeySentence','PrDSM','TraP','PhD_SNPg','FATHMM_MKL','CADD','DANN','FATHMM_XF','priPhCons','mamPhCons','verPhCons','priPhyloP','mamPhyloP','verPhyloP','GerpS','TFBs','TE','dPSIZ','DSP','Source']
    return df





def showTable(indata, page, limit):
    '''
    为普通搜索进行sql查询，分页
    :param indata: searchBy，和userinput
    :param page: 当前页
    :param limit: 每页个数
    :return: 返回查询分页结果
    '''
    searchBy = indata[0]
    userinput = indata[1]
    if searchBy == 'Disease':
        paginate = AllData.query.filter(AllData.Disease.like('%' + userinput + '%')).paginate(page, limit, False)
    elif searchBy == 'Gene':
        paginate = AllData.query.filter(AllData.Gene.like('%' + userinput + '%')).paginate(page, limit, False)
    elif searchBy == 'GRCh38_Position':
        paginate = AllData.query.filter(AllData.GRCh38_Position.like('%' + userinput + '%')).paginate(page, limit,
                                                                                                      False)
    elif searchBy == 'Mutation':
        paginate = AllData.query.filter(or_(AllData.Protein.like('%' + userinput + '%'),
                                            AllData.cDNA.like('%' + userinput + '%'),
                                            AllData.SNPID.like('%' + userinput + '%'))).paginate(page, limit, False)
    else:
        paginate = []
    return paginate


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












