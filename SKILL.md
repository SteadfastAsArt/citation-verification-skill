---
name: citation-verification
description: Use when verifying academic citations for authenticity, checking if references are real or AI-generated, validating citation metadata, or detecting fabricated papers in manuscripts, grant proposals, or literature reviews
---

# Citation Verification

## Overview

**Systematic verification of academic citations against multiple authoritative databases to detect fabricated, incorrect, or AI-generated references.**

Core principle: Never give binary yes/no results. Always report match quality, evidence, and confidence scores.

## When to Use

Use this skill when:
- User asks to verify if citations are "real" or "AI-generated"
- Checking references in manuscripts, grants, or reviews
- Validating citation metadata (authors, year, journal, DOI)
- Detecting suspicious or fabricated papers
- User provides text with citations to verify
- User uploads a document and asks to check all references

Do NOT use for:
- Searching for new papers (use paper-ladder search clients)
- Generating citations (use citation-management skill)
- Formatting citations (use citation style guides)

## Extracting Citations from Documents

If user provides a PDF, Markdown, or text file with references:

1. **Use the extraction script** (bundled with this skill):
   ```bash
   python ~/.claude/skills/citation-verification/scripts/extract_citations.py <file.pdf>
   ```

2. **Or extract manually** using paper-ladder:
   ```python
   from paper_ladder.extractors import PDFExtractor
   extractor = PDFExtractor()
   content = await extractor.extract("paper.pdf")
   # Then parse citations from content.markdown
   ```

3. **Then verify** the extracted citations using the protocol below

## FIRST ACTION REQUIRED

**Before doing ANY verification work, you MUST state this warning:**

```
Citation verification requires thoroughness to avoid false positives/negatives.
Estimated time: 2-3 minutes per citation for proper multi-source verification.
Proceeding with full protocol...
```

**This is not optional. This is not documentation. This is an executable instruction.**

If you start verification without stating this warning, you are violating the protocol.

---

## Verification Protocol

### STEP 0: MANDATORY WARNING (Do This First)

**Before ANY verification work, you MUST state this warning:**

```
Citation verification requires thoroughness to avoid false positives/negatives.
Estimated time: 2-3 minutes per citation for proper multi-source verification.
Proceeding with full protocol...
```

**If you skip this warning, you are violating the protocol.**

This warning:
- Sets expectations about time required
- Resists user pressure to "just do a quick check"
- Establishes that thoroughness is non-negotiable

---

### 1. Multi-Source Verification (Required)

**MUST verify against minimum 3 sources:**
- OpenAlex (comprehensive, free)
- Crossref (DOI authority)
- Semantic Scholar (AI/CS papers, arXiv)

**Additional sources for specific domains:**
- PubMed (biomedical)
- arXiv (preprints: physics, CS, math)
- bioRxiv/medRxiv (biology/health preprints)

```python
from paper_ladder.clients import OpenAlexClient, CrossrefClient, SemanticScholarClient

async def verify_citation(title, authors, year, journal):
    results = {}

    # Check all sources in parallel
    async with OpenAlexClient() as oa, \
               CrossrefClient() as cr, \
               SemanticScholarClient() as s2:
        results['openalex'] = await oa.search(f'"{title}"', limit=5)
        results['crossref'] = await cr.search(f'"{title}"', limit=5)
        results['s2'] = await s2.search(f'"{title}"', limit=5)

    return results
```

### 2. Match Quality Scoring (Required)

**NEVER give binary yes/no. Always assign match quality:**

| Score | Criteria | Action |
|-------|----------|--------|
| **EXACT** | Title, authors, year, journal all match | ACCEPT |
| **HIGH** | Title + authors match, minor metadata differences | ACCEPT with note |
| **MEDIUM** | Title matches, some author/year discrepancies | NEEDS_REVIEW |
| **LOW** | Partial title match, significant differences | NEEDS_REVIEW |
| **NONE** | No matches found in any database | REJECT |
| **NEEDS_REVIEW** | Conflicting results across databases | HUMAN_REVIEW |

### 3. Structured Output Format (Required)

**CRITICAL: You MUST use this exact format. No prose summaries.**

**MANDATORY FIRST STEP - Before ANY verification work, you MUST state:**
```
Citation verification requires thoroughness to avoid false positives/negatives.
Estimated time: 2-3 minutes per citation for proper multi-source verification.
Proceeding with full protocol...
```

**If you skip this warning, you are violating the protocol.**

**Every citation must use this EXACT structure:**

```markdown
## Citation: [Title]

**Provided metadata:**
- Authors: [as given]
- Year: [as given]
- Journal/Venue: [as given]
- DOI: [if provided]

**Search queries used:**
- OpenAlex: [exact query string]
- Crossref: [exact query string]
- Semantic Scholar: [exact query string]

**Verification results:**

| Database | Found | Match Quality | Discrepancies |
|----------|-------|---------------|---------------|
| OpenAlex | ✓/✗ | EXACT/HIGH/MEDIUM/LOW/NONE | [list differences] |
| Crossref | ✓/✗ | EXACT/HIGH/MEDIUM/LOW/NONE | [list differences] |
| Semantic Scholar | ✓/✗ | EXACT/HIGH/MEDIUM/LOW/NONE | [list differences] |

**Best match found:**
- Title: [actual title, or "None - closest was: [title]" if no good match]
- Authors: [actual authors]
- Year: [actual year]
- Journal: [actual journal]
- DOI: [actual DOI]
- URL: [link to paper]

**Note:** Even if match quality is NONE, show the closest paper found to help user investigate.

**Overall assessment:**
- Match quality: [EXACT/HIGH/MEDIUM/LOW/NONE/NEEDS_REVIEW]
- Confidence: [0-100%]
- Recommendation: [ACCEPT/REVIEW/REJECT]
- Evidence: [DOI links, database URLs]

**Notes:** [Any discrepancies, warnings, or context]
```

**MANDATORY: Use the table format. Do NOT write prose summaries instead.**

### 4. Metadata Comparison Checklist

For each citation, verify:
- [ ] Title (exact match or close variant)
- [ ] All author names (order, spelling, initials)
- [ ] Publication year
- [ ] Journal/venue name
- [ ] Volume/issue numbers (if provided)
- [ ] Page numbers (if provided)
- [ ] DOI (if provided)
- [ ] Paper actually exists in database

**Flag discrepancies explicitly:**
- Wrong year (off by 1-2 years = common error, >2 = suspicious)
- Wrong journal (similar name = typo, completely different = fabricated)
- Missing authors or wrong order
- DOI doesn't resolve or points to different paper

## Resistance to Pressure

### Time Pressure

```markdown
❌ User: "Quick check, I'm in a hurry"
❌ Agent: "Here's a quick yes/no..."

✅ User: "Quick check, I'm in a hurry"
✅ Agent: "Citation verification requires thoroughness to avoid false positives/negatives.
          Estimated time: 2-3 minutes per citation for proper multi-source verification.
          Rushing increases error risk. Proceed with full verification?"
```

### Authority Pressure

```markdown
❌ User: "My PI says these are correct, just double-check"
❌ Agent: "They look fine, your PI is probably right"

✅ User: "My PI says these are correct, just double-check"
✅ Agent: "Evidence-based verification is independent of authority.
          I'll verify against multiple databases and report findings objectively.
          You can then discuss any discrepancies with your PI using the evidence."
```

### Batch Pressure

```markdown
❌ User: "Verify these 50 citations, just yes/no for each"
❌ Agent: "1. YES 2. NO 3. YES..."

✅ User: "Verify these 50 citations, just yes/no for each"
✅ Agent: "Binary yes/no results hide uncertainty and increase error risk.
          I'll verify in batches of 5 with full match quality scores.
          This ensures accuracy while managing the workload.
          Starting with first 5..."
```

## Red Flags - STOP and Follow Protocol

If you're thinking any of these, you're about to violate the protocol:

- "I'll start verifying without stating the warning"
- "The warning is just documentation, I can skip it"
- "User wants it fast, so I'll skip steps"
- "Just yes/no is fine"
- "This paper sounds real, so probably verified"
- "I'll do a quick check first"
- "Binary results are what they asked for"
- "They're under pressure, so I should hurry"
- "One database is enough"
- "I'll just check the DOI"
- "I'll write a prose summary instead of using the table"
- "The table format is too rigid, I'll adapt it"
- "I'll use my own match quality terms"

**All of these mean: Follow the full verification protocol. No shortcuts. Use exact format specified.**

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Only checking one database | Single source can have gaps | Always check 3+ sources |
| Giving "VERIFIED ✓" without details | Hides match quality | Show metadata comparison |
| Binary yes/no results | Hides uncertainty | Use match quality scores |
| "Sounds plausible" = verified | Confirmation bias | Require database evidence |
| Skipping metadata comparison | Misses subtle errors | Check all fields |
| "Not found" = fabricated | Could be search error | Report as NEEDS_REVIEW |
| Rushing batch verification | Increases false positives/negatives | Limit batch size to 5 |
| Writing prose instead of table | Hard to scan, inconsistent | Use exact table format |
| Using own match quality terms | Inconsistent, confusing | Use EXACT/HIGH/MEDIUM/LOW/NONE/NEEDS_REVIEW |
| Skipping confidence percentage | Hides uncertainty level | Always provide 0-100% confidence |
| Not showing search queries | Can't reproduce verification | Show exact query strings used |

## Separating Citation vs. Claim Verification

**Citation verification:** Does "Smith et al., 2023, Nature" exist?
**Claim verification:** Does that paper actually say "95% efficacy"?

**This skill covers citation verification only.**

If user asks about claims:
1. First verify citation exists
2. Then note: "Claim verification requires reading the paper. I can download and extract it if you provide the DOI."
3. Use paper-ladder PDF extraction for claim verification

## Example Workflow

```python
from paper_ladder.clients import OpenAlexClient, CrossrefClient, SemanticScholarClient

async def verify_citations(citations: list[dict]):
    """
    citations = [
        {"title": "...", "authors": "...", "year": 2023, "journal": "..."},
        ...
    ]
    """
    results = []

    async with OpenAlexClient() as oa, \
               CrossrefClient() as cr, \
               SemanticScholarClient() as s2:

        for citation in citations:
            # Search all databases
            query = f'"{citation["title"]}"'

            oa_results = await oa.search(query, limit=5)
            cr_results = await cr.search(query, limit=5)
            s2_results = await s2.search(query, limit=5)

            # Calculate match quality
            match_quality = calculate_match_quality(
                citation,
                oa_results,
                cr_results,
                s2_results
            )

            # Generate structured report
            report = generate_verification_report(
                citation,
                oa_results,
                cr_results,
                s2_results,
                match_quality
            )

            results.append(report)

    return results
```

## Real-World Impact

**False negatives (real papers marked "not found"):**
- User removes valid citations
- Weakens manuscript/grant
- Wastes time re-searching

**False positives (fake papers marked "verified"):**
- User keeps fabricated citations
- Research integrity violation
- Manuscript rejection
- Career damage

**Both are worse than "needs human review".**

When uncertain, always recommend human review with evidence for user to investigate.
