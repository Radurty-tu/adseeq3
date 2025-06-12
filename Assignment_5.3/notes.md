# Oswald Efficiency Factor Estimation

Based on *Airplane Design Part 2*, page 85, the Oswald efficiency factor `e` accounts for changes in lift‑induced drag compared to an ideal wing. For a configuration without flap deflection, the induced drag is modeled as:

\[
C_{D_i} = \psi \, C_L^2 + \frac{C_L^2}{\pi A_w \phi}
\]

where `ψ` is a parasite drag parameter depending on lift coefficient and `φ` is the span efficiency factor.

Equation (5.17) provides `e` as:

\[
e = \frac{1}{\psi \, \pi A_w + \tfrac{1}{\phi}}
\]

**Example assumptions**

1. Take the parasite drag parameter as `ψ = 0.0075`.
2. Assume the span efficiency factor `φ = 0.83`.
3. Using the equation above yields `e ≈ 0.71` for the example four‑seat aircraft.

These assumptions match those used for the dashed trend line in Figure 5.5.
