# Google ADK Agent with Snyk Security Integration

This project demonstrates building a secure Google AI Development Kit (ADK) agent with comprehensive security scanning using Snyk MCP server at every development stage.

## 🔒 Security-First Development Approach

This project showcases **"Secure at Inception"** by integrating security checks at every stage:

1. **Dependency Scanning (SCA)** - Scan Python dependencies for vulnerabilities
2. **Code Analysis (SAST)** - Detect security issues in application code
3. **Container Security** - Scan Docker images for vulnerabilities
4. **Infrastructure Security (IaC)** - Validate infrastructure configurations

### Security Results Summary

| Layer | Scan Type | Vulnerabilities | Status |
|-------|-----------|----------------|--------|
| Dependencies | SCA | 0 issues | ✅ PASS |
| Source Code | SAST | 0 issues | ✅ PASS |
| Container | Container Scan | 3 issues | ✅ FIXED (2), ACCEPTED (1) |
| Infrastructure | IaC Scan | 4 issues | ✅ FIXED (3), ACCEPTED (1) |

**Total:** 7 vulnerabilities found, 5 fixed (71%), 2 accepted with rationale (29%)

---

## 📚 Documentation

This project includes comprehensive documentation:

### Quick Start
- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[README.md](README.md)** - This file (project overview)

### Security Reports
- **[VULNERABILITIES_SUMMARY.md](VULNERABILITIES_SUMMARY.md)** - Quick reference of all 7 vulnerabilities
- **[VULNERABILITIES_DETAILED.md](VULNERABILITIES_DETAILED.md)** - Complete analysis with CVEs, fixes, and rationale
- **[SECURITY_REPORT.md](SECURITY_REPORT.md)** - Comprehensive security assessment report

### Workflows
- **[WORKFLOW.md](WORKFLOW.md)** - Complete Snyk MCP scanning workflow with examples

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
export GOOGLE_API_KEY="your-api-key"
```

### 3. Run the Agent
```bash
python agent.py
```

### 4. Run Security Scans
```bash
# Dependency scan
snyk_sca_scan --path=/path/to/project --command=python3

# Code scan
snyk_code_scan --path=agent.py

# Container scan (after building)
docker build -t adk-agent:latest .
snyk_container_scan --image=adk-agent:latest

# IaC scan
snyk_iac_scan --path=terraform/
snyk_iac_scan --path=k8s-deployment.yaml
```

---

## 📁 Project Structure

```
adk-agents/
├── agent.py                          # Main ADK agent implementation
├── requirements.txt                  # Python dependencies (secured)
├── Dockerfile                        # Container definition (hardened)
├── k8s-deployment.yaml              # Kubernetes manifests (secure)
├── terraform/
│   └── main.tf                      # GCP infrastructure (encrypted, logged)
├── .env.example                     # Environment template
├── .dockerignore                    # Docker ignore patterns
│
├── README.md                        # This file
├── QUICKSTART.md                    # Quick start guide
├── SECURITY_REPORT.md               # Comprehensive security report
├── VULNERABILITIES_SUMMARY.md       # Quick vulnerability reference
├── VULNERABILITIES_DETAILED.md      # Detailed vulnerability analysis
└── WORKFLOW.md                      # Complete scanning workflow
```

---

## 🛡️ Vulnerabilities Found & Fixed

### Summary by Severity

**Medium (3):**
- ✅ VULN-001: requests - Sensitive info disclosure (Fixed: Upgrade to 2.32.4)
- ✅ VULN-002: requests - Control flow error (Fixed: Upgrade to 2.32.4)
- ⚠️ VULN-003: certifi - MPL-2.0 license (Accepted: Permissive license)

**Low (4):**
- ✅ VULN-004: Storage bucket logging (Fixed: Added logging)
- ✅ VULN-005: No customer encryption (Fixed: KMS implemented)
- ⚠️ VULN-006: Audit bucket logging (Accepted: Circular dependency)
- ✅ VULN-007: Container UID clash (Fixed: Changed to 10000)

**See [VULNERABILITIES_SUMMARY.md](VULNERABILITIES_SUMMARY.md) for quick reference**  
**See [VULNERABILITIES_DETAILED.md](VULNERABILITIES_DETAILED.md) for complete analysis**

---

## 🔧 Security Features Implemented

### Application Level
- ✅ Type-safe function declarations
- ✅ Environment variable management
- ✅ Error handling and validation
- ✅ Structured logging capability

### Container Level
- ✅ Non-root user execution (UID 10000)
- ✅ Minimal base image (python:3.11-slim)
- ✅ Health checks configured
- ✅ Updated dependencies (requests@2.32.4)
- ✅ Read-only root filesystem

### Infrastructure Level
- ✅ Customer-managed encryption (KMS)
- ✅ Audit logging enabled
- ✅ Network policies for segmentation
- ✅ Secret management (Secret Manager)
- ✅ Service account with least privilege
- ✅ 90-day key rotation
- ✅ Resource quotas and limits

---

## 🎯 Example Usage

The agent provides a customer service assistant with two tools:

### 1. Knowledge Base Search
```
You: What's your shipping policy?
Agent: Standard shipping takes 5-7 business days. Express shipping takes 2-3 business days.
```

### 2. Order Status Check
```
You: Check order ORD-12345
Agent: Your order has been shipped with tracking number 1Z999AA10123456784. 
       Estimated delivery: 2026-02-05
```

---

## 🔍 Snyk MCP Integration

This project uses Snyk MCP server for automated security scanning:

### Available Scans
- **SCA (Software Composition Analysis)** - Dependencies
- **SAST (Static Application Security Testing)** - Source code
- **Container Security** - Docker images
- **IaC Security** - Terraform and Kubernetes

### Scan Commands
```bash
# Authenticate once
snyk_auth

# Trust directory
snyk_trust --path=/path/to/project

# Run scans
snyk_sca_scan --path=/path --command=python3
snyk_code_scan --path=file.py
snyk_container_scan --image=image:tag
snyk_iac_scan --path=terraform/
```

**See [WORKFLOW.md](WORKFLOW.md) for complete scanning workflow**

---

## 📊 Compliance Alignment

This implementation aligns with:
- ✅ OWASP Top 10 - Address common vulnerabilities
- ✅ CIS Benchmarks - Container and Kubernetes hardening
- ✅ NIST Cybersecurity Framework - Identify, Protect, Detect
- ✅ SOC 2 Type II - Security controls and audit trail
- ✅ ISO 27001 - Information security management

---

## 🚀 CI/CD Integration

Add to your pipeline:

```yaml
# Example GitHub Actions
- name: Snyk Security Scan
  run: |
    snyk auth ${{ secrets.SNYK_TOKEN }}
    snyk test --all-projects
    snyk code test
    snyk container test $IMAGE_NAME
    snyk iac test terraform/
```

---

## 📖 Learn More

- [Google ADK Documentation](https://ai.google.dev/adk)
- [Snyk Documentation](https://docs.snyk.io/)
- [Snyk MCP Server](https://github.com/snyk/snyk-mcp-server)
- [Security Best Practices](SECURITY_REPORT.md)

---

## 🤝 Contributing

When contributing:
1. Run all Snyk scans before committing
2. Fix any high/critical vulnerabilities
3. Document security decisions
4. Update security reports

---

## 📝 License

This is a demonstration project for educational purposes.

---

**🔒 Built with Security at Inception using Snyk MCP**

**Status:** ✅ Production Ready - All critical/high vulnerabilities resolved
