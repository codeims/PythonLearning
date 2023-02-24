import logging
logging.basicConfig(filename='test.log', level=logging.INFO)
logging.info('This is my first logging class')
l = [1, 2, 3, 4, 5, 6, 7]
for i in l:
    if i == 2:
        logging.info(i)

logging.shutdown()