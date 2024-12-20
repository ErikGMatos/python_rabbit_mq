# RabbitMQ-Telegram Message Relay System

This project implements a message relay system using RabbitMQ as a message broker and Telegram as the message destination.

The system consists of a publisher that sends messages to a RabbitMQ exchange, a consumer that processes these messages, and a Telegram sender that forwards the messages to a specified Telegram chat.
This setup allows for decoupled, asynchronous communication between different parts of an application or between multiple applications.

The project demonstrates the integration of RabbitMQ for reliable message queuing and Telegram for instant messaging, showcasing a practical use case for distributed systems and real-time notifications.

## Repository Structure

```
.
├── publisher.py
├── run.py
├── sender.py
└── src
    ├── __init__.py
    ├── drivers
    │   ├── __init__.py
    │   └── telegram_sender.py
    └── main
        ├── __init__.py
        └── rabbit_mq_configs
            ├── __init__.py
            ├── callback.py
            └── consumer.py
```

- `publisher.py`: Defines the `RabbitMQPublisher` class for sending messages to RabbitMQ.
- `run.py`: Entry point of the application, initializes and starts the RabbitMQ consumer.
- `sender.py`: Standalone script for sending messages directly to Telegram.
- `src/drivers/telegram_sender.py`: Contains the function for sending messages to Telegram.
- `src/main/rabbit_mq_configs/callback.py`: Defines the callback function for processing RabbitMQ messages.
- `src/main/rabbit_mq_configs/consumer.py`: Implements the `RabbitMQConsumer` class for consuming messages from RabbitMQ.

## Usage Instructions

### Installation

1. Ensure you have Python 3.6 or later installed.
2. Install the required dependencies:

```bash
pip3 install -r requirements.txt  
```

### Configuration

1. RabbitMQ Configuration:
   - Update the RabbitMQ connection parameters in `publisher.py` and `src/main/rabbit_mq_configs/consumer.py` if needed.
   - Default values are:
     - Host: localhost
     - Port: 5672
     - Username: guest
     - Password: guest

2. Telegram Configuration:
   - Update the Telegram bot token and chat ID in `src/drivers/telegram_sender.py`.

### Running the Application

1. Start the RabbitMQ consumer:

```bash
python run.py
```

2. Publish a message to RabbitMQ:

```python
from publisher import RabbitMQPublisher

publisher = RabbitMQPublisher()
publisher.send_message({"msg": "Hello, RabbitMQ and Telegram!"})
```

3. The consumer will automatically process the message and send it to the configured Telegram chat.

### Standalone Telegram Sender

To send a message directly to Telegram without using RabbitMQ:

```bash
python sender.py
```

This will send a predefined message to the configured Telegram chat.

### Troubleshooting

1. RabbitMQ Connection Issues:
   - Ensure RabbitMQ is running and accessible.
   - Verify the connection parameters in `publisher.py` and `src/main/rabbit_mq_configs/consumer.py`.
   - Check RabbitMQ logs for any errors.

2. Telegram Message Sending Failures:
   - Confirm the bot token and chat ID are correct in `src/drivers/telegram_sender.py`.
   - Ensure the bot has permission to send messages to the specified chat.
   - Check for any network issues that might prevent reaching the Telegram API.

3. Message Processing Errors:
   - Enable debug logging in `src/main/rabbit_mq_configs/callback.py` to trace message flow.
   - Verify the message format matches the expected JSON structure.

## Data Flow

1. The publisher sends a message to the RabbitMQ exchange "minha_exchange".
2. The RabbitMQ broker routes the message to the queue "minha_queue".
3. The consumer, running continuously, receives the message from the queue.
4. The consumer's callback function processes the message:
   - Decodes the message body
   - Parses the JSON content
   - Extracts the "msg" field
5. The extracted message is sent to the Telegram chat using the `send_telegram_message` function.

```
[Publisher] -> [RabbitMQ Exchange] -> [RabbitMQ Queue] -> [Consumer] -> [Telegram Sender] -> [Telegram Chat]
```

Note: The system uses a direct exchange with an empty routing key, effectively functioning as a single queue system.