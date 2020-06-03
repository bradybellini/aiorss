from secret import redis_host, redis_pass, redis_port
# REDIS_URL = 'redis://10.138.236.140:6379/0'

# You can also specify the Redis DB to use
REDIS_HOST = redis_host
REDIS_PORT = redis_port
REDIS_DB = 0
REDIS_PASSWORD = redis_pass

# Queues to listen on
QUEUES = ['high', 'default', 'low']

# If you're using Sentry to collect your runtime exceptions, you can use this
# to configure RQ for it in a single step
# The 'sync+' prefix is required for raven: https://github.com/nvie/rq/issues/350#issuecomment-43592410
# SENTRY_DSN = 'sync+http://public:secret@example.com/1'

# If you want custom worker name
# NAME = 'worker-1024'