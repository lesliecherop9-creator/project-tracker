class Identified:
    _next_id = 1

    @classmethod
    def _allocate_id(cls, given_id=None):
        """
        If given_id is provided (eg loading from a file),
        use that. Otherwise use the next available ID.
        """
        if given_id is None:
            new_id = cls._next_id
        else:
            new_id = int(given_id)

        if new_id >= cls._next_id:
            cls._next_id = new_id + 1

        return new_id

    @classmethod
    def reset_counter(cls):
        """reset ID counter (mainly for tests)"""
        cls._next_id = 1
