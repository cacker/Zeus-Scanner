import re

from lib.core.common import HTTP_HEADER


__item__ = "FortiWeb Web Application Firewall (Fortinet)"


def detect(content, **kwargs):
    headers = kwargs.get("headers", None)
    content = str(content)
    detection_schema = (
        re.compile(r"<.+>powered.by.fortinet<.+.>", re.I),
        re.compile(r"<.+>fortigate.ips.sensor<.+.>", re.I),
        re.compile(r"fortigate", re.I), re.compile(r".fgd_icon", re.I),
        re.compile(r"\AFORTIWAFSID=", re.I)
    )
    for detection in detection_schema:
        if detection.search(content) is not None:
            return True
        if detection.search(headers.get(HTTP_HEADER.SET_COOKIE, "")) is not None:
            return True
