
#Logiing level =(DEBUG,INFO ,WARNING, ERROR , CRITICAL )
#format : log message format
#info ma info bhanda mathiko print hunxa 
#basic config hunu parxa ra ek turn matra basic config use garne 

import logging

logging.basicConfig(level=logging.WARNING,
                    format="%(asctime)s %(levelname)s %(message)s",
                    filename="app.log",
                    filemode="a"
                    )
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

