#!/bin/bash
# 전체 pytest 테스트 실행 및 Allure 보고서 생성

# pytest 테스트 실행 및 Allure 결과 생성
#pytest tests/test_naver.py
#pytest tests/test_sample.py
#pytest tests/test_sample.py

pytest --alluredir=reports/allure-results

# Allure 보고서 생성 및 자동 실행
allure serve reports/allure-results

rm -rf reports/