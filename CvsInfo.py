from flask_restful import Resource

CVSINFO = {
     'name': 'matteo',
    'surname': 'massai'
}

class CvsInfo(Resource):
    print("qui")
    def get(self):
        print("QUI")
        return CVSINFO
