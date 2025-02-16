# MATTER

**Note: the ideas found below are still being developed.**

MATTER is a CLI-based tool

The starting point is the use of "physical matter"" as a metaphor for
nonphysical, primarily cognitive units, processes, etc. This is reflected
by the use of a nonstandard, even idiosyncratic, language to describe the
various objects, their relationships, and the actions that can be performed
on them.

## Comparison with other software

Applications like Obsidian, LogSeq, and others present interesting ways to
interact with one's files, and many people obviously find them useful. Albeit,
whenever you choose one application over another, that application closes 
certain avenues, even while opening others. My experience of Obsidian and co.
was exactly this: Although they offer unique methods, relatively speaking, for
interacting with files, I often felt like they were keeping me from doing more
interesting things. This isn't necessarily a criticism of any particular
application, but it is a critique of the, often aggressively enthusiastic,
communities that coalesce around these applications and the ideas they
represent.

## Objects

- mote
  - The most basic unit, generally consisting of a single "thing", be its
  documentable, memorizable, etc. In a sense "indivisible" in that it makes
  little sense to break it down into component parts, the true dimensions
  of any given mote is left to the discretion of the user.
- mass
  - Any aggregate of motes and masses as determined by the bonds between them.
- bond
  - The connection between any two objects, be they motes and motes, masses
  and masses, or motes and masses.

## Properties

Although their are only three classes of objects, every object can be
associated with a number of properties. Certain properties are necessary
in determining what sorts of things can be done with an object. For
instance, "memorize" and "document" objects fulfill different functions,
and will be treated differently as a result.

Bonds are just as much "objects" in this regard as motes and masses—which is
to say, bonds also have properties. Two properties unique to bonds determine
the structure of masses by determining their density and their directionality.

- dense
- order

Their can exist multiple bonds between any object pair, which allows networks
of ideas to be viewed in different ways.

## Functions

```sh
mttr coalesce
mttr form ...
mttr void ...
mttr reveal ...
mttr mend ...
mttr ...

```

What should matter be able to do?

- Fluidly connect ideas, sources, people, tasks, etc., and reveal the
  connections between these things in useful and interesting ways.

More specific objectives:

- Retrieve information from websites
- Extract information from PDFs, e-books and other sources
- Create and connect notes
- Create and learn flashcards
- Manage bibliographies, contacts, emails, notes, flashcards

Main areas:

- Create and manage notes
- Create, manage, and learn flashcards
- Manage source/reference material
- Create and manage tasks
- Connect all of the above, e.g. notes and sources, flashcards and notes,
  tasks and notes, etc.

## YAML-based metadata

Justification for separating metadata and files:

- Cleaner writing experience
- More flexible application of YAML
- Ability to add metadata to diverse file types without having to add
  the files to notes.

- Ordered (sequential/hierarchical) vs. unordered: An object precedes, and/or
  is preceded by, another object, whereby actions performed on a given object
  are dependent on the completion of actions performed on prior object.
  - Examples:
    - Ordered notes are those for which one note conceptually precedes
      another note.
    - Ordered flashcards are those for which one flashcard should be
      learned before another.
    - Ordered tasks are those for which one task must be finished
      before another can be started.
- Dense vs. sparse: The connections between objects vary in magnitude based on
  conceptual relatedness—whereby "relatedness" varies according to individual
  needs and goals.
  - Examples:
    - A note can represent the continuation of an idea from another note,
      or it might only be conceptually related, but not directly relevant.
    - A flashcard can be immediately relevant to another.
    - A task might be part of the same project, and therefore directly
      relevant, or only distantly related.
- The relationships between objects consist of a combination of **order** and
  **density**:
  - Ordered and dense:
    - Notes: A composite note.
    - Flashcards: A composite flashcard.
    - Tasks: A cluster of tasks.
  - Ordered, but not dense:
    - Notes: A sequence of ideas where one ideas follows from the next.
    - Flashcards: A sequence of flashcards where one is learned, then then next.
    - Tasks: A sequence of tasks that may not be directly related, but where
      one task might block another.
  - Not ordered, but dense:
    - Notes: A collection of related notes, similar to a folder, tag, or label.
    - Flashcards: A collection of related flashcards, similar to a deck or tag.
    - Tasks: A collection of related tasks that can be done in any order.
  - Not ordered or dense:
    - Notes: Any linked notes.
    - Flashcards: Any linked flashcards.
    - Tasks: Any linked tasks.

## Network visualization

Visualizations of massive networks of ideas are, although visually impressive,
of limited utility. A more useful approach would enable the individual to
explore these networks in different ways, which is why *matter* seeks to
**reveal** connections in a systematized manner.

For example, instead of simply presenting all notes linked to a particular
note, where the only adjustable variable is perhaps "depth", **matter**
allows the individual to systematically trace a path from one idea to another,
and to do so in a way that this path can then itself be formed into a "mass", i.e.
a composite of ideas.
