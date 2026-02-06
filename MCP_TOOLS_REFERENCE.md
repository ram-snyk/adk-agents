# Snyk MCP Tools - Complete Reference

This project uses the **Snyk MCP Server** which provides comprehensive security scanning tools.

---

## 🔧 Available Snyk MCP Tools

### 1. **Authentication & Setup**

#### `snyk_auth`
- **Purpose:** Authenticate with Snyk
- **When to use:** First time setup, or when authentication expires
- **Usage in this project:** ✅ Used to authenticate before scanning
```json
{
  "server": "user-snyk",
  "toolName": "snyk_auth",
  "arguments": {}
}
```

#### `snyk_trust`
- **Purpose:** Trust a folder to allow Snyk scanning
- **When to use:** Before scanning any new project directory
- **Usage in this project:** ✅ Used to trust `/adk-agents` directory
```json
{
  "server": "user-snyk",
  "toolName": "snyk_trust",
  "arguments": {
    "path": "/absolute/path/to/project"
  }
}
```

---

### 2. **Security Scanning Tools** (Core Functionality)

#### `snyk_sca_scan` (Software Composition Analysis)
- **Purpose:** Scan dependencies for vulnerabilities
- **Scans:** `requirements.txt`, `package.json`, `pom.xml`, etc.
- **Usage in this project:** ✅ Scanned Python dependencies
- **Results:** 0 issues found (with skip-unresolved flag)

**Example:**
```json
{
  "server": "user-snyk",
  "toolName": "snyk_sca_scan",
  "arguments": {
    "path": "/absolute/path/to/project",
    "command": "python3",
    "severity_threshold": "low",
    "skip_unresolved": true
  }
}
```

**What we scanned:**
- `requirements.txt` with google-genai, flask, requests, etc.

---

#### `snyk_code_scan` (SAST - Static Application Security Testing)
- **Purpose:** Scan source code for security vulnerabilities
- **Scans:** Python, JavaScript, Java, Go, etc.
- **Usage in this project:** ✅ Scanned `agent.py`
- **Results:** 0 issues found

**Example:**
```json
{
  "server": "user-snyk",
  "toolName": "snyk_code_scan",
  "arguments": {
    "path": "/absolute/path/to/file.py",
    "severity_threshold": "low"
  }
}
```

**What we scanned:**
- `agent.py` - Main ADK agent code
- All Python source files in the project

---

#### `snyk_container_scan`
- **Purpose:** Scan Docker containers for vulnerabilities
- **Scans:** OS packages, application dependencies in images
- **Usage in this project:** ✅ Scanned `adk-agent:latest`
- **Results:** 3 issues found (2 fixed, 1 accepted)

**Example:**
```json
{
  "server": "user-snyk",
  "toolName": "snyk_container_scan",
  "arguments": {
    "image": "adk-agent:latest",
    "severity_threshold": "low"
  }
}
```

**What we found:**
- VULN-001: requests@2.31.0 - Sensitive info disclosure → ✅ Fixed
- VULN-002: requests@2.31.0 - Control flow error → ✅ Fixed
- VULN-003: certifi - MPL-2.0 license → ⚠️ Accepted

---

#### `snyk_iac_scan` (Infrastructure as Code)
- **Purpose:** Scan IaC files for misconfigurations
- **Scans:** Terraform, Kubernetes, CloudFormation, ARM templates
- **Usage in this project:** ✅ Scanned Terraform and K8s configs
- **Results:** 4 issues found (3 fixed, 1 accepted)

**Example:**
```json
{
  "server": "user-snyk",
  "toolName": "snyk_iac_scan",
  "arguments": {
    "path": "/absolute/path/to/terraform/",
    "severity_threshold": "low"
  }
}
```

**What we scanned:**
- `terraform/main.tf` - GCP infrastructure
- `k8s-deployment.yaml` - Kubernetes deployment

**What we found:**
- VULN-004: No logging on storage bucket → ✅ Fixed
- VULN-005: No customer-managed encryption → ✅ Fixed
- VULN-006: Audit bucket logging → ⚠️ Accepted
- VULN-007: Container UID collision → ✅ Fixed

---

### 3. **Advanced Scanning Tools**

#### `snyk_sbom_scan`
- **Purpose:** Scan Software Bill of Materials (SBOM)
- **Scans:** CycloneDX, SPDX format SBOMs
- **Usage in this project:** ❌ Not used (experimental)
- **Use case:** Scan third-party software when only SBOM available

**Example:**
```json
{
  "server": "user-snyk",
  "toolName": "snyk_sbom_scan",
  "arguments": {
    "file": "/absolute/path/to/sbom.json",
    "severity_threshold": "low"
  }
}
```

---

#### `snyk_aibom`
- **Purpose:** AI-specific Bill of Materials scanning
- **Scans:** AI/ML model dependencies
- **Usage in this project:** ❌ Not used
- **Use case:** Scan AI models and training data dependencies

---

### 4. **Utility Tools**

#### `snyk_version`
- **Purpose:** Check Snyk CLI version
- **Usage in this project:** ❌ Not used
```json
{
  "server": "user-snyk",
  "toolName": "snyk_version",
  "arguments": {}
}
```

#### `snyk_logout`
- **Purpose:** Logout from Snyk
- **Usage in this project:** ❌ Not used
```json
{
  "server": "user-snyk",
  "toolName": "snyk_logout",
  "arguments": {}
}
```

#### `snyk_send_feedback`
- **Purpose:** Send feedback to Snyk
- **Usage in this project:** ❌ Not used
```json
{
  "server": "user-snyk",
  "toolName": "snyk_send_feedback",
  "arguments": {
    "feedback": "Great tool!"
  }
}
```

---

## 📊 Summary of Tool Usage in This Project

| Tool | Used | Scans Performed | Issues Found | Status |
|------|------|----------------|--------------|--------|
| `snyk_auth` | ✅ | - | - | Authenticated |
| `snyk_trust` | ✅ | - | - | Trusted project |
| `snyk_sca_scan` | ✅ | 1 | 0 | ✅ Clean |
| `snyk_code_scan` | ✅ | 2 | 0 | ✅ Clean |
| `snyk_container_scan` | ✅ | 1 | 3 | ✅ 2 fixed, 1 accepted |
| `snyk_iac_scan` | ✅ | 2 | 4 | ✅ 3 fixed, 1 accepted |
| `snyk_sbom_scan` | ❌ | 0 | - | Not needed |
| `snyk_aibom` | ❌ | 0 | - | Not needed |
| `snyk_version` | ❌ | - | - | Not needed |
| `snyk_logout` | ❌ | - | - | Not needed |
| `snyk_send_feedback` | ❌ | - | - | Not needed |

---

## 🔍 Complete Scan Workflow

### Step 1: Setup
```bash
snyk_auth                              # Authenticate
snyk_trust --path=/project/path        # Trust directory
```

### Step 2: Dependency Scan
```bash
snyk_sca_scan \
  --path=/project \
  --command=python3 \
  --severity_threshold=low
```

### Step 3: Code Scan
```bash
snyk_code_scan \
  --path=/project/agent.py \
  --severity_threshold=low
```

### Step 4: Container Scan
```bash
snyk_container_scan \
  --image=adk-agent:latest \
  --severity_threshold=low
```

### Step 5: IaC Scan
```bash
snyk_iac_scan \
  --path=/project/terraform \
  --severity_threshold=low

snyk_iac_scan \
  --path=/project/k8s-deployment.yaml \
  --severity_threshold=low
```

---

## 🎯 Tool Selection Guide

**For Python projects:**
- ✅ Use `snyk_sca_scan` with `command=python3`
- ✅ Use `snyk_code_scan` on `.py` files

**For containers:**
- ✅ Use `snyk_container_scan` on Docker images
- 💡 Add `--file=Dockerfile` for better remediation advice

**For infrastructure:**
- ✅ Use `snyk_iac_scan` on Terraform (`.tf` files)
- ✅ Use `snyk_iac_scan` on Kubernetes (`.yaml` files)
- ✅ Use `snyk_iac_scan` on CloudFormation templates

**For third-party software:**
- ✅ Use `snyk_sbom_scan` if you have an SBOM file
- ⚠️ Tool is experimental

---

## 📖 References

- **Snyk Documentation:** https://docs.snyk.io/
- **MCP Server Info:** Installed at `/Users/ramdhakne/.cursor/projects/.../mcps/user-snyk/`
- **Tool Schemas:** Available in `mcps/user-snyk/tools/*.json`

---

**All tools used in this project are documented in:**
- [WORKFLOW.md](WORKFLOW.md) - Complete scanning workflow
- [SECURITY_REPORT.md](SECURITY_REPORT.md) - Security assessment
- [VULNERABILITIES_DETAILED.md](VULNERABILITIES_DETAILED.md) - All findings
