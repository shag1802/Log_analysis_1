import logging
import time
import random
# Configure logging
# logging.basicConfig(level=logging.DEBUG) # Set the root logger level to
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# DEBUG
# Create a logger
logger = logging.getLogger(__name__)
# Define log message formats
formats = {
logging.INFO: "INFO message",
logging.DEBUG: "DEBUG message",
logging.ERROR: "ERROR message"
}
# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]
# Main loop to log messages
while True:
    try:
    # Randomly select a log level
        log_level = random.choice(log_levels)
        # Get the log message format for the selected log level
        log_message = formats[log_level]
        # Log the message
        logger.log(log_level, log_message)
        
        time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nLogging interrupted. Exiting.")
        break
