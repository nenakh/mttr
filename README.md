# MATTER

MATTER is a CLI-based tool that uses physical matter as a metaphor for organizing cognitive units, processes, and relationships. At its core, MATTER recognizes that various knowledge work activities (documenting, memorizing, referencing, and accomplishing tasks) are fundamentally manifestations of the same thing: text with attributes and relations. The system's power comes from this unifying concept, treating these different activities not as separate domains requiring different tools, but as variations in how we interact with fundamentally similar objects.

## Core Philosophy

The system uses "physical matter" as a metaphor for nonphysical, primarily cognitive units and processes. This is reflected in the nonstandard, deliberately idiosyncratic language used to describe objects, their relationships, and the actions that can be performed on them.

### Comparison with Other Software

While applications like Obsidian, LogSeq, and similar tools offer valuable ways to interact with files, choosing any specific application inherently limits certain possibilities while enabling others. MATTER aims to avoid these limitations by providing a more flexible, lower-level approach to knowledge organization. Rather than prescribing specific workflows or treating different activities (like note-taking and task management) as separate domains, it provides fundamental building blocks that users can combine in ways that suit their needs.

## Core Concepts

### Base Objects

- **mote**
  - The most basic, "indivisible" unit
  - Represents a single unit of text with attributes
  - The true dimensions of any mote are left to user discretion
  - Format: Clean, uncluttered text (typically Markdown) with separate YAML metadata
  - Type determined by attributes: document, memorize, reference, or accomplish

- **mass**
  - Any aggregate of motes and other masses
  - Structure determined by the bonds between components
  - Can represent various organizational concepts across all activity types

- **bond**
  - Connections between any two objects (motes-motes, masses-masses, or motes-masses)
  - Treated as first-class objects with their own properties
  - Multiple bonds can exist between any object pair, each representing different relationship contexts
  - Stored in YAML metadata, keeping content files clean and flexible

### Multiple Bonds: A Key Feature

MATTER's handling of bonds sets it apart from other tools:
- Any two objects can share multiple distinct relationships
- Each bond can represent a different context or type of relationship
- Bonds are stored entirely in metadata, allowing for:
  - Clean, uncluttered content files
  - Rich relationship metadata without compromising readability
  - Easy linking of any file type without modifying content
  - Flexible relationship types that can be added or modified without touching content
  - Multiple organizational schemes operating simultaneously

### Properties

Every object (motes, masses, and bonds) can have multiple properties that determine their function and behavior. Two key properties unique to bonds shape the structure of masses:

- **dense** (true/false)
  - Determines how tightly bound components are
  - Affects how objects are treated in operations

- **ordered** (true/false)
  - Determines if sequence matters
  - Influences how objects are processed and displayed

This creates four fundamental relationship types:

1. **Ordered and Dense**
   - Document: Composite notes with tight narrative flow
   - Memorize: Sequential, tightly related cards
   - Accomplish: Interdependent task clusters
   - Reference: Structured source material analysis

2. **Ordered but Sparse**
   - Document: Sequential ideas with loose connections
   - Memorize: Learning sequences
   - Accomplish: Sequential but independent tasks
   - Reference: Timeline-based references

3. **Dense but Unordered**
   - Document: Related notes without sequence
   - Memorize: Themed study materials
   - Accomplish: Related but flexible-order tasks
   - Reference: Thematically grouped sources

4. **Sparse and Unordered**
   - Document: Loosely linked notes
   - Memorize: Generally related study items
   - Accomplish: Independent tasks
   - Reference: Loosely related sources

### YAML-based Metadata

Metadata is deliberately separated from content files for:
- Cleaner writing experience without inline links or markers
- More flexible metadata application
- Ability to add metadata to diverse file types
- Enhanced querying and manipulation capabilities
- Support for multiple simultaneous organizational schemes

Example metadata structure:
```yaml
# mote.yaml
type: document  # or memorize, reference, accomplish
content_file: content.md
properties:
  created: 2024-02-20
  modified: 2024-02-20
  tags: []
bonds:
  - id: bond_123
    target: mote_456
    properties:
      dense: true
      ordered: true
      context: "continues from"
  - id: bond_124
    target: mote_456
    properties:
      dense: false
      ordered: false
      context: "related concept"
```

## Core Functions

### System Operations

```bash
mttr coalesce   # Initialize a directory as a MATTER space
  --connect     # Connect with other spaces
  --import      # Import existing files
  --template    # Specify metadata templates

mttr form       # Create and modify objects
  --mote       # Create atomic unit
  --mass       # Create collection
  --bond       # Create relationship
  --type       # Specify object type
  --properties # Set object properties

mttr void       # Remove or break down objects
  --dissolve   # Break mass into components
  --clean      # Remove orphaned metadata
  --preserve   # Keep content while removing structure

mttr reveal     # Show relationships and launch interactions
  --bonds      # Show connections
  --path       # Trace path between objects
  --context    # Filter by relationship context
  --visualize  # Generate network visualization
```

### Activity-Specific Operations

Different activities (document, memorize, reference, accomplish) are handled through property variations rather than separate commands:

```bash
# Creating a document mote
mttr form --mote --type document

# Creating a flashcard
mttr form --mote --type memorize

# Creating a reference entry
mttr form --mote --type reference

# Creating a task
mttr form --mote --type accomplish

# Creating a mass of related items
mttr form --mass --dense true --ordered false
```

## File Organization

```plaintext
~/.matter/
  objects/
    motes/
      <uuid>/
        content.md     # Clean, uncluttered content
        metadata.yaml  # Properties, bonds, and attributes
    masses/
      <uuid>/
        metadata.yaml  # Mass properties and components
    bonds/
      <uuid>/
        metadata.yaml  # Bond properties and connected objects
  indexes/
    by-type/        # Activity type lookups
    by-tag/         # Tag-based organization
    temporal/       # Time-based organization
  templates/        # Templates for different activity types
  spaces/           # Connected MATTER spaces
```

## Implementation Notes

### Content Management
- Content files remain clean and readable
- No inline links or special syntax
- All relationships handled through metadata
- Standard Markdown for content
- Version control through Git

### Relationship Management
- Multiple bonds between objects
- Rich metadata for each bond
- Context-aware relationships
- Flexible organization schemes
- Path tracing and discovery

### Future Development
- Query language for relationship exploration
- Visualization tools for network navigation
- Plugin system for extended functionality
- Integration with external tools
- Import/export capabilities
- Backup and synchronization options

## Capabilities

MATTER aims to:
- Provide a unified approach to managing cognitive work
- Handle different activity types as variations of the same fundamental unit
- Enable multiple simultaneous organizational schemes through rich bond metadata
- Maintain clean, uncluttered content files while supporting complex relationships
- Reveal connections in useful and interesting ways

## Network Visualization

Rather than attempting to visualize entire networks, which can be overwhelming and of limited utility, MATTER focuses on systematic exploration of connections:
- Trace specific paths between objects
- Filter relationships by context
- Form new masses from discovered paths
- Explore connections through different lenses
- Focus on relevant subsets of the network

Through this approach, MATTER helps users discover and understand connections while avoiding the cognitive overhead of complete network visualization.