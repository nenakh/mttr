mttr/
├── pyproject.toml           # Project metadata and dependencies
├── README.md               # Project documentation
├── LICENSE                 # License file
├── .gitignore             # Git ignore file
├── src/
│   └── mttr/
│       ├── __init__.py    # Package initialization
│       ├── cli.py         # Command-line interface handling
│       ├── commands/      # Command implementations
│       │   ├── __init__.py
│       │   ├── form.py    # Object creation
│       │   ├── reveal.py  # Object analysis
│       │   ├── fuse.py    # Object combination
│       │   ├── split.py   # Object division
│       │   └── scour.py   # Object cleaning
│       ├── core/          # Core functionality
│       │   ├── __init__.py
│       │   ├── objects.py     # Base object implementations
│       │   ├── motes.py      # Mote-specific implementation
│       │   ├── masses.py     # Mass-specific implementation
│       │   ├── bonds.py      # Bond-specific implementation
│       │   └── workspace.py  # Workspace management
│       ├── templates/     # YAML templates
│       │   ├── global.yml
│       │   ├── mote/
│       │   │   ├── base.yml
│       │   │   ├── document.yml
│       │   │   ├── memorize.yml
│       │   │   ├── reference.yml
│       │   │   └── accomplish.yml
│       │   ├── mass.yml
│       │   └── bond.yml
│       └── utils/         # Utility functions
│           ├── __init__.py
│           ├── config.py      # Configuration handling
│           ├── templates.py   # Template processing
│           └── validators.py  # Input validation
├── tests/                 # Test directory
│   ├── __init__.py
│   ├── conftest.py       # Test configuration
│   ├── test_cli.py
│   ├── test_commands/
│   │   └── test_form.py
│   └── test_core/
│       └── test_objects.py
└── docs/                  # Documentation
    ├── commands.md        # Command reference
    ├── objects.md         # Object type reference
    └── templates.md       # Template reference

# Example command handling in cli.py:
import click

@click.group()
def cli():
    """MTTR - Matter-based Knowledge Organization System"""
    pass

@cli.command()
@click.option('--document', '-d', is_flag=True, help='Create a document mote')
@click.option('--memorize', '-m', is_flag=True, help='Create a memorization mote')
@click.option('--reference', '-r', is_flag=True, help='Create a reference mote')
@click.option('--accomplish', '-a', is_flag=True, help='Create a task mote')
@click.argument('source', required=False)
def form(document, memorize, reference, accomplish, source):
    """Create a new object"""
    # Implementation

@cli.command()
@click.argument('object_id')
@click.option('--bonds', is_flag=True, help='Show connections')
@click.option('--orphans', is_flag=True, help='Show isolated objects')
def reveal(object_id, bonds, orphans):
    """Analyze an object"""
    # Implementation

if __name__ == '__main__':
    cli()