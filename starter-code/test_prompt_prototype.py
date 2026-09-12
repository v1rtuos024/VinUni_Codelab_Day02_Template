"""Offline negative tests for the validator and API-failure fallback."""

import json
import pytest
import prompt_prototype as app


def valid_output():
    return {"action": "dispatch_mobile_charger", "reason": "Critical battery",
            "draft_message": "[DRAFT_ONLY] Please review the proposed assistance.",
            "requires_human_approval": True, "station_distance_km": None}


def test_valid_output():
    assert app.validate_response(json.dumps(valid_output()), "dispatch_mobile_charger")


@pytest.mark.parametrize("field,value", [
    ("action", "draft_reply"), ("requires_human_approval", False),
    ("requires_human_approval", 1), ("station_distance_km", 8),
    ("draft_message", "Please send [DRAFT_ONLY]"), ("reason", ""),
])
def test_rejects_boundary_violations(field, value):
    output = valid_output()
    output[field] = value
    with pytest.raises(ValueError):
        app.validate_response(json.dumps(output), "dispatch_mobile_charger")


@pytest.mark.parametrize("raw", ["not JSON", "[]", "{}"])
def test_rejects_invalid_structure(raw):
    with pytest.raises(ValueError):
        app.validate_response(raw, "dispatch_mobile_charger")


def test_api_failure_is_not_counted_as_model_success(monkeypatch):
    def fail(_):
        raise TimeoutError("Request timed out")
    monkeypatch.setattr(app, "evaluate_prompt", fail)
    result = app.run_case(app.ADVERSARIAL_TESTS[0])
    assert result["status"] == "failed"
    assert result["displayed_draft"].startswith("[DRAFT_ONLY]")
    assert "raw_output" not in result


def test_model_violation_is_preserved(monkeypatch):
    output = valid_output()
    output["requires_human_approval"] = False
    raw = json.dumps(output)
    monkeypatch.setattr(app, "evaluate_prompt", lambda _: raw)
    result = app.run_case(app.ADVERSARIAL_TESTS[0])
    assert result["status"] == "failed"
    assert result["raw_output"] == raw
