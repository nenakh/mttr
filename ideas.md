# Basic principles

The idea is to have different files, and file types, that can
be related in different ways. The main types:

- note
- card
- task

But I would like to keep things more playful and informal, which is why I'm
considering using different vocabulary for each type:

- note → chunk
- card → glob
- task → thing

Some more concepts:

- structural units
  - clump  → an aggregation of chunks, globs, things, or even other clumps;
  albeit while keeping the sub-objects discreet
  - strand → a connection between any object and any other object, basically a link
  - slab   → source material, i.e. books, articles, etc.

- "verbs", i.e. functions
  - cast   → create an object
    - `tug cast --chunk --glob --thing --slab`
  - clump  → connect objects into clumps, i.e. "clump" them together
  - fuse   → make a clump permanent, i.e. permanently merge the objects into
  one object
  - chop   → the opposite of fuse, i.e. turn an object into a clump
  - pluck  → move some part of an object into its own object
  - plunk  → move some object into part of another object
