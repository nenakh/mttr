# templates/global.yml
---
id: ${uuid}                 # Automatically generated UUID
created: ${timestamp}       # Creation timestamp
modified: ${timestamp}      # Last modified timestamp
tags: []                   # List of tags for organization

# templates/mote/base.yml
---
title: ""                  # Human-readable title
content: ""               # Primary content in markdown
type: ${type}              # One of: document, memorize, reference, accomplish
links: []                  # List of linked objects
location: ${path}         # Path within .mttr/objects/motes

# templates/mote/document.yml
---
format: markdown           # Content format
outline: false            # Whether this is an outline/structure doc
references: []            # List of citations/references used
status: draft             # draft, review, final

# templates/mote/memorize.yml
---
question: ""              # Front of card
answer: ""                # Back of card
difficulty: 0             # Current difficulty rating (0-5)
next_review: ${timestamp} # Next review date
review_history: []        # List of review timestamps and results

# templates/mote/reference.yml
---
source_type: ""          # book, article, web, etc.
authors: []              # List of authors
date: ""                 # Publication/creation date
url: ""                  # URL if applicable
doi: ""                  # DOI if applicable
isbn: ""                 # ISBN if applicable
accessed: ${timestamp}   # When this reference was accessed/created
citation: ""            # Formatted citation text

# templates/mote/accomplish.yml
---
due: null                # Due date if applicable
priority: 3              # Priority (1-5)
status: todo            # todo, in_progress, done, cancelled
dependencies: []        # List of dependent task IDs
assignee: ""           # Person assigned (if applicable)
progress: 0            # Progress percentage (0-100)

# templates/mass.yml
---
properties:
  dense: false           # Whether components are tightly bound
  ordered: false         # Whether sequence matters
components: []           # List of component objects
  # Each component has structure:
  # - id: ${uuid}
  #   type: mote|mass
  #   sequence: ${n}     # Only if ordered: true
location: ${path}        # Path within .mttr/objects/masses

# templates/bond.yml
---
properties:
  category: reference    # reference, dependency, contradiction, support
  strength: 1.0         # Bond strength (0.0-1.0)
  bidirectional: false  # Whether bond is bidirectional
  visual:
    color: "#4A90E2"    # Visual representation color
    thickness: 1        # Line thickness for visualization
    style: "solid"      # Line style (solid, dashed, dotted)
objects:
  - id: ${uuid_1}
    role: source
  - id: ${uuid_2}
    role: target
location: ${path}        # Path within .mttr/objects/bonds