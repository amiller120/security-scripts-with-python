from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///security1.db')
Base = declarative_base()


class Log(Base):
    __tablename__ = "log"

    date1 = Column(String, primary_key=True)
    policy = Column(String)
    port = Column(Integer)
    source_address = Column(String)
    source_zone = Column(String)
    destination_address = Column(String)
    destination_zone = Column(String)

    def __init__(self, date1, policy, port, source_address, source_zone, destination_address, destination_zone):
        self.date1 = date1
        self.policy = policy
        self.port = port
        self.source_address = source_address
        self.source_zone = source_zone
        self.destination_address = destination_address
        self.destination_zone = destination_zone


Base.metadata.create_all(engine)

