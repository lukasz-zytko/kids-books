from flask import Flask, request, render_template, redirect, url_for, jsonify, abort, make_response

from forms import BooksForm
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "ksiazkizosi123"

@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = BooksForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
            books.save_all()
        return redirect(url_for("books_list"))

    return render_template("books.html", form=form, books=books.all(), error=error, count=books.count())


@app.route("/books/<int:book_id>", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id - 1)
    form = BooksForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, book_id=book_id)

@app.route("/api/v1/books/", methods=["GET"])
def books_list_api_v1():
    return jsonify(books.all())

@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    if book_id < 1 or book_id > books.count():
        abort(404)
    book = books.get(book_id-1)
    return jsonify({"book": book})

#errorhandlers
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


if __name__ == "__main__":
    app.run(debug=True)