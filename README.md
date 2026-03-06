# Citation Verification Skill for Claude Code

A systematic skill for verifying academic citations against multiple authoritative databases to detect fabricated, incorrect, or AI-generated references.

## What This Skill Does

- **Detects AI-generated fake citations** by cross-checking multiple academic databases
- **Validates citation metadata** (authors, year, journal, DOI) for accuracy
- **Provides structured verification reports** with match quality scores and confidence levels
- **Resists pressure shortcuts** (time pressure, authority bias, batch processing)
- **Generates reproducible evidence trails** for every citation checked

## Installation

### Quick Install (Recommended)

```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills/citation-verification

# Download the skill
curl -o ~/.claude/skills/citation-verification/SKILL.md \
  https://raw.githubusercontent.com/SteadfastAsArt/citation-verification-skill/main/SKILL.md
```

### Manual Install

1. Create directory: `mkdir -p ~/.claude/skills/citation-verification`
2. Copy `SKILL.md` to `~/.claude/skills/citation-verification/SKILL.md`
3. Restart Claude Code

### Verify Installation

In Claude Code, ask:
```
Do you have the citation-verification skill?
```

Claude should confirm the skill is loaded.

## Usage

Simply ask Claude Code to verify citations:

```
Verify these citations:
1. Smith et al. (2023). "Transformer models for protein folding." Nature Machine Intelligence, 5(2), 123-135.
2. Zhang, L. (2024). "Quantum computing applications in drug discovery." arXiv:2401.12345.
```

Claude will automatically:
1. Check 3+ academic databases (OpenAlex, Crossref, Semantic Scholar)
2. Compare metadata across sources
3. Assign match quality scores (EXACT/HIGH/MEDIUM/LOW/NONE/NEEDS_REVIEW)
4. Provide confidence percentages
5. Generate structured verification report with evidence

## Requirements

This skill works best with the [paper-ladder](https://github.com/SteadfastAsArt/paper-ladder) library, which provides:
- Multi-source academic database clients
- Async search capabilities
- Unified Paper data model

Install paper-ladder:
```bash
pip install paper-ladder
# or
uv pip install paper-ladder
```

## Features

### Multi-Source Verification
- OpenAlex (comprehensive, free)
- Crossref (DOI authority)
- Semantic Scholar (AI/CS papers, arXiv)
- PubMed (biomedical)
- arXiv, bioRxiv, medRxiv (preprints)

### Match Quality Scoring
- **EXACT**: All metadata matches perfectly
- **HIGH**: Title + authors match, minor discrepancies
- **MEDIUM**: Title matches, some author/year differences
- **LOW**: Partial match, significant differences
- **NONE**: No matches found
- **NEEDS_REVIEW**: Conflicting results, requires human judgment

### Pressure Resistance
The skill enforces thoroughness even when users request:
- "Quick check" (resists time pressure)
- "Just yes/no" (always provides detailed reports)
- Batch processing (limits to 5 citations at a time)

### Structured Output
Every citation gets:
- Provided metadata
- Search queries used
- Database verification table
- Best match found
- Overall assessment (match quality, confidence, recommendation)
- Evidence links

## Example Output

```markdown
## Citation: Attention Is All You Need

**Provided metadata:**
- Authors: Vaswani et al.
- Year: 2017
- Journal/Venue: NeurIPS

**Search queries used:**
- OpenAlex: "Attention Is All You Need"
- Crossref: "Attention Is All You Need"
- Semantic Scholar: "Attention Is All You Need"

**Verification results:**

| Database | Found | Match Quality | Discrepancies |
|----------|-------|---------------|---------------|
| OpenAlex | ✓ | EXACT | None |
| Crossref | ✓ | EXACT | None |
| Semantic Scholar | ✓ | EXACT | None |

**Overall assessment:**
- Match quality: EXACT
- Confidence: 100%
- Recommendation: ACCEPT
- Evidence: [DOI link], [Semantic Scholar link]
```

## Use Cases

- **Manuscript review**: Verify references before submission
- **Grant proposals**: Check citations for accuracy
- **Literature reviews**: Validate sources
- **Peer review**: Detect fabricated references
- **Academic integrity**: Identify AI-generated citations

## Development

This skill was created using Test-Driven Development (TDD) for documentation:
1. **RED**: Tested baseline behavior without skill (identified shortcuts and rationalizations)
2. **GREEN**: Wrote skill to address specific failures
3. **REFACTOR**: Strengthened enforcement through multiple test iterations

See test scenarios in `/tests/` directory.

## Contributing

Contributions welcome! Please:
1. Follow TDD methodology (test before writing)
2. Maintain token efficiency (<500 words for skill content)
3. Add test scenarios for new features
4. Update README with new capabilities

## License

MIT License - see LICENSE file

## Related Projects

- [paper-ladder](https://github.com/SteadfastAsArt/paper-ladder) - Academic paper search library
- [Claude Code](https://github.com/anthropics/claude-code) - Official Anthropic CLI

## Support

- Issues: [GitHub Issues](https://github.com/SteadfastAsArt/citation-verification-skill/issues)
- Discussions: [GitHub Discussions](https://github.com/SteadfastAsArt/citation-verification-skill/discussions)

---

**Repository**: https://github.com/SteadfastAsArt/citation-verification-skill
