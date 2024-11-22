"""."""

from chalice import Chalice

app = Chalice(app_name="app_test")


@app.route("/hello/{name}")
def hello_name(name: str) -> dict:
    """.

    Args:
        name (str): 名前

    Returns:
        dict: レスポンス
    """
    return {"hello": name}


@app.route("/users", methods=["POST"])
def create_user() -> dict:
    """.

    Returns:
        dict: レスポンス
    """
    user_as_json = app.current_request.json_body
    return {"user": user_as_json}
