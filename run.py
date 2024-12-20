from src.main.rabbit_mq_configs.consumer import RabbitMQConsumer

if __name__ == "__main__":
    rabbit_mq_consumer = RabbitMQConsumer()
    rabbit_mq_consumer.start()
