def extract_features(parsed_log):

    if parsed_log is None:
        return None

    method = parsed_log["method"]

    method_get = 1 if method == "GET" else 0
    method_post = 1 if method == "POST" else 0

    url = parsed_log["url"]

    url_length = len(url)

    contains_query = 1 if "?" in url else 0

    status = parsed_log["status"]

    contains_admin = 1 if "admin" in url.lower() else 0
    contains_login = 1 if "login" in url.lower() else 0

    sql_keywords = [
        "select",
        "union",
        "drop",
        "insert",
        "delete",
        "update",
        "--",
        "'"
    ]

    contains_sql_keyword = 1 if any(keyword in url.lower() for keyword in sql_keywords) else 0

    status_is_error = 1 if status >= 400 else 0

    # Timestamp format: 23/Jul/2026:10:15:00
    hour = int(parsed_log["timestamp"].split(":")[1])

    return {
        "status": status,
        "url_length": url_length,
        "method_get": method_get,
        "method_post": method_post,
        "contains_query": contains_query,
        "contains_admin": contains_admin,
        "contains_login": contains_login,
        "contains_sql_keyword": contains_sql_keyword,
        "status_is_error": status_is_error,
        "hour": hour
    }