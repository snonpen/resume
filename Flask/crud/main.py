from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = []

class Book(Resource):
    def get(self, id):
        for book in books:
            if book['id'] == id:
                return book, 200
        return {'error': 'book not found'}, 404

    def post(self, id):
        book = {
            'id': id,
            'title': request.json['title'],
            'author': request.json['author']
        }
        books.append(book)
        return book, 201

    def put(self, id):
        for book in books:
            if book['id'] == id:
                book['title'] = request.json['title']
                book['author'] = request.json['author']
                return book, 200
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

if __name__ == '__main__':
    app.run(debug=True)
