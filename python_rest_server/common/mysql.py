from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import logging
import settings

logger = logging.getLogger(__name__)

def init_db_engine_and_session(connectionStr):
    try:
        engine = create_engine(connectionStr, pool_recycle=1800)
        session = scoped_session(sessionmaker(autoflush=True, bind=engine))

        return engine, session
    except Exception as e:
        logger.error(f"Connect to {connectionStr} failed: {e}")
        raise e
    
testEngine, testSession = init_db_engine_and_session(settings.test_db_connection_string)