#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__version__ = "GIT"
__author__ = {
    "name": "Hiroaki Yamamoto",
    "email": "admin@hysoftware.net"
}
__license__ = "GPLv3"
__copyright__ = "(c) 2014 by Hiroaki Yamamoto"
__url__ = "http://hysoftware.net"
__all__ = ["errorhandler"]

from flask import Blueprint, jsonify


errorhandler = Blueprint("errorhandler", __name__)


# If you want to create your own error,
# inherit this base function
class StatusReasonError(Exception):
    __status = 500
    __reason = "Error"
    __additional_info = {}

    def __init__(self, status, reason, **additional_info):
        self.__additional_info = additional_info
        self.__reason = reason
        self.__status = status

    @property
    def status(self):
        return self.__status

    @property
    def reason(self):
        return self.__reason

    @property
    def additional_info(self):
        return self.__additional_info


# Commonly used Errors
class NotFound(StatusReasonError):
    def __init__(self, reason="Not Found", **additional_info):
        StatusReasonError.__init__(self, 404, reason, **additional_info)


class NotAuthorized(StatusReasonError):
    def __init__(self, reason="Not Authorized", **additional_info):
        StatusReasonError.__init__(self, 401, reason, **additional_info)


class PermissionDenied(StatusReasonError):
    def __init__(self, reason="Permission Denied", **additional_info):
        StatusReasonError.__init__(self, 403, reason, **additional_info)


@errorhandler.app_errorhandler(StatusReasonError)
def custom_err(e):
    toJson = {
        "status": e.status,
        "message": e.reason
    }
    toJson.update(e.additional_info)

    response = jsonify(toJson)
    response.status_code = e.status
    return response


# These handlers are generic handlers
@errorhandler.app_errorhandler(NotImplementedError)
def __not_implemented(e):
    status_code = 501
    response = jsonify({"status": status_code,
                        "message": "Not Implemented Yet"
                        })
    response.status_code = status_code
    return response


@errorhandler.app_errorhandler(BaseException)
def __general_err(e):
    status_code = 500
    response = jsonify({"status": status_code,
                        "message": ("{0}: {1}").format(
                            type(e).__name__,
                            str(e))
                        })
    response.status_code = status_code
    return response
