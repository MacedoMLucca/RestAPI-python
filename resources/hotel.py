from flask_restful import Resource


hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'alpha Hotel',
        'estrela': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
        {
        'hotel_id': 'bravo',
        'nome': 'bravo Hotel',
        'estrela': 4.4,
        'diaria': 320.14,
        'cidade': 'Santa Catarina'
    },
        {
        'hotel_id': 'charlie',
        'nome': 'charlie Hotel',
        'estrela': 4.3,
        'diaria': 210.20,
        'cidade': 'Santa Catarina'
    }
]


class Hoteis(Resource):
    def get(self):
        return{'hoteis': hoteis}
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message':'Hotel not found.'}, 404
    
    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
