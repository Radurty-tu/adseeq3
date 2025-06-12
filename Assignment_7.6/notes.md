# Rate-of-Climb Constraint (Part 3 p.165)

This page outlines how to build the rate-of-climb constraint for the matching diagram. The key steps are:

1. **State the requirement** – specify climb rate $c$, altitude $h$, weight fraction $\beta$, and temperature deviation $\Delta T$.
2. **Find atmospheric properties** – compute $T$, $p$, and $\rho$ at the given altitude and temperature.
3. **Determine the optimal lift coefficient** where the highest climb rate occurs.
4. **For a range of wing loadings**, calculate the speed that yields the best climb rate.
5. **(Jet only)** Compute the corresponding Mach number for each wing loading and determine the total temperature ratio $\theta_t$ and total pressure ratio $\delta_t$.
6. **(Jet only)** Use $\theta_t$ and $\delta_t$ to evaluate the thrust lapse $\alpha_T$.
7. **Compute take‑off power loading or thrust‑to‑weight ratio** versus wing loading.
8. **Plot the constraint** in the matching diagram.

Propeller aircraft skip the Mach number and thrust lapse calculations because the thrust lapse relation for turbofans requires additional steps.
