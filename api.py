from flask import request, jsonify, Flask

import Utils.utils as utils
import Repository.mongo as mongo

app = Flask(__name__)

@app.route('/api/v1/resources/synonym', methods=['GET'])
def api_id():
    if 'word' in request.args:
        word = str(request.args['word'])
        db_word = mongo.find(word)
        print(db_word)
        if db_word is None:
            res = utils.get_synonyms(word)
            if res is not None:
                mongo.add(res)
                result = res.__dict__
                result["_id"] = str(result["_id"])
                return jsonify(result)
            else:
                return "Error: The word was not found. Please check the spelling"
        else:
            db_word["_id"] = str(db_word['_id'])
            return db_word
    else:
        return "Error: No word field provided. Please specify an word."

app.run()
