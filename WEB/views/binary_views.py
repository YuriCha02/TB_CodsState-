from flask import Blueprint, render_template #,url_for
# from werkzeug.utils import redirect

# with open('../../model','binary') as pickle_file:
#    model = pickle.load(pickle_file)

bp = Blueprint('binary', __name__, url_prefix='/')

@bp.route('/binary/')
def binary_main():
    return render_template('main/binary.html')

@bp.route('/binary/result', methods=['POST'])
def binary_result():
    
    result = None # = model 예측 결과
    
    return render_template('result/binary_result.html', result = result), # result를 html로 보냅니다.