You're absolutely right. Looking at the README, masses and bonds have their own distinct properties. Let me add templates for those and reorganize our structure to better reflect the system's architecture.



Key changes and additions:

1. Reorganized the structure:
   - `global.yml` now only contains truly universal properties
   - Created a `mote/base.yml` for shared mote properties
   - Moved specific mote types under `templates/mote/`

2. Added `mass.yml`:
   - Implements the mass properties from the README
   - Supports both dense/sparse and ordered/disordered collections
   - Defines component structure for containing other objects

3. Added `bond.yml`:
   - Implements the bond properties from the README
   - Supports visual properties for network representation
   - Defines clear source/target relationship structure

4. Consistent location handling:
   - Each template specifies its location in the `.mttr` directory structure
   - Follows the organization outlined in the README

Would you like to:
1. Refine any of these templates further?
2. Add any additional properties to specific types?
3. Define subtypes for any of the main types?
4. Specify validation rules for any of the properties?