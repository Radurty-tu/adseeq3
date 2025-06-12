# Drag Polar Construction

This page condenses the key steps from *Airplane Design Part 3* p.170. It describes how to estimate drag polars for different flight phases so that constraint curves can be constructed later in the matching diagram.

## Flap and Gear Effects
- **Oswald factor change** due to flap deflection is approximated using Obert's relation (Eq. 7.62). The effect is larger for fuselage-mounted engines than for wing-mounted engines.
- **Zero-lift drag increment** for flap deflection is crudely estimated as 1.3 drag counts per degree of deflection (Eq. 7.63).
- **Landing gear drag increment** adds 100–250 drag counts to the zero-lift drag coefficient (Eq. 7.64).

These relations provide quick estimates until more refined analyses are available.

## Example Configuration
- Starting cruise condition: $C_{D0}=0.0180$, $e=0.80$ and aspect ratio $A=8$.
- Flap settings examined:
  - Cruise: flaps up, gear up.
  - Take‑off 1: flaps 15°, gear up.
  - Take‑off 2: flaps 15°, gear down.
  - Landing: flaps 35°, gear down.
- For each case, Eqs. 7.62–7.64 are used to adjust $e$ and $C_{D0}$.

## Assignment 7.7 Tasks
1. Compute $e$ in cruise (Eq. 5.17).
2. Select landing flap deflection.
3. Choose an intermediate take‑off flap setting.
4. Find $C_{D0}$ for take‑off and landing with Eq. 7.63–7.64.
5. Compute $e$ for take‑off and landing using Eq. 7.62.
6. Tabulate the resulting coefficients similar to the example table.

This procedure yields a set of drag polars in cruise, take‑off and landing, allowing subsequent performance calculations.
