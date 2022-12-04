from typing import Dict, Any

from .models import PluginData


class PluginDataManager:
    """
    插件所有信息管理
    """

    def __init__(self):
        self._data: Dict[str, PluginData] = {}

    def add_plugin_info(self, info: PluginData):
        """
        说明:
            添加插件信息
        参数:
            :param info: PluginInfo
        """
        if info.model in self._data.keys() and self._data[info.model] == info:
            raise ValueError(f"PluginInfoManager {info.model}:{info.name} 插件名称及类型已存在")
        self._data[info.model] = info

    def get(self, item: str, default: Any = None) -> PluginData:
        return self._data.get(item, default)

    def __getitem__(self, item) -> PluginData:
        return self._data.get(item)

    def __str__(self) -> str:
        return str(self._data)


