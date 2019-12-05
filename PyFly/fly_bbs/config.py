import os


class DevConfig:
    '''开发环境配置'''


class ProConfig(DevConfig):
    '''生产环境配置'''


configs = {
        'dev': DevConfig,
        'pro': ProConfig
}
