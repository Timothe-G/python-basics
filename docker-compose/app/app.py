from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-container', port=6379, decode_responses=True)

@app.route('/')
def hello():
	redis.incr('hits')
	return ' - - - Cette page web a été vu {} fois - - -'.format(redis.get('hits'))

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
