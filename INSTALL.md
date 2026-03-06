# Installation Guide

## Prerequisites

- Claude Code CLI installed
- Python 3.10+ (for paper-ladder library)
- Git (optional, for cloning)

## Method 1: Quick Install (Recommended)

```bash
# Create skills directory
mkdir -p ~/.claude/skills/citation-verification

# Download the skill
curl -o ~/.claude/skills/citation-verification/SKILL.md \
  https://raw.githubusercontent.com/SteadfastAsArt/citation-verification-skill/main/SKILL.md

# Install paper-ladder library
pip install paper-ladder
```

## Method 2: Git Clone

```bash
# Clone to skills directory
cd ~/.claude/skills
git clone https://github.com/SteadfastAsArt/citation-verification-skill.git citation-verification

# Install paper-ladder
pip install paper-ladder
```

## Method 3: Manual Download

1. Download `SKILL.md` from [GitHub](https://github.com/SteadfastAsArt/citation-verification-skill)
2. Create directory: `mkdir -p ~/.claude/skills/citation-verification`
3. Move `SKILL.md` to `~/.claude/skills/citation-verification/SKILL.md`
4. Install paper-ladder: `pip install paper-ladder`

## Verify Installation

Start Claude Code and ask:
```
Do you have the citation-verification skill?
```

Claude should respond confirming the skill is available.

## Troubleshooting

### Skill Not Found

Check skill location:
```bash
ls -la ~/.claude/skills/citation-verification/SKILL.md
```

Should show the file exists.

### Paper-Ladder Not Found

Install paper-ladder:
```bash
pip install paper-ladder
# or with uv
uv pip install paper-ladder
```

### Permission Issues

Ensure skills directory is readable:
```bash
chmod -R 755 ~/.claude/skills
```

## Updating

### Quick Install Method
```bash
curl -o ~/.claude/skills/citation-verification/SKILL.md \
  https://raw.githubusercontent.com/SteadfastAsArt/citation-verification-skill/main/SKILL.md
```

### Git Clone Method
```bash
cd ~/.claude/skills/citation-verification
git pull
```

## Uninstalling

```bash
rm -rf ~/.claude/skills/citation-verification
```

---

**Note**: Replace `SteadfastAsArt` with the actual GitHub username after repository creation.
