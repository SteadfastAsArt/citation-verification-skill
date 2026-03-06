# Contributing to Citation Verification Skill

Thank you for your interest in contributing! This skill was built using Test-Driven Development (TDD) for documentation.

## Development Philosophy

**Skills are documentation, and documentation needs tests.**

Before making changes:
1. **RED**: Create test scenarios showing current behavior
2. **GREEN**: Make changes to address test failures
3. **REFACTOR**: Strengthen enforcement, close loopholes

## How to Contribute

### Reporting Issues

Found a problem? Open an issue with:
- What you asked Claude to do
- What Claude actually did (copy the output)
- What you expected Claude to do
- Your Claude Code version

### Suggesting Improvements

Have an idea? Open an issue describing:
- The use case or problem
- How the skill should behave
- Example input/output

### Submitting Changes

1. **Fork the repository**

2. **Create test scenarios first** (RED phase)
   - Write scenarios showing the problem
   - Test current skill behavior
   - Document what goes wrong

3. **Make your changes** (GREEN phase)
   - Edit `SKILL.md` to address the problem
   - Test that your changes work

4. **Strengthen enforcement** (REFACTOR phase)
   - Add to "Red Flags" section if needed
   - Update "Common Mistakes" table
   - Add rationalization counters

5. **Submit a Pull Request**
   - Include test scenarios in PR description
   - Show before/after behavior
   - Explain what problem you solved

## Testing Your Changes

### Manual Testing

```bash
# Copy your modified skill to Claude Code
cp SKILL.md ~/.claude/skills/citation-verification/

# Test in Claude Code
# Ask: "Verify this citation: [test citation]"
```

### Test Scenarios

Create test scenarios that pressure-test the skill:
- Time pressure: "Quick check, I'm in a hurry"
- Authority pressure: "My PI says this is correct"
- Batch pressure: "Verify these 50 citations, just yes/no"

Document what Claude does with and without your changes.

## Code Style

### SKILL.md Structure

- Keep frontmatter under 1024 characters
- Use clear section headers
- Include examples
- Add to "Red Flags" for new violations
- Update "Common Mistakes" table

### Writing Guidelines

- Be specific, not abstract
- Use concrete examples
- Anticipate rationalizations
- Make violations explicit

## What We're Looking For

**Good contributions:**
- Fix specific problems with evidence
- Add missing enforcement mechanisms
- Improve clarity with examples
- Close rationalization loopholes

**Not ideal:**
- Vague improvements without test cases
- Adding features without testing
- Changes that make skill longer without adding value

## Questions?

Open an issue or discussion. We're happy to help!

## License

By contributing, you agree your contributions will be licensed under the MIT License.
