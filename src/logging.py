import logging

def logging_wrapper(level, path):

   # Determine desired logging level
   level = int(str(level) + "0")

   # Create a logging instance
   logger = logging.getLogger()
   logger.setLevel(level)

   # Setup logging file
   logger_handler = logging.FileHandler(path)
   logger_handler.setLevel(level)

   # Formatting:
   logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

   # Put them together
   logger_handler.setFormatter(logger_formatter)

   logger.addHandler(logger_handler)
   logger.info("Logging successfully configured!")

   return logger