class GoSMSError(Exception):
    """Базовый класс для всех исключений GoSMS."""
    pass

class GoSMSAuthError(GoSMSError):
    """Ошибка аутентификации."""
    pass

class GoSMSRequestError(GoSMSError):
    """Ошибка при выполнении запроса."""
    pass

class GoSMSValidationError(GoSMSError):
    """Ошибка валидации данных."""
    pass 