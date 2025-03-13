import json
import os
from typing import Any, Dict, Optional


class ConfigManager:
    _instance = None
    _config: Dict[str, Dict[str, Any]] = {}
    _config_path: Optional[str] = None

    def __new__(cls) -> "ConfigManager":
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance

    @classmethod
    def load_config(cls, config_path: str) -> None:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

        try:
            with open(config_path, "r", encoding="utf-8") as file:
                cls._config = json.load(file)
                cls._config_path = config_path
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON in configuration file '{config_path}': {e.msg}",
                e.doc,
                e.pos,
            )

    @classmethod
    def get_value(cls, section: str, key: str, default: Any = None) -> Any:
        return cls._config.get(section, {}).get(key, default)

    @classmethod
    def reload_config(cls) -> None:
        if cls._config_path:
            cls.load_config(cls._config_path)
        else:
            raise ValueError("No configuration has been loaded yet.")

    @classmethod
    def get_section(
        cls, section: str, default: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        return cls._config.get(section, default or {})
