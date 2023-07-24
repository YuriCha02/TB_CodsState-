from flask import Blueprint, render_template #,url_for
# from werkzeug.utils import redirect

# with open('../../model','multi') as pickle_file:
#    model = pickle.load(pickle_file)

bp = Blueprint('multi', __name__, url_prefix='/')

@bp.route('/multi/')
def multi_main():
    return render_template('main/multi.html')

@bp.route('/multi/result', methods=['POST'])
def multi_result():
    
    result = None # = model 예측 결과
    
    return render_template('result/multi_result.html', result = result), # result를 html로 보냅니다.