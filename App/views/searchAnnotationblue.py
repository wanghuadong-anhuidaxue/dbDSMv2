from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .forms import SearchAnnotationForm
from App.models import db, AllDataAnnotation
from App.tools import changeHTML, result_to_dictAnnotation, showAnnotationAdvancedTable, showAnnotationTable  # 导入自制工具包


searchAnnotationblue = Blueprint("searchAnnotationblue", __name__)



@searchAnnotationblue.route('/dbDSMv2/searchannotation', methods=['GET', 'POST'])
def searchAnnotation():
    '''
    跳转到查询表单，wtf负责第一个search表单，第二个高级搜索使用原始的方式，因为wtf如何实现ajax实时更新我不会。
    :return:
    '''
    form = SearchAnnotationForm()
    form.searchBy.data = 'Gene'  # 默认选择，不然就是中文的请选择了
    return render_template("searchannotation.html", form=form)



@searchAnnotationblue.route('/dbDSMv2/searchAnnotationSubmit', methods=['GET', 'POST'])
def searchAnnotationSubmit():
    '''
    普通查询首次提交
    :return: 使用的是request.form调用
    '''
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    searchBy = request.form.get("searchBy")
    userinput = request.form.get("userinput")
    if searchBy == 'GRCh38 Position':
        searchBy = 'GRCh38_Position'
    userinput = changeHTML(userinput)
    paginate = showAnnotationTable((searchBy, userinput), page, per_page)
    return render_template('searchAnnotationresult.html', searchBy=searchBy, userinput=userinput, pagination=paginate,
                           search_result=searchBy + ' like:' + userinput)



@searchAnnotationblue.route('/dbDSMv2/searchAnnotationTable', methods=['GET', 'POST'])
def searchAnnotationTable():  # page, per_page, searchBy, userinput
    '''
    表单更新
    :return:使用的是request.args调用
    '''
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    searchBy = request.args.get("searchBy")
    userinput = request.args.get("userinput")
    # print(page,per_page,searchBy,userinput)
    paginate = showAnnotationTable((searchBy, userinput), page, per_page)
    return render_template('searchAnnotationresult.html', page=page, per_page=per_page, searchBy=searchBy, userinput=userinput,
                           pagination=paginate)


@searchAnnotationblue.route('/dbDSMv2/detailAnnotationScore', methods=['GET', 'POST'])
def detailAnnotationScore():
    dbid = request.args.get("dbid")
    result = AllDataAnnotation.query.filter_by(dbid=dbid).first()
    return render_template('details2.html', dbDSMData=result)



@searchAnnotationblue.route('/dbDSMv2/advancedAnnotationSearch', methods=['GET', 'POST'])
def advancedAnnotationSearch():
    Chromosome = request.args.get('Chromosome')
    Vote = request.args.get('Vote')
    flags = {'Chromosome': 1, 'Vote':1}  # 立标签
    sql = 'select dbid,DBDSMID' \
          + (",Chromosome" if (Chromosome == "" or Chromosome == None) else "") \
          + (",Vote" if (Vote == "" or Vote == None) else "") \
          + " from all_data_annotation where DBDSMID like '%'" \
          + ("" if (Chromosome == "" or Chromosome == None) else (' and Chromosome="%s"' % Chromosome))\
          + ("" if (Vote == "" or Vote == None) else (' and Vote="%s"' % Vote)) + ';'
    # print('sql__!!:', sql)
    result = db.session.execute(sql)

    if (Chromosome == "" or Chromosome == None):
        flags['Chromosome'] = 0
    if (Vote == "" or Vote == None):
        flags['Vote'] = 0


    payload = result_to_dictAnnotation(result, flags)  # 转为字典

    # print(payload)
    # print(flags)
    return jsonify(payload)



@searchAnnotationblue.route('/dbDSMv2/advancedAnnotationSearchTable', methods=['GET', 'POST'])
def advancedAnnotationSearchTable():
    '''
    表单更新
    :return:
    '''
    Chromosome = request.args.get('Chromosome')
    Vote = request.args.get('Vote')

    dict = {
        'Chromosome': Chromosome if Chromosome!='None' else None
        , 'Vote': Vote if Vote!='None' else None
    }
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    # print('dict',dict)
    paginate = showAnnotationAdvancedTable(dict, page, per_page)
    # print(page,per_page,dict)
    return render_template('searchAnnotationresult2.html', page=page, per_page=per_page, pagination=paginate, Chromosome=dict['Chromosome'], Vote=dict['Vote'])



# @searchAnnotationblue.route('/dbDSMv2/researchDisease', methods=['GET', 'POST'])
# def researchDisease():
#     Disease = request.args.get("Disease")
#     dict = {
#         'Disease': Disease
#         , 'Gene': ''
#         , 'Chromosome': ''
#         , 'Classification':''
#         , 'StrengthOfEvidence':''
#     }
#     page = request.args.get("page", 1, type=int)
#     per_page = request.args.get("per_page", 10, type=int)
#     paginate = showAnnotationAdvancedTable(dict, page, per_page)
#     return render_template('searchresult2.html', page=page, per_page=per_page, pagination=paginate, Disease=Disease,
#                            Gene='', Chromosome='',Classification='',StrengthOfEvidence='')



# @searchAnnotationblue.route('/dbDSMv2/researchGene', methods=['GET', 'POST'])
# def researchGene():
#     reGene = request.args.get("reGene")
#     dict = {
#         'Disease': ''
#         , 'Gene': reGene
#         , 'Chromosome': ''
#         , 'Classification': ''
#         , 'StrengthOfEvidence': ''
#     }
#     page = request.args.get("page", 1, type=int)
#     per_page = request.args.get("per_page", 10, type=int)
#     paginate = showAnnotationAdvancedTable(dict, page, per_page)
#     # print(paginate)
#     return render_template('searchresult2.html', page=page, per_page=per_page, pagination=paginate, Disease='',
#                            Gene=reGene, Chromosome='',Classification='',StrengthOfEvidence='')  # 不能写none，会导致查询and_查询无果



# @searchAnnotationblue.route('/dbDSMv2/resetPageLimit1', methods=['GET', 'POST'])
# def resetPageLimit1():
#     newlimit = int(request.args.get('newlimit'))
#     searchBy = request.args.get('searchBy')
#     userinput = request.args.get("userinput")
#     return redirect(url_for('searchblue.searchTable', page=1, per_page=newlimit, userinput=userinput, searchBy=searchBy))


# 下面这是数据库载入的代码
@searchAnnotationblue.route('/dbDSMv2/addallAnn')
def addAllSql():
    import pandas as pd
    data = pd.read_csv('/data1/WWW/flask_website/dbDSMv2/whole_genome_SYN_annotation-based.vcf', dtype=str, encoding='ISO-8859-1', sep='\t')
    for line in data.values:
        allDataInfo = AllDataAnnotation(
            DBDSMID=str(line[0]),
            Disease=str(line[1]),
            DOID='n/a' if str(line[2]) == 'nan' else str(line[2]),
            Gene='n/a' if str(line[3]) == 'nan' else str(line[3]),
            GeneID='n/a' if str(line[4]) == 'nan' else str(line[4]),
            MIM='n/a' if str(line[5]) == 'nan' else str(line[5]),
            Map_Location='n/a' if str(line[6]) == 'nan' else str(line[6]),
            VariantType='n/a' if str(line[7]) == 'nan' else str(line[7]),
            Protein='n/a' if str(line[8]) == 'nan' else str(line[8]),
            cDNA='n/a' if str(line[9]) == 'nan' else str(line[9]),
            SNPID='n/a' if str(line[10]) == 'nan' else str(line[10]),
            CodonChange='n/a' if str(line[11]) == 'nan' else str(line[11]),
            RefseqTranscript='n/a' if str(line[12]) == 'nan' else str(line[12]),
            P_Value='n/a' if str(line[13]) == 'nan' else str(line[13]),
            Strand='n/a' if str(line[14]) == 'nan' else str(line[14]),
            GRCh38_Position='n/a' if str(line[15]) == 'nan' else str(line[15]),
            GRCh37_Position='n/a' if str(line[16]) == 'nan' else str(line[16]),
            Ref='n/a' if str(line[17]) == 'nan' else str(line[17]),
            Alt='n/a' if str(line[18]) == 'nan' else str(line[18]),
            Year='n/a' if str(line[19]) == 'nan' else str(line[19]),
            PMID='n/a' if str(line[20]) == 'nan' else str(line[20]),
            Ethnicity='n/a' if str(line[21]) == 'nan' else str(line[21]),
            Classification='n/a' if str(line[22]) == 'nan' else str(line[22]),
            StrengthOfEvidence='n/a' if str(line[23]) == 'nan' else str(line[23]),
            KeySentence='n/a' if str(line[24]) == 'nan' else str(line[24]),

            Source='n/a' if str(line[25]) == 'nan' else str(line[25]),
            Score='n/a' if str(line[26]) == 'nan' else str(line[26]),
            Vote='n/a' if str(line[27]) == 'nan' else str(line[27]),

            PrDSM='n/a' if str(line[28]) == 'nan' else str(line[28]),
            TraP='n/a' if str(line[29]) == 'nan' else str(line[29]),
            SilVA='n/a' if str(line[30]) == 'nan' else str(line[30]),
            PhD_SNPg='n/a' if str(line[31]) == 'nan' else str(line[31]),
            FATHMM_MKL='n/a' if str(line[32]) == 'nan' else str(line[32]),
            CADD='n/a' if str(line[33]) == 'nan' else str(line[33]),
            DANN='n/a' if str(line[34]) == 'nan' else str(line[34]),
            FATHMM_XF='n/a' if str(line[35]) == 'nan' else str(line[35]),

            priPhCons='n/a' if str(line[36]) == 'nan' else str(line[36]),
            mamPhCons='n/a' if str(line[37]) == 'nan' else str(line[37]),
            verPhCons='n/a' if str(line[38]) == 'nan' else str(line[38]),
            priPhyloP='n/a' if str(line[39]) == 'nan' else str(line[39]),
            mamPhyloP='n/a' if str(line[40]) == 'nan' else str(line[40]),
            verPhyloP='n/a' if str(line[41]) == 'nan' else str(line[41]),
            GerpS='n/a' if str(line[42]) == 'nan' else str(line[42]),
            TFBs='n/a' if str(line[43]) == 'nan' else str(line[43]),
            TE='n/a' if str(line[44]) == 'nan' else str(line[44]),
            dPSIZ='n/a' if str(line[45]) == 'nan' else str(line[45]),
            DSP='n/a' if str(line[46]) == 'nan' else str(line[46]),

            RSCU='n/a' if str(line[47]) == 'nan' else str(line[47]),
            dRSCU='n/a' if str(line[48]) == 'nan' else str(line[48]),
            CpG_mark='n/a' if str(line[49]) == 'nan' else str(line[49]),
            CpG_exon='n/a' if str(line[50]) == 'nan' else str(line[50]),
            SR_minus='n/a' if str(line[51]) == 'nan' else str(line[51]),
            SR_plus='n/a' if str(line[52]) == 'nan' else str(line[52]),
            FAS6_minus='n/a' if str(line[53]) == 'nan' else str(line[53]),
            FAS6_plus='n/a' if str(line[54]) == 'nan' else str(line[54]),
            MES='n/a' if str(line[55]) == 'nan' else str(line[55]),
            dMES='n/a' if str(line[56]) == 'nan' else str(line[56]),
            MES_plus='n/a' if str(line[57]) == 'nan' else str(line[57]),
            MES_minus='n/a' if str(line[58]) == 'nan' else str(line[58]),
            MEC_MC_mark='n/a' if str(line[59]) == 'nan' else str(line[59]),
            MEC_CS_mark='n/a' if str(line[60]) == 'nan' else str(line[60]),
            MES_KM_mark='n/a' if str(line[61]) == 'nan' else str(line[61]),
            PESE_minus='n/a' if str(line[62]) == 'nan' else str(line[62]),
            PESE_plus='n/a' if str(line[63]) == 'nan' else str(line[63]),
            PESS_minus='n/a' if str(line[64]) == 'nan' else str(line[64]),
            PESS_plus='n/a' if str(line[65]) == 'nan' else str(line[65]),
            f_premrna='n/a' if str(line[66]) == 'nan' else str(line[66]),
            f_mrna='n/a' if str(line[67]) == 'nan' else str(line[67]),

            Chromosome='n/a' if str(line[15]) == 'nan' else str(line[15]).split(':')[0]
        )
        db.session.add(allDataInfo)
        # break
    db.session.commit()
    print('ok!')
    return render_template("index.html")
