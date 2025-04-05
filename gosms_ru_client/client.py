import requests
from typing import Optional, Dict, Any
from .exceptions import GoSMSAuthError, GoSMSRequestError, GoSMSValidationError

class GoSMSClient:
    """Клиент для работы с API GoSMS."""
    
    BASE_URL = "https://api.gosms.ru/v1"
    
    def __init__(self, api_key: str):
        """
        Инициализация клиента GoSMS.
        
        Args:
            api_key (str): API ключ для аутентификации
        """
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    def send_sms(self, phone_number: str, message: str, device_id: Optional[str] = None, 
                 to_sim: Optional[int] = None, callback_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Отправка SMS сообщения.
        
        Args:
            phone_number (str): Номер телефона получателя
            message (str): Текст сообщения
            device_id (str, optional): ID устройства для отправки
            to_sim (int, optional): Номер слота SIM-карты
            callback_id (str, optional): ID вебхука для обработки события
            
        Returns:
            Dict[str, Any]: Ответ от API
            
        Raises:
            GoSMSAuthError: Ошибка аутентификации
            GoSMSRequestError: Ошибка при выполнении запроса
            GoSMSValidationError: Ошибка валидации данных
        """
        if not phone_number or not message:
            raise GoSMSValidationError("Phone number and message are required")
            
        data = {
            "phone_number": phone_number,
            "message": message
        }
        
        if device_id is not None:
            data["device_id"] = device_id
        if to_sim is not None:
            data["to_sim"] = to_sim
        if callback_id is not None:
            data["callback_id"] = callback_id
            
        try:
            response = self.session.post(
                f"{self.BASE_URL}/sms/send",
                json=data
            )
            
            if response.status_code == 401:
                raise GoSMSAuthError("Invalid API key")
            elif response.status_code == 400:
                raise GoSMSValidationError(response.json().get("message", "Validation error"))
            elif response.status_code != 200:
                raise GoSMSRequestError(f"Request failed with status {response.status_code}")
                
            return response.json()
            
        except requests.RequestException as e:
            raise GoSMSRequestError(f"Request failed: {str(e)}") 