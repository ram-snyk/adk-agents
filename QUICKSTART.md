# Google ADK Agent Security Demo

## Quick Start Guide

This project demonstrates building a secure Google AI Development Kit (ADK) agent with comprehensive Snyk security scanning at every stage.

### Prerequisites

- Python 3.11+
- Docker
- Snyk account (for scanning)
- Google API key

### Step-by-Step: Secure Development

#### 1. **Setup Dependencies**
```bash
cd adk-agents
pip install -r requirements.txt
```

**Security Check:**
```bash
# Run SCA scan on dependencies
snyk test --file=requirements.txt
```

#### 2. **Run the Agent**
```bash
export GOOGLE_API_KEY="your-api-key"
python agent.py
```

**Security Check:**
```bash
# Run code scan
snyk code test agent.py
```

#### 3. **Build Container**
```bash
docker build -t adk-agent:latest .
```

**Security Check:**
```bash
# Scan container image
snyk container test adk-agent:latest
```

#### 4. **Deploy Infrastructure**
```bash
cd terraform
terraform init
terraform plan
```

**Security Check:**
```bash
# Scan IaC configurations
snyk iac test terraform/
snyk iac test k8s-deployment.yaml
```

### Project Structure

```
adk-agents/
├── agent.py                 # Main ADK agent implementation
├── requirements.txt         # Python dependencies (secured)
├── Dockerfile              # Container definition (hardened)
├── k8s-deployment.yaml     # Kubernetes manifests (secure)
├── terraform/              # Infrastructure as Code
│   └── main.tf            # GCP resources (encrypted, logged)
├── README.md              # This file
├── SECURITY_REPORT.md     # Comprehensive security analysis
└── .env.example           # Environment template

```

### Security Scanning Results

| Layer | Tool | Status |
|-------|------|--------|
| Dependencies | SCA | ✅ 0 issues |
| Source Code | SAST | ✅ 0 issues |
| Container | Container Scan | ✅ Fixed |
| Infrastructure | IaC Scan | ✅ 1 low accepted |

**Full Report:** See [SECURITY_REPORT.md](SECURITY_REPORT.md)

### Key Security Features

#### Application
- ✅ Type-safe function declarations
- ✅ Environment variable management
- ✅ Error handling and validation
- ✅ Structured logging capability

#### Container
- ✅ Non-root user execution
- ✅ Minimal base image
- ✅ Health checks
- ✅ Updated dependencies

#### Infrastructure
- ✅ Customer-managed encryption (KMS)
- ✅ Audit logging enabled
- ✅ Network policies
- ✅ Least privilege access
- ✅ Auto-scaling configured

### Example Usage

The agent provides two tools:

1. **Knowledge Base Search**
```
You: What's your shipping policy?
Agent: Standard shipping takes 5-7 business days...
```

2. **Order Status Check**
```
You: Check order ORD-12345
Agent: Your order has been shipped with tracking number 1Z999AA10123456784...
```

### Snyk MCP Integration

This project uses Snyk MCP server for automated security scanning:

```bash
# Authenticate
snyk auth

# Trust project directory
snyk_trust /path/to/project

# Run scans
snyk_sca_scan --path=/path --command=python3
snyk_code_scan --path=/path/to/file.py
snyk_container_scan --image=image:tag
snyk_iac_scan --path=/path/to/terraform
```

### CI/CD Integration

Add to your pipeline:

```yaml
# Example GitHub Actions
- name: Snyk Security Scan
  run: |
    snyk test --all-projects
    snyk code test
    snyk container test $IMAGE_NAME
    snyk iac test terraform/
```

### Compliance

This implementation aligns with:
- OWASP Top 10
- CIS Benchmarks
- NIST Cybersecurity Framework
- SOC 2 Type II
- ISO 27001

### Learn More

- [Google ADK Documentation](https://ai.google.dev/adk)
- [Snyk Documentation](https://docs.snyk.io/)
- [Security Report](SECURITY_REPORT.md)

### Contributing

When contributing:
1. Run all Snyk scans before committing
2. Fix any high/critical vulnerabilities
3. Document security decisions
4. Update SECURITY_REPORT.md

### License

This is a demonstration project for educational purposes.

---

**🔒 Built with Security at Inception using Snyk MCP**
