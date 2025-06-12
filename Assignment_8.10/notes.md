# Determining Engine/Motor Dimensions and Envelope

Summary of the approach presented in *Airplane Design Part 3* p.221 for sizing a nacelle (engine enclosure):

- The cone at the exit of the gas turbine is sized using:
  - $$D_c \approx 0.55 D_{eg}$$
  - $$l_c \approx 1.5 D_c$$
- With these dimensions, the nacelle layout can be drawn. Example 8.14 describes the procedure for a jet engine (Type C nacelle, fan cowl fraction \(\phi=0.75\)):
  1. **Inlet diameter** \(D_i\) from mass flow using Eqs. (8.24)--(8.25). Example: \(D_i = 1.6\,\text{m}\).
  2. **Highlight diameter** \(D_h\) (droop neglected). Often set equal to the inlet diameter.
  3. **Nacelle length** \(l_n\) via Eq. (8.27) and Table 8.1. Example: \(l_n = 4.8\,\text{m}\).
  4. **Fan cowling length** \(l_f\) from Eq. (8.28). Example: \(l_f = 3.6\,\text{m}\).
  5. **Position of maximum diameter** located at \(\beta l_f\) using Table 8.1. Example: \(\beta = 0.39\) \(\Rightarrow\) 1.4 m from the highlight plane.
  6. **Maximum diameter** \(D_n\) from Eq. (8.29). Example: \(D_n = 1.9\,\text{m}\).
  7. **Fan cowling exit diameter** \(D_{ef}\) via Eq. (8.30). Example: \(D_{ef} = 1.5\,\text{m}\).
  8. **Gas turbine diameter at fan cowl exit** \(D_g\) from Eq. (8.32). Example: \(D_g = 1.0\,\text{m}\).
  9. **Gas turbine exit diameter** \(D_{eg}\) from Eq. (8.33). Example: \(D_{eg} = 0.56\,\text{m}\).
  10. **Cone size** using the relations above for \(D_c\) and \(l_c\). Example: \(D_c = 0.36\,\text{m}\) and \(l_c = 0.54\,\text{m}\).
  11. **Draw the nacelle outline** with all computed dimensions.
  12. **Connect the points** to complete the nacelle envelope.

The example ends by noting that a symmetry line is used as a reference when drawing because the nacelle is assumed axisymmetric. Assignment 8.15 encourages repeating these steps for a specific design.
