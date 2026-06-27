from app.db.database import Base, engine
from app.models import User

Base.metadata.create_all(bind=engine)

print("Users table created successfully!")