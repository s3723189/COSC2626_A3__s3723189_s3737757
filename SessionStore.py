import redis

class Session_store:

    def __init__(self, token, url='redis://localhost:6379', ttl=10):
        self.token = token
        self.redis = redis.Redis.from_url(url)
        self.ttl = ttl

    def log_in_user(self):
        return self.redis.hset(self.token, "logged_in", "true")

    def check_user_log_in(self):
        return self.redis.hget(self.token, "logged_in")


    def log_out_user(self):
        return self.redis.hset(self.token, "logged_in", "false")
    

    