# -*- coding: utf-8 -*-


class JUHEErrorCodeType(object):
    @staticmethod
    def to_string(error_code):
        return {
            203901: '查询城市不能为空',
            203902: '查询不到该城市的天气',
            203903: '查询出错，请重试',
            203904: '错误的GPS坐标',
            203905: 'GPS坐标解析出错，请确认提供的坐标正确（暂支持国内）',
            203906: 'IP地址错误',
            203907: '查询不到该IP地址相关的天气信息',

            10001: '错误的请求KEY',
            10002: '该KEY无请求权限',
            10003: 'KEY过期',
            10004: '错误的OPENID',
            10005: '应用未审核超时，请提交认证',
            10007: '未知的请求源',
            10008: '被禁止的IP',
            10009: '被禁止的KEY',
            10011: '当前IP请求超过限制',
            10012: '请求超过次数限制',
            10013: '测试KEY超过请求限制',
            10014: '系统内部异常(调用充值类业务时，请务必联系客服或通过订单查询接口检测订单，避免造成损失)',
            10020: '接口维护',
            10021: '接口停用',
        }[error_code]
