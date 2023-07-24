from flask import Blueprint, render_template #,url_for
# from werkzeug.utils import redirect

# with open('../../model','regression') as pickle_file:
#    model = pickle.load(pickle_file)

bp = Blueprint('regression', __name__, url_prefix='/')

@bp.route('/regression/')
def regression_main():
    return render_template('main/regression.html')

@bp.route('/regression/result', methods=['POST'])
def regression_result():
    
    result = None # = model 예측 결과
    
    return render_template('result/regression_result.html', result = result), # result를 html로 보냅니다.