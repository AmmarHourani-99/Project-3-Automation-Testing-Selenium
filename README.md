# Project 3 — Automation Testing | Selenium + Python

## Overview
Automation testing project using Selenium WebDriver and Python.
This project automates key user flows on the Sauce Demo web application
including valid login, invalid login error handling, and logout functionality.

## Test Summary
| Field | Details |
|---|---|
| Tester | Ammar Hourani |
| Environment | Mac / Chrome 146 / Python 3.9.6 / Selenium 4.36.0 |
| Total Scripts | 3 |
| Passed | 3 |
| Failed | 0 |
| Overall Status | Pass — All automated test scripts executed successfully |

## Test Scripts
| Script | Description | Result |
|---|---|---|
| test_login.py | Valid login with correct credentials | ✅ Pass |
| test_login_invalid.py | Invalid login with wrong credentials | ✅ Pass |
| test_logout.py | Valid login followed by logout | ✅ Pass |

## Tools Used
- Python 3.9.6
- Selenium 4.36.0
- WebDriver Manager
- Google Chrome 146
- VS Code

## Website Tested
- https://www.saucedemo.com — Demo e-commerce application by Sauce Labs

## How to Run
1. Install Python 3.9+
2. Install dependencies:
pip3 install selenium webdriver-manager
3. Run any script:
python3 test_login.py
python3 test_login_invalid.py
python3 test_logout.py
