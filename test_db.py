from app.db.database import Base, engine
from app.models import User, Note

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")