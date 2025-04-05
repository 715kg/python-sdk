"""
GoSMS Python SDK
~~~~~~~~~~~~~~~

Простой Python пакет для работы с API GoSMS.
"""

from .client import GoSMSClient
from .exceptions import GoSMSError

__version__ = "0.1.0"
__all__ = ["GoSMSClient", "GoSMSError"] 