from flask import request, jsonify, Flask

import utils.web_scrapping as web_scrapping
import repositories.mongo as mongo

app = Flask(__name__)

@app.route('/api/v1/resources/synonym', methods=['GET'])
def api_id():
    if 'word' in request.args:
        word = str(request.args['word'])
        db_word = mongo.find(word)
        print(db_word)
        if db_word is None:
            res = web_scrapping.get_synonyms(word)
            if res is not None:
                mongo.add(res)
                result = res.__dict__
                result["_id"] = str(result["_id"])
                response = jsonify(result)
                response.headers.add('Access-Control-Allow-Origin', '*')
                return response
            else:
                response = jsonify("A palavra não foi encontrada. Por favor, cheque a soletração e tente novamente")
                response.headers.add('Access-Control-Allow-Origin', '*')
                return response
        else:
            db_word["_id"] = str(db_word['_id'])
            response = jsonify(db_word)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    else:
        response = jsonify("Error: No word field provided. Please specify an word.")
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/')
def home():
    return "Please insert a word"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8656)

