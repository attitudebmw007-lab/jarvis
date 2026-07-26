#!/bin/bash
# Setup script for JARVIS - One-command installation

echo "=================================================="
echo "  🤖 JARVIS - AI Assistant Setup"
echo "=================================================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "  Python $python_version detected"
echo ""

# Create virtual environment
echo "✓ Creating virtual environment..."
python3 -m venv venv
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi
echo ""

# Upgrade pip
echo "✓ Upgrading pip..."
pip install --upgrade pip
echo ""

# Install requirements
echo "✓ Installing requirements..."
pip install -r requirements.txt
echo ""

# Setup environment file
echo "✓ Setting up environment..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "  ⚠️  Created .env file - Please add your OpenAI API key"
else
    echo "  ✓ .env file already exists"
fi
echo ""

# Create necessary directories
echo "✓ Creating directories..."
mkdir -p logs
mkdir -p data
mkdir -p screenshots
echo ""

echo "=================================================="
echo "  ✅ Setup Complete!"
echo "=================================================="
echo ""
echo "📝 Next steps:"
echo "  1. Edit .env and add your OpenAI API key"
echo "  2. Run: python launch.py"
echo ""
echo "🔗 Get your API key from:"
echo "  https://platform.openai.com/api-keys"
echo ""
