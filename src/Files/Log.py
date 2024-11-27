"""re
    Import all libraries that are being used in the script.
"""
from os.path import join
import logging
from logging import DEBUG, basicConfig, Formatter, getLogger, FileHandler

class LoggerSetup:
    '''
        Define the constructor method that will receive:
        - pathLog: The path where the log file will be stored.
        - nameLog: The name of the log file.
        - nameLogger: The name of the logger that will be used throughout the system.
    '''

    def __init__(self, pathLog, nameLog, nameLogger):
        # Initialize instance variables with the provided parameters
        self._pathLog = pathLog
        self._nameLog = nameLog
        self._nameLogger = nameLogger

    '''
        Define the basic standard configuration for logging:
        - Set up basic logging configurations.
        - Create and configure the formatter for log messages.
        - Determine the path where the log file will be stored.
        - Create a logger with the name provided by the user.
        - Create a file handler to write log messages to the log file.
    '''

    def _setup_logger(self, levellOG: str = None):
        # Configure basic logging settings, including log level and format
        basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        # Create and configure the formatter that defines the structure of log messages
        formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Combine the log file name and path to get the full path where the log will be stored
        log_path = join(self._pathLog, self._nameLog)

        # Create a logger instance with the specified name
        logger = getLogger(self._nameLogger)
        logger.setLevel(DEBUG)  # Set the logging level to DEBUG by default

        # Create a file handler to write log messages to a file
        file_handler = FileHandler(log_path)

        # Convert the string level to the corresponding logging level (e.g., "INFO" to logging.INFO)
        level = getattr(logging, levellOG.upper(), DEBUG)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)  # Apply the formatter to the file handler

        # Add the file handler to the logger so that logs are written to the file
        logger.addHandler(file_handler)

        return logger

    # Create functions to log messages with different levels
    def debugMessage(self, message, level):
        # Set up the logger and log a message at the DEBUG level
        self._logger = self._setup_logger(level)
        self._logger.debug(message)

    def infoMessage(self, message, level):
        # Set up the logger and log a message at the INFO level
        self._logger = self._setup_logger(level)
        self._logger.info(message)

    def errorMessage(self, message, level):
        # Set up the logger and log a message at the ERROR level
        self._logger = self._setup_logger(level)
        self._logger.error(message)

    def warningMessage(self, message, level):
        # Set up the logger and log a message at the WARNING level
        self._logger = self._setup_logger(level)
        self._logger.warning(message)