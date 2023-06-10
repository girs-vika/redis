import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

print(redis_client.set(name="test_key1", value=11))
print(redis_client.get("test_key"))


redis_client.close()