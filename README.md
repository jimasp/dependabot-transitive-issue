# Dependabot Transitive Dependency Detection Issue Demo

This repository demonstrates a scenario where Dependabot may not detect that a transitive dependency vulnerability has been fixed.

## The Problem Scenario

1. **Initial State**: We have `dependabot-transitive-demo==1.0.0` installed, which depends on `urllib3==1.26.5`
   - urllib3 1.26.5 (transitive dependency) has CVE-2021-33503 (CRLF injection vulnerability)
   - Dependabot will create an alert for the urllib3 vulnerability

2. **The Fix**: We update dependabot-transitive-demo to version 1.0.1 which depends on `urllib3>=1.26.17`
   - The urllib3 vulnerability is resolved
   - However, we didn't directly change urllib3 in requirements.txt - we only changed dependabot-transitive-demo

3. **The Issue**: Dependabot may not automatically detect that the transitive dependency issue is resolved
   - The alert remains open even though the vulnerability is fixed
   - Developers must manually dismiss the alert
   - There's no standard dismissal reason that says "Fixed in merged PR #X"

## Project Structure

```
.
├── app.py                    # Simple Python script
├── requirements.txt          # Python dependencies
├── python-package/           # Source for dependabot-transitive-demo package
└── README.md                 # This file
```

## Steps to Reproduce

### Step 0: Publish the demo package (one-time setup)

First, you need to publish the `dependabot-transitive-demo` package to Test PyPI:

```bash
cd python-package
python -m build
python -m twine upload --repository testpypi dist/*
```

Note: You'll need a Test PyPI account at https://test.pypi.org/account/register/

### Step 1: Create the vulnerability (Initial commit)
```bash
# This commit has dependabot-transitive-demo 1.0.0 with vulnerable urllib3 1.26.5
git add .
git commit -m "Initial commit with vulnerable dependencies"
git push
```

Wait for Dependabot to create an alert for the `urllib3` vulnerability.

### Step 2: Fix the vulnerability (Fix commit)

First, update the python-package to version 1.0.1:
- Update `pyproject.toml`: change `urllib3==1.26.5` to `urllib3>=1.26.17`
- Update `pyproject.toml`: change version to `1.0.1`
- Update `__init__.py`: change `__version__ = "1.0.1"`
- Publish: `python -m build && python -m twine upload dist/*`

Then update `requirements.txt` to:
```
dependabot-transitive-demo==1.0.1
```

```bash
git add requirements.txt
git commit -m "Update dependabot-transitive-demo to fix transitive urllib3 vulnerability"
git push
```

### Step 3: Observe the issue
- The vulnerability is actually fixed (check with `pip install -r requirements.txt && pip list`)
- But Dependabot may not automatically close the alert
- Developers are forced to manually dismiss the alert
- The available dismissal reasons don't include "Fixed in merged PR #X"

## About the Demo Package

This demo uses `dependabot-transitive-demo`, a custom package created specifically for this demonstration. The package:
- Is published to PyPI
- Has no vulnerabilities itself
- Depends on `urllib3==1.26.5` (version 1.0.0) which has CVE-2021-33503
- Will be updated to depend on `urllib3>=1.26.17` (version 1.0.1) to fix the vulnerability

The source code for this package is in the `python-package/` directory.

## Why This Happens

Dependabot typically:
1. Detects vulnerabilities in direct and transitive dependencies
2. Creates PRs to update the vulnerable package directly
3. Auto-closes alerts when it sees the vulnerable package version updated

However, when you fix a transitive dependency by updating its parent package:
- Dependabot may not always correlate the parent package update with the transitive fix
- The vulnerable package isn't explicitly mentioned in the fix PR
- The alert can remain open indefinitely

## Current Workaround

Developers currently dismiss the alert with:
- Dismissal reason: "A fix has already been started"
- Comment: "Fixed in merged PR #X"

## Better Solution Needed

A dismissal reason like "Fixed in merged PR" would be more accurate for this scenario.
