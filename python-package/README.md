# Dependabot Transitive Demo Package

This is a minimal Python package created to demonstrate Dependabot's behavior with transitive dependency vulnerabilities.

## Purpose

- **Version 1.0.0**: Depends on `urllib3==1.26.5` which has CVE-2021-33503
- **Version 1.0.1** (to be published later): Will update to `urllib3>=1.26.17` which fixes the vulnerability

This package itself contains no vulnerabilities - it simply depends on a vulnerable package to demonstrate how Dependabot handles transitive dependency issues.

## Installation

```bash
pip install dependabot-transitive-demo
```

## Usage

```python
from dependabot_transitive_demo import demo_function

demo_function()
```
