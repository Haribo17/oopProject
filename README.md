# 취약점 분석 MCP (Model Context Protocol) 프로젝트

이 프로젝트는 취약점 분석 정보를 관리하고 공유하기 위한 Model Context Protocol 구현입니다.

## 주요 기능

- 실시간 취약점 정보 관리
- CVSS 점수 기반 취약점 심각도 평가
- 취약점 상태 추적 (OPEN, IN_PROGRESS, FIXED, VERIFIED)
- 분석가별 독립적인 세션 관리
- 취약점 데이터베이스 유지 관리

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

## 실행 방법

1. 서버 실행:
```bash
python server.py
```

2. 클라이언트 실행 (새 터미널에서):
```bash
python client.py
```

## 사용 방법

### 취약점 관리
1. 새로운 취약점 추가
   - 제목, 설명, 심각도 입력
   - CVSS 점수 평가
   - 대상 시스템 정보
   - 해결 방안 제시

2. 취약점 목록 조회
   - 전체 취약점 목록 확인
   - 상세 정보 조회

3. 취약점 상태 업데이트
   - OPEN: 새로 발견된 취약점
   - IN_PROGRESS: 수정 중
   - FIXED: 수정 완료
   - VERIFIED: 수정 검증 완료

## 데이터 형식

### 취약점 정보
```json
{
    "id": "VULN-1",
    "timestamp": "2024-01-01T00:00:00",
    "analyst_id": "분석가ID",
    "severity": "HIGH",
    "title": "취약점 제목",
    "description": "상세 설명",
    "target_system": "대상 시스템",
    "status": "OPEN",
    "cvss_score": 7.5,
    "remediation": "해결 방안"
}
```

## 주의사항

- 서버는 기본적으로 localhost:8080에서 실행됩니다.
- 모든 취약점 데이터는 메모리에 저장되며, 서버 재시작 시 초기화됩니다.
- 실제 운영 환경에서는 영구 저장소 연동이 필요합니다. 