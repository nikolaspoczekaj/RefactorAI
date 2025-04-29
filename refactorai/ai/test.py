from openai import OpenAI
import os
import json
import logging

class AIClient:
    """
    Client für DeepSeek/OpenAI-kompatible APIs.
    Unterstützt Text- und JSON-Ausgaben.
    """

    def __init__(
        self,
        api_key: str = None,
        base_url: str = "https://api.deepseek.com",
        default_model: str = "deepseek-chat",
        default_tokens: int = 8000,
        default_temperature: float = 1.0,
    ):
        """
        Initialisiert den AIClient.
        :param api_key: API-Key (falls None, wird aus Umgebungsvariable DEEPSEEK_KEY gelesen)
        :param base_url: Basis-URL der API
        :param default_model: Standardmodellname
        :param default_tokens: Standardwert für max_tokens
        :param default_temperature: Standardwert für temperature
        """
        self.api_key = api_key or os.getenv("DEEPSEEK_KEY")
        self.base_url = base_url
        self.default_model = default_model
        self.default_tokens = default_tokens
        self.default_temperature = default_temperature
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        self.logger = logging.getLogger(__name__)

    def text(
        self,
        system: str,
        prompt: str,
        tokens: int = None,
        temp: float = None,
        model: str = None,
        stream: bool = False,
    ) -> str:
        """
        Holt eine Textantwort vom Modell.
        """
        try:
            response = self.client.chat.completions.create(
                model=model or self.default_model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                stream=stream,
                max_tokens=tokens or self.default_tokens,
                temperature=temp if temp is not None else self.default_temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Text-Request fehlgeschlagen: {e}")
            raise

    def json(
        self,
        system: str,
        prompt: str,
        tokens: int = None,
        temp: float = None,
        model: str = None,
    ) -> dict:
        """
        Holt eine JSON-Antwort vom Modell.
        """
        try:
            response = self.client.chat.completions.create(
                model=model or self.default_model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                stream=False,
                max_tokens=tokens or self.default_tokens,
                temperature=temp if temp is not None else self.default_temperature,
                response_format={'type': 'json_object'}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            self.logger.error(f"JSON-Request fehlgeschlagen: {e}")
            raise

    def set_model(self, model_name: str):
        """
        Setzt das Standardmodell.
        """
        self.default_model = model_name

    def set_temperature(self, temperature: float):
        """
        Setzt die Standardtemperatur.
        """
        self.default_temperature = temperature
