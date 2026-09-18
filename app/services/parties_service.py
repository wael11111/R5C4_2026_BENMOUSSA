from app.repositories.parties_repository import PartiesRepository


class PartiesService:

    def __init__(self, db_path):
        self.repository = PartiesRepository(db_path)

    def get_parties(self, limit=20, offset=0):
        return self.repository.get_parties(limit, offset)