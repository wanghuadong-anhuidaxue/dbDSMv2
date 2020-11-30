from flask import Blueprint, render_template, request, redirect, url_for, jsonify,current_app, send_from_directory

from App.tools import downShowTable, sQLAlchemyToCsv, random_filename, downShowAdvancedTable, Path, downAnnotationShowTable, downAnnotationShowAdvancedTable


downblue = Blueprint("downblue", __name__)





@downblue.route('/downAllTable')
@downblue.route('/dbDSMv2/downAllTable')
def downAllTable():
    userinput = request.args.get("userinput")
    searchBy = request.args.get("searchBy")
    result = downShowTable([searchBy, userinput])
    filename = random_filename('')+'.csv'
    sQLAlchemyToCsv(result).to_csv(Path(current_app.config['DOWNTABLE_PATH']).joinpath(filename), index=False)
    return send_from_directory(Path(current_app.config['DOWNTABLE_PATH']),filename=filename,as_attachment=True)#redirect(url_for('/dbDSMv2/'+filename))


@downblue.route('/dbDSMv2/downAnnotationAllTable')
def downAnnotationAllTable():
    userinput = request.args.get("userinput")
    searchBy = request.args.get("searchBy")
    result = downAnnotationShowTable([searchBy, userinput])
    filename = random_filename('')+'.csv'
    sQLAlchemyToCsv(result).to_csv(Path(current_app.config['DOWNTABLE_PATH']).joinpath(filename), index=False)
    return send_from_directory(Path(current_app.config['DOWNTABLE_PATH']),filename=filename,as_attachment=True)#redirect(url_for('/dbDSMv2/'+filename))



@downblue.route('/downAllTable2')
@downblue.route('/dbDSMv2/downAllTable2')
def downAllTable2():
    dict = {
        'Disease': request.args.get('Disease') if request.args.get('Disease')!='None' else None
        , 'Gene': request.args.get('Gene') if request.args.get('Gene')!='None' else None
        , 'Chromosome': request.args.get('Chromosome') if request.args.get('Chromosome')!='None' else None
        , 'Classification': request.args.get('Classification') if request.args.get('Classification')!='None' else None
        , 'StrengthOfEvidence': request.args.get('StrengthOfEvidence') if request.args.get('StrengthOfEvidence')!='None' else None
    }
    result = downShowAdvancedTable(dict)
    filename = random_filename('')+'.csv'
    sQLAlchemyToCsv(result).to_csv(Path(current_app.config['DOWNTABLE_PATH']).joinpath(filename), index=False)
    return send_from_directory(Path(current_app.config['DOWNTABLE_PATH']),filename=filename,as_attachment=True)#redirect(url_for('/dbDSMv2/'+filename))



@downblue.route('/dbDSMv2/downAnnotationAllTable2')
def downAnnotationAllTable2():
    dict = {
        'Chromosome': request.args.get('Chromosome') if request.args.get('Chromosome') != 'None' else None
        , 'Vote': request.args.get('Vote') if request.args.get('Vote') != 'None' else None
    }
    result = downAnnotationShowAdvancedTable(dict)
    filename = random_filename('')+'.csv'
    sQLAlchemyToCsv(result).to_csv(Path(current_app.config['DOWNTABLE_PATH']).joinpath(filename), index=False)
    return send_from_directory(Path(current_app.config['DOWNTABLE_PATH']),filename=filename,as_attachment=True)#redirect(url_for('/dbDSMv2/'+filename))



@downblue.route('/downResult')
@downblue.route('/dbDSMv2/downResult')
def downResult():
    filename = request.args.get('filename')
    return send_from_directory(str(current_app.config['RESULT_PATH']),filename=filename,as_attachment=True)#redirect(url_for('/dbDSMv2/'+filename))
