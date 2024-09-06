#!/bin/bash
# 전체 pytest 테스트 실행 및 Allure 보고서 생성

# pytest 테스트 실행 및 Allure 결과 생성
pytest tests/test_naver.py

# Allure 보고서 생성 및 자동 실행
allure serve allure-results
 