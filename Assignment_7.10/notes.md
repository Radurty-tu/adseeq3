# Notes on Selecting the Final Design Point (Part 3 p. 183)

- After plotting all flight performance constraints in the matching diagram, pick one point which sets both wing size and propulsion system. This **design point** represents a combination of wing loading (W/S) and either power loading (W/P) for propeller aircraft or thrust-to-weight ratio (T/W) for jets.
- Ensure the chosen point lies inside the feasible region bounded by all active constraint curves. The goal is generally the smallest wing and powerplant while still meeting every constraint.
- For a propeller airplane, this typically means choosing a point on the climb–gradient line at the intersection with the stall–speed line. Here the stall–speed constraint sizes the wing, and the climb–gradient constraint sizes the powerplant.
- For a jet airplane, feasible space lies above the thrust curves and left of the wing–loading limits. Choose a point on the take‑off curve between its junctions with the climb–rate and approach–speed lines. In that case the take‑off and approach‑speed constraints determine propulsion and wing size.
- Once the design point is chosen and the maximum take‑off mass is known, compute wing area and power (or thrust):
  - \(S_w = \frac{m_{MTO} g}{W_{TO}/S_w}\)   (Eq. 7.78)
  - For propeller airplanes: \(P_{TO} = \frac{m_{MTO} g}{W_{TO}/P_{TO}}\)   (Eq. 7.79)
  - For jet airplanes: \(T_{TO} = m_{MTO} g\,(T_{TO}/W_{TO})\)   (Eq. 7.80)
- Example 7.11 illustrates this calculation. For a 1 830 kg propeller aircraft at a design point of \(W_{TO}/S_w = 1230\text{ N/m}^2\) and \(W_{TO}/P_{TO} = 0.118\text{ N/W}\), the result is
  \(S_w = 14.6\text{ m}^2\) and \(P_{TO} = 152\text{ kW}\).
  For a jet with \(m_{MTO} = 63\text{ t}\) and design point \(W_{TO}/S_w = 5500\text{ N/m}^2\), \(T_{TO}/W_{TO} = 0.34\), the wing area is \(S_w = 112\text{ m}^2\) and total thrust \(T_{TO} = 210\text{ kN}\) (105 kN per engine for a twin).
