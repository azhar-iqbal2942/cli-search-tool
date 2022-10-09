from pytest import MonkeyPatch

from app.cli import SearchCommandLineInterface


def test_search_with_user_file_and_id_column(monkeypatch: MonkeyPatch) -> None:
    inputs = [1, 1, "_id", "1", "quit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    instance = SearchCommandLineInterface()
    resp = instance.search()

    assert resp == None


def test_search_with_user_file_and_tags_column(monkeypatch: MonkeyPatch) -> None:
    inputs = [1, 1, "tags", "Kaka", "quit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    instance = SearchCommandLineInterface()
    resp = instance.search()

    assert resp == None


def test_search_with_user_file_and_shared_column(monkeypatch: MonkeyPatch) -> None:
    inputs = [1, 1, "shared", "true", "quit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    instance = SearchCommandLineInterface()
    resp = instance.search()

    assert resp == None


def test_search_with_user_file_and_invalid_id(monkeypatch: MonkeyPatch) -> None:
    inputs = [1, 1, "_id", "300", "quit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    instance = SearchCommandLineInterface()
    resp = instance.search()

    assert resp == None
