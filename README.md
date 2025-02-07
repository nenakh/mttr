# MTTR - Matter-based Knowledge Organization System

## Overview

MTTR is a command-line knowledge organization system that uses physical matter as its core metaphor. This unconventional approach breaks traditional thought patterns and enables novel approaches to knowledge management through two fundamental concepts: motes (indivisible units) and masses (collections of units).

## Core Concepts

### Base Objects

- `mote` - Indivisible unit of knowledge, task, or learning
  - Properties determine function (note-like, flashcard-like, task-like)
  - Format: Markdown with YAML frontmatter
  - Can be enriched with various property sets

- `mass` - Collection of motes or other masses
  - Properties aggregate from components
  - Supports flexible organization patterns
  - Enables emergent functionality

### Properties

Properties determine what can be done with an object. Objects can have multiple property sets:

```yaml
# Note-like properties
content: markdown    # Primary content
tags: []            # For organization
references: []      # Links to other objects
modified: datetime  # Last modified time

# Learning properties (flashcard-like)
pattern:
  type: simple|cloze|incremental
  question: string
  answer: string
learning:
  intervals: [1,3,7,14,30]
  next_review: datetime
  history: []
  difficulty: float

# Task properties
task:
  status: formed|shaped|settled|dissolved
  due: datetime
  priority: high|medium|low
  workload: duration
  dependencies: []

# Mass properties
collection:
  organization: explicit|implicit   # How the mass is formed
  ordering: ordered|unordered      # Whether sequence matters
  cohesion: tight|loose           # How closely items relate
components:
  - id: mote123
    type: mote
  - id: mass456
    type: mass
aggregates:
  workload: duration      # Sum of component workloads
  completion: percentage  # Average completion
  due: datetime          # Earliest due date
```

### Connections

- `bond` - Relationship between objects
  - Properties: type, strength, direction
  - Types: reference, depends, supports, contradicts

## Core Functions

### System Initialization

```bash
mttr crystallize .              # Initialize directory as mttr workspace
```

### Object Creation

```bash
mttr form [options]
  --mote     Create atomic unit
  --mass     Create collection
  --bond     Create connection
```

### Object Analysis

```bash
mttr reveal [options] <object>
  --bonds    Show connections
  --orphans  Show isolated objects
  --similar  Find related content
  --stats    Show metadata
```

### Path Exploration

```bash
mttr trace [options] <start> [end]
  --depth    Maximum path length
  --via      Preferred object types
  --sift     Filter criteria
```

### Object Manipulation

```bash
mttr fuse [options] <objects...>    # Combine objects
mttr split [options] <object>       # Divide object
mttr scour [options] <object>       # Clean/normalize
```

### Learning System

```bash
mttr study [options] <object>    # Works on objects with learning properties
  --due      Show only due items
  --new      Show only new items
```

### Task Management

```bash
mttr process [options] <object>   # Works on objects with task properties
  --status    Update status
  --priority  Set priority
  --estimate  Set time estimate
```

## File Organization

```plaintext
~/.mttr/
  objects/
    <uuid>/
      content.md      # Primary content
      metadata.yaml   # Metadata and properties
  indexes/
    by-type/         # Type-based lookups
    by-tag/          # Tag-based lookups
    temporal/        # Time-based lookups
  relationships/     # Connection definitions
    bonds/
    masses/
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
   - Media handling through Markdown renderer
   - Based on MarkdownPreview with potential modifications

3. Future Extensions
   - Plugin system for extending functionality
   - Custom property set definitions
   - Complex query language
   - Integration hooks for external tools
   - Web interface for visualization
   - Collaboration features