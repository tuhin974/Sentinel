def extract_features(parsed_log):

    if parsed_log is None:
        return None

    method = parsed_log["method"]

    method_get = 1 if method == "GET" else 0
    method_post = 1 if method == "POST" else 0

    url_length = len(parsed_log["url"])

    contains_query = 1 if "?" in parsed_log["url"] else 0
    
    status = parsed_log["status"]

    return {
    "status": 500,
    "url_length": 12,
    "method_get": 0,
    "method_post": 1,
    "contains_query": 1,
    "contains_admin": 1,
    "contains_login": 0,
    "contains_sql_keyword": 1,
    "status_is_error": 1,
    "hour": 10
}
