class TrackerError(Exception):
    """Base class for all errors raised by the tracker."""

class StorageError(TrackerError):
    """Raised when saving or loading the data file fails."""