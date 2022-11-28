import secrets
from flask import Flask
from flask import jsonify, make_response, request, session
from flask_httpauth import HTTPBasicAuth
from logger import trace, exc
from project_app.views import BITTREX_V3 as bv3

app = Flask(__name__)
auth = HTTPBasicAuth()
app.secret_key = 'tIZs2IzxoCTCd0_SkJK4fz7gRNQ'.encode('utf-8')


@auth.verify_password
def authenticate(username, password):
    try:
        if username and password:
            auth_user, auth_pass = bv3.read_auth_details()
            if username == auth_user and password == auth_pass:
                session['id'] = secrets.token_urlsafe(20)
                return True
            else:
                return False
        return False
    except Exception as e:
        exc.exception(f'Authentication error : {e}')
        return make_response(jsonify({'message': 'Internal server Issue:'}), 500)


@app.route('/')
@auth.login_required
def login():
    try:
        if session['id']:
            trace.info("Login success - Session id created")
            return jsonify({"Access token": session['id']})
        else:
            session['id'] = secrets.token_urlsafe(20)
            trace.info("Login success - Session id created")
            return jsonify({"Access token": session['id']})
    except Exception as e:
        exc.exception(f'Error while user login: {e}')
        return make_response(jsonify({'message': 'Internal server Issue:'}), 500)


@app.route('/v3/markets/all_summaries', methods=["GET", "POST"])
def all_summaries():
    try:
        if 'token' in request.args:
            token = request.args['token']
            if token == session['id']:
                res, make = bv3.collect_all_summaries(request)
                if make:
                    return make_response(jsonify(res), make)
                else:
                    return jsonify(res)
            else:
                return make_response(jsonify({'message': 'Unauthorized Access - invalid session ID'}), 401)
        else:
            return [{'message': 'Missing required parameter'}, 400]

    except Exception as e:
        exc.exception(f'Error while collecting the market summaries : {e}')
        return make_response(jsonify({'message': 'Internal server Issue:'}), 500)


# @project_app.route('v3/markets/<string:market_symbol>/summary', methods=["GET", "POST"])
@app.route('/v3/markets/individual_summary', methods=["GET", "POST"])
def individual_summary():
    try:
        if 'token' in request.args:
            token = request.args['token']
            if token == session['id']:
                res, make = bv3.collect_individual_summary(request)
                if make:
                    return make_response(jsonify(res), make)
                else:
                    return jsonify(res)
            else:
                return make_response(jsonify({'message': 'Unauthorized Access - invalid session ID'}), 401)
        else:
            return [{'message': 'Missing required parameter'}, 400]

    except Exception as e:
        exc.exception(f'Error while collecting the specific market summary : {e}')
        return make_response(jsonify({'message': 'Internal server Issue:'}), 500)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)