# Notes on Adding Take‑Off Field‑Length Constraint (Part 3 p.179)

Part 3 page 179 describes "Assignment 7.9" where the reader builds the constraint
curve for the take‑off field‑length requirement. Steps **e**–**h** apply only to
jet aircraft. The procedure is:

1. **State the requirement** – specify the required take‑off field length `L_TO`,
   the take‑off altitude `h`, the temperature offset `ΔT`, and whether the
take‑off distance is based on all‑engine operating (AEO) or continued take‑off
after one engine inoperative (OEI).
2. **Define drag and lift parameters** – list the zero‑lift drag coefficient
   `C_D0` and Oswald factor `e` for the take‑off configuration.
3. **Compute atmospheric properties** – determine `T`, `p` and `ρ` for the
   take‑off conditions.
4. **Find the lift coefficient `C_L2`** – use the minimal allowable margin above
   stall speed to calculate `C_L2`.
5. **Determine safety speed `V₂`** – for a range of wing loadings `W/S`, compute
   the take‑off safety speed.
6. **Calculate Mach numbers** for the corresponding `V₂` values.
7. **Evaluate total temperature ratio `θ_t` and pressure ratio `δ_t`** based on
   those Mach numbers.
8. **Compute thrust lapse `α_T`** for each wing loading using `θ_t` and `δ_t`.
9. **Find the required power loading or thrust-to-weight ratio** for the take‑off
   field length requirement across the chosen wing loading range.
10. **Plot the resulting constraint curve** in the matching diagram.

These steps add the take‑off field‑length limit to the matching diagram so the
feasible design space reflects this performance constraint.
