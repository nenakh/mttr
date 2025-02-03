# MTTR - Matter-based Knowledge Organization System

## Overview

MTTR is a command-line knowledge organization system that uses physical matter as its core metaphor. This unconventional approach aims to break traditional thought patterns and enable novel approaches to knowledge management.

## Core Concepts

### Base Objects

- `shard` - Atomic unit of knowledge (traditional note)
  - Properties: title, content, tags, created, modified
  - Format: Markdown with YAML frontmatter

- `grain` - Unit of learning (flashcard)
  - Properties: question, answer, type, difficulty
  - Types: simple, cloze, occlude, principle, incremental
  - Supports spaced repetition learning

- `chunk` - Unit of action (task)
  - Properties: description, due date, priority, status
  - Status: formed, shaped, settled, dissolved
  - Supports workload tracking and dependencies

- `stuff` - External material (source)
  - Properties: type, location, citation info
  - Supports: PDF, EPUB, HTML, etc.

### Collections

Collections are defined by three core properties:

```yaml
collection:
  organization: explicit | implicit   # How the collection is formed
  ordering: ordered | unordered      # Whether sequence matters
  cohesion: tight | loose           # How closely items are related
```

Standard collection types:

- `clump` - Ordered composite object
  - organization: explicit
  - ordering: ordered
  - cohesion: tight
  - Example: Research paper composed of multiple shards

- `pile` - Non-exclusive collection
  - organization: explicit
  - ordering: unordered
  - cohesion: loose
  - Objects can belong to multiple piles

- `strand` - Hierarchical sequence
  - organization: explicit
  - ordering: ordered
  - cohesion: loose
  - Similar to Zettelkasten Folgezettel

- `bulk` - Emergent collection
  - organization: implicit
  - ordering: unordered
  - cohesion: loose
  - Generated through content analysis

### Connections

- `bond` - Relationship between objects
  - Properties: type, strength, direction
  - Types: reference, depends, supports, contradicts

## Core Functions

### System Initialization

```bash
mttr crystallize .              # Initialize directory as mttr workspace
```

### Object Creation and Manipulation

```bash
mttr form [options] <target>
  --shard    Create note
  --grain    Create flashcard
  --chunk    Create task
  --stuff    Import source
  --clump    Create composite
  --pile     Create collection
  --strand   Create sequence
  --bulk     Define emergent group
  --bond     Create connection
```

### Object Analysis

```bash
mttr reveal [options] <object>
  --bonds    Show connections
    --self   From this object
    --other  To this object
    --depth  Connection depth
  --orphans  Show isolated objects
  --strands  Show hierarchical sequences
  --similar  Find related content
  --stats    Show metadata statistics
```

### Path Exploration

```bash
mttr trace [options] <start> [end]
  --depth    Maximum path length
  --via      Preferred node types
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
mttr study [options] <grain|pile>
  --due        # Show only due cards
  --new        # Show only new cards
  --difficult  # Show cards marked difficult
```

### Task Management

```bash
mttr process [options] <chunk|clump>
  --status    # Update status
  --priority  # Set priority
  --estimate  # Set time estimate
```

## File Organization

```plaintext
~/.mttr/
  objects/
    <uuid>/
      content.md      # Primary content
      metadata.yaml   # Metadata and references
  indexes/
    by-type/         # Type-based lookups
    by-tag/          # Tag-based lookups
    temporal/        # Time-based lookups
  relationships/     # Connection definitions
    bonds/
    clumps/
    piles/
    strands/
  templates/         # Templates for different object types
```

## Metadata Structures

### Base Object Metadata

```yaml
id: 550e8400-e29b-41d4-a716-446655440000
type: shard
title: "Example Note"
created: 2025-02-03T14:30:00Z
modified: 2025-02-03T14:30:00Z
tags: ["research", "ideas"]
bonds:
  - id: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
    type: reference
    context: "Supports main argument"
```

### Grain Metadata

```yaml
type: grain
state: active | dormant
intervals: [1, 3, 7, 14, 30, 90]
history:
  - date: 2025-02-03
    result: good | again | hard
    interval: 7
next_due: 2025-02-10
difficulty: 0.3
stability: 0.8
```

### Chunk Metadata

```yaml
type: chunk
status: formed | shaped | settled | dissolved
workload: 3h
priority: high
subtasks:
  - id: chunk123
    workload: 1h
  - id: chunk456
    workload: 2h
aggregates:
  total_workload: 6h
  completion: 33%
dependencies:
  - id: chunk789
    type: blocks | suggests
```

### Collection Metadata

```yaml
type: clump
collection:
  organization: explicit
  ordering: ordered
  cohesion: tight
components:
  - id: chunk123
    type: chunk
  - id: chunk456
    type: chunk
aggregates:
  workload: 5h      # Sum of component workloads
  priority: high    # Highest priority of components
  completion: 60%   # Average completion of components
  due: 2025-02-10  # Earliest due date of components
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
   - Custom object type definitions
   - Complex query language
   - Integration hooks for external tools
   - Web interface for visualization
   - Collaboration features
