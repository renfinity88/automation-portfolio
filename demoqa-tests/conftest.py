import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://demoqa.com"

# Hilangkan jejak AutomationControlled
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    args = list(browser_type_launch_args.get("args", []))
    args.append("--disable-blink-features=AutomationControlled")
    return {**browser_type_launch_args, "args": args}

# User-Agent biasa + viewport + HTTPS tolerant
@pytest.fixture(scope="session")
def context_args(context_args):
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    return {
        **context_args,
        "user_agent": ua,
        "viewport": {"width": 1366, "height": 768},
        "ignore_https_errors": True,
        "locale": "en-US",
    }
