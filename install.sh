#!/bin/bash
# Citation Verification Skill Installer for Claude Code

set -e

SKILL_NAME="citation-verification"
INSTALL_DIR="$HOME/.claude/skills/$SKILL_NAME"
REPO_URL="https://raw.githubusercontent.com/SteadfastAsArt/citation-verification-skill/main"

echo "📦 Installing Citation Verification Skill..."

# Create skills directory
mkdir -p "$INSTALL_DIR"

# Download SKILL.md
echo "⬇️  Downloading skill file..."
curl -fsSL "$REPO_URL/SKILL.md" -o "$INSTALL_DIR/SKILL.md"

# Check if paper-ladder is installed
if ! python3 -c "import paper_ladder" 2>/dev/null; then
    echo "⚠️  paper-ladder not found. Installing..."
    pip3 install paper-ladder || {
        echo "❌ Failed to install paper-ladder. Please install manually:"
        echo "   pip install paper-ladder"
        exit 1
    }
fi

echo "✅ Citation Verification Skill installed successfully!"
echo ""
echo "📍 Location: $INSTALL_DIR/SKILL.md"
echo ""
echo "🚀 Usage in Claude Code:"
echo "   Ask: 'Verify these citations: ...'"
echo "   Or invoke directly: /citation-verification"
echo ""
echo "🔍 Verify installation:"
echo "   Ask Claude: 'Do you have the citation-verification skill?'"
