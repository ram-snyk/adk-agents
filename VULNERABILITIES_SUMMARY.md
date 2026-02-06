# Vulnerability Quick Reference

## All 7 Vulnerabilities Found (Summary)

### 🟡 MEDIUM Severity (3 total)

| ID | Vulnerability | Package/Resource | Status | Fix |
|----|---------------|------------------|--------|-----|
| VULN-001 | Insertion of Sensitive Information | requests@2.31.0 | ✅ FIXED | Upgrade to 2.32.4 |
| VULN-002 | Control Flow Implementation Error | requests@2.31.0 | ✅ FIXED | Upgrade to 2.32.4 |
| VULN-003 | MPL-2.0 License Issue | certifi@2026.1.4 | ⚠️ ACCEPTED | Permissive license, no action needed |

### 🔵 LOW Severity (4 total)

| ID | Vulnerability | Package/Resource | Status | Fix |
|----|---------------|------------------|--------|-----|
| VULN-004 | No Logging on Storage Bucket | google_storage_bucket | ✅ FIXED | Added logging block |
| VULN-005 | No Customer-Managed Encryption | google_storage_bucket | ✅ FIXED | Implemented KMS encryption |
| VULN-006 | Audit Bucket Without Logging | google_storage_bucket | ⚠️ ACCEPTED | Circular dependency |
| VULN-007 | Container UID Could Clash | Kubernetes Deployment | ✅ FIXED | Changed UID to 10000 |

---

## By Scan Type

### 🐳 Container Scan
- **VULN-001** (Medium): requests - Sensitive info disclosure → ✅ Fixed
- **VULN-002** (Medium): requests - Control flow error → ✅ Fixed  
- **VULN-003** (Medium): certifi - License issue → ⚠️ Accepted

### ☁️ IaC Terraform Scan
- **VULN-004** (Low): Storage bucket logging → ✅ Fixed
- **VULN-005** (Low): Customer encryption keys → ✅ Fixed
- **VULN-006** (Low): Audit bucket logging → ⚠️ Accepted

### ☸️ IaC Kubernetes Scan
- **VULN-007** (Low): Container UID collision → ✅ Fixed

---

## Quick Stats

- **Total Found:** 7
- **Fixed:** 5 (71%)
- **Accepted:** 2 (29%)
- **Critical/High:** 0
- **Medium:** 3
- **Low:** 4

---

## Key Fixes Applied

1. ✅ Upgraded `requests` from 2.31.0 → 2.32.4
2. ✅ Added KMS encryption to Cloud Storage
3. ✅ Enabled logging on primary storage bucket
4. ✅ Changed Kubernetes UID from 1000 → 10000
5. ⚠️ Accepted MPL-2.0 license (permissive)
6. ⚠️ Accepted audit bucket logging (circular dependency)

---

For detailed information on each vulnerability, see: **VULNERABILITIES_DETAILED.md**
