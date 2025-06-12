# Notes: Building the Loading Diagram and Calculating CG Shifts

This summary is based on **Airplane Design Part 3**, page 243 which outlines how to determine the aircraft center of gravity (CG) excursion using a simplified loading diagram.

## Steps for CG Estimation
1. **Group components** into wing and fuselage assemblies.
2. **Estimate component weight fractions** statistically.
3. **Compute wing and fuselage CG locations** from these fractions.
4. **Choose a desired CG position** for the operating empty mass (OEM) in terms of MAC.
5. **Compute the LEMAC position** in the fuselage reference frame.
6. **Determine fuel and payload CG locations** relative to the fuselage.
7. **Construct the simplified loading diagram** showing how CG shifts with payload and fuel addition.
8. **Estimate the vertical CG location** (often along the fuselage centerline).

## Assignment Highlights
- Calculate mass fractions for payload and fuel relative to the maximum take-off mass.
- Evaluate three configurations: OEM + payload, OEM + payload + fuel, and OEM + fuel.
- Plot these cases along with the OEM point in the loading diagram using normalized CG position (x/c_bar) on the horizontal axis and mass fraction (m_hat) on the vertical axis.
- Identify forward and aft CG limits, then show them in the side view of the drawing.
- Report the resulting forward and aft CG positions as well as the CG excursion Δx/c_bar.

The final forward and aft CG values provide inputs for sizing the landing gear and tail surfaces. Chapter 12 discusses a more refined approach, which may yield a larger CG travel than predicted with this simplified method.
