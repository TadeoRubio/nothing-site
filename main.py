from flask import Flask, make_response, jsonify

# Create Flask App
app = Flask(__name__)

# Handles the root directory (index)
@app.route('/')
def root():
    return  make_response(jsonify({'error': 'Oops Nothing to see!'}), 204)

# Handles the HTTP CODE 404 (Not Found) as 204 (No Content)
@app.errorhandler(404)
def page_not_foud(error):
    return "Oops Nothing to see!", 204

# Add some headers to use cache and don't allow robots
@app.after_request
def add_header(r):
    r.headers['Cache-Control'] = 'public, max-age=60, s-maxage=60, must-revalidate'
    r.headers['X-Robots-Tag'] = 'none'
    return r

# As any code, run on localhost to test, on GCloud the gunicorn execute Flask
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)