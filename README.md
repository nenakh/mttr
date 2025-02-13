# MTTR - Matter-based Knowledge Organization System

## Overview

MTTR is a command-line knowledge organization system that uses physical matter as its core metaphor. This unconventional approach breaks traditional thought patterns and enables novel approaches to knowledge management through three fundamental concepts: motes (indivisible units), masses (collections of units), and bonds (relationships between objects).

## Core Concepts

### Base Objects

- `mote` - Indivisible unit of knowledge, task, or learning
  - Properties determine function (note-like, flashcard-like, task-like)
  - Format: Markdown with YAML frontmatter
  - Can be enriched with various property sets

- `mass` - Collection of motes or other masses
  - Characterized by two core properties:
    - `dense` (true/false): Whether components are tightly bound
    - `ordered` (true/false): Whether sequence matters
  - Four fundamental types:
    - Note-like (dense + ordered): Sequential reading, tight narrative flow
    - Folder-like (sparse + disordered): Loose grouping, flexible organization
    - Idea chain (sparse + ordered): Sequential but loose, connected thoughts
    - Default dense (dense + disordered): Tightly related, no specific sequence

- `bond` - Explicit relationship between objects
  - Independent objects that can be modified separately
  - Multiple bonds can exist between the same objects
  - Properties include type, strength, directionality
  - Visual properties for network representation

### Properties

Properties determine what can be done with an object. Objects can have multiple property sets:

```yaml
# Note-like properties
content: markdown    # Primary content
tags: []            # For organization
modified: datetime  # Last modified time

# Mass properties
properties:
  dense: true/false     # Whether components are tightly bound
  ordered: true/false   # Whether sequence matters
components:
  - id: mote123
    type: mote
    sequence: 1  # Only if ordered: true

# Bond properties
properties:
  category: reference/dependency/contradiction/support
  strength: 0.8
  bidirectional: true/false
  visual:
    color: "#4A90E2"
    thickness: 2
    style: "solid"
objects:
  - id: obj_x
    role: source
  - id: obj_y
    role: target
```

### Link Management

MTTR supports both inline and metadata-based linking:

1. Creation using familiar wiki-style brackets:
   ```markdown
   This is a reference to [[another_note]]
   ```

2. Optional scrubbing to clean text while preserving links:
   ```yaml
   # After mttr scour --links
   links:
     - target: another_note
       bond: bond_123
       reference:
         text: "another_note"
         context: "reference to {text}"
         original_markup: "[[another_note]]"
   ```

3. Link integrity checking and repair options if text changes

## Core Functions

### System Initialization

```bash
mttr crystallize .              # Initialize directory as mttr workspace
```

### Object Creation

```bash
mttr form --mote [options]     # Create atomic unit
mttr form --mass [options]     # Create collection
  --dense                      # Make tightly bound
  --ordered                    # Make sequence matter
mttr form --bond [options]     # Create relationship
  --type <type>               # Set bond type
  --source <obj>              # Set source object
  --target <obj>              # Set target object
```

### Object Analysis

```bash
mttr reveal [options] <object>
  --bonds    Show connections
  --orphans  Show isolated objects
  --similar  Find related content
  --stats    Show metadata
```

### Link Management

```bash
mttr scour --links <object>    # Move brackets to metadata
mttr restore --links <object>  # Restore brackets in text
```

### Object Manipulation

```bash
mttr fuse [options] <objects...>    # Combine objects
mttr split [options] <object>       # Divide object
mttr scour [options] <object>       # Clean/normalize
```

## File Organization

```plaintext
~/.mttr/
  objects/
    motes/
      <uuid>/
        content.md      # Primary content
        metadata.yaml   # Metadata and properties
    masses/
      <uuid>/
        metadata.yaml   # Mass properties and components
    bonds/
      <uuid>/
        metadata.yaml   # Bond properties and objects
  indexes/
    by-type/         # Type-based lookups
    by-tag/          # Tag-based lookups
    temporal/        # Time-based lookups
  templates/         # Templates for different property sets
```

## Implementation Notes

1. File Management
   - All files maintain human-readable names
   - UUIDs only appear in metadata YAML files
   - File operations should occur through mttr framework
   - `reveal --orphans` helps identify detached files
   - Git handles version control

2. Content Handling
   - Primary content format is Markdown
   - Links can be inline or metadata-based
   - Link integrity checking on text changes
   - Media handling through Markdown renderer

3. Future Extensions
   - Plugin system for extending functionality
   - Custom property set definitions
   - Complex query language
   - Integration hooks for external tools
   - Web interface for visualization
   - Collaboration features