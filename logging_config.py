import logging



def setup_logging():
    logging.basicConfig(
        filename='bot.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    # This adds a nice separator in the log every time the bot starts
    logging.info("================ NEW SESSION STARTED ================")