from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
api = Api(app)

books = []

def validate_book_data(data):
    if not all(key in data for key in ['id', 'title', 'author']):
        raise BadRequest("Missing required field")
    if not isinstance(data['id'], int):
        raise BadRequest("Id must be an integer")
    if not isinstance(data['title'], str):
        raise BadRequest("Title must be a string")
    if not isinstance(data['author'], str):
        raise BadRequest("Author must be a string")

class Book(Resource):
    def get(self, id):
        for book in books:
            if book['id'] == id:
                return book, 200
        return {'error': 'book not found'}, 404

    def post(self, id):
        data = request.get_json()
        try:
            validate_book_data(data)
        except BadRequest as e:
            return {'error': str(e)}, 400
        for book in books:
            if book['id'] == id:
                return {'error': 'book with id already exists'}, 409
        book = {
            'id': id,
            'title': data['title'],
            'author': data['author']
        }
        books.append(book)
        return book, 201

    def put(self, id):
        data = request.get_json()
        try:
            validate_book_data(data)
        except BadRequest as e:
            return {'error': str(e)}, 400
        index = None
        for i, book in enumerate(books):
            if book['id'] == id:
                index = i
                break
        if index is not None:
            books[index] = {
                'id': id,
                'title': data['title'],
                'author': data['author']
            }
            return books[index], 200
        return {'error': 'book not found'}, 404

    def delete(self, id):
        index = None
        for i, book in enumerate(books):
            if book['id'] == id:
                index = i
                break
        if index is not None:
            books.pop(index)
            return '', 204
        return {'error': 'book not found'}, 404

api.add_resource(Book, '/book/<int:id>')

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)