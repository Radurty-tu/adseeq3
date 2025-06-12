# Constructing the climb-gradient constraint (Part 3 p.175)

This page of the notes describes how the text in *Airplane Design Part 3* explains the construction of a climb‑gradient constraint curve.

## Example procedure
For a jet airplane with a climb‑gradient requirement of \(c/V = 0.024\) at sea level with \(\Delta T = 15\,\mathrm{K}\) and one engine inoperative, the book illustrates these steps:

1. **Determine density** at the given altitude and temperature using Eqs. (7.10) and (7.12). At sea level with \(T=303\,\mathrm{K}\) and \(p=101\,\mathrm{kPa}\), this gives \(\rho=1.16\,\mathrm{kg/m^3}.\)
2. **Find CL and CD** giving the best climb gradient for the chosen configuration (take‑off configuration in the example). With \(C_{D0}=0.038\) and \(e=0.87\), the resulting coefficients are \(C_L=0.91\) and \(C_D=0.075\).
3. **Compute the speed** for maximum climb gradient from Eq. (7.43) for a range of wing‑loading values.
4. **Determine Mach number** for each speed using Eq. (7.30).
5. **Calculate total temperature and pressure ratios** \(\theta_t\) and \(\delta_t\) via Eqs. (7.34) and (7.32).
6. **Evaluate thrust lapse** \(\alpha_T\) using Eqs. (7.37) and (7.38).
7. **Compute the required thrust‑to‑weight ratio** using Eq. (7.60) for each wing loading.
8. **Plot the resulting points** to obtain the climb‑gradient constraint curve on the matching diagram.

## Assignment 7.8 tasks
The text then outlines a general procedure to construct this constraint for your own design. The steps are:

- (a) State the climb‑gradient requirement (\(c/V\), altitude \(h\), mass ratio \(\beta\), temperature change \(\Delta T\)) and whether it applies to all engines operating (AEO) or one engine inoperative (OEI), including the airplane configuration.
- (b) Quote suitable values for \(C_{D0}\) and Oswald factor \(e\).
- (c) Compute ambient temperature and density for the requirement.
- (d) Determine the lift coefficient maximizing the climb gradient, accounting for margin to stall if needed.
- (e) Compute the corresponding drag coefficient.
- (f) For chosen wing‑loading values, find the speed that maximizes climb gradient.
- (g) Calculate Mach number for each speed.
- (h) Evaluate \(\theta_t\) and \(\delta_t\) for each Mach number.
- (i) Determine the thrust lapse \(\alpha_T\) for each wing loading using the appropriate formula.
- (j) Compute the required power loading or thrust‑to‑weight ratio so that the climb‑gradient requirement is met.
- (k) Plot the climb‑gradient constraint curve in the matching diagram.

These steps generate the curve that can be compared with other performance constraints.
