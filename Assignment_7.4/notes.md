# Assignment 7.4 Notes

Summary of how to compute thrust or power lapse at cruise altitude based on Part 3 p. 158.

1. **Cruise Conditions**
   - Determine the cruise altitude and temperature offset \(\Delta T\). From these, compute the ambient static pressure \(p\) and temperature \(T\) using standard atmosphere equations (7.10) and (7.11) of the text.
   - Use the cruise Mach number \(M\) to find the total temperature \(T_t\) via
     \[T_t = T \left(1 + 0.2 M^2\right)\] (Eq. 7.31)
     and the total pressure \(p_t\) via
     \[p_t = p \left(1 + \tfrac{\gamma - 1}{2} M^2\right)^{\tfrac{\gamma}{\gamma-1}}\] (Eq. 7.32).
   - Define the nondimensional ratios
     \[\theta_t = \frac{T_t}{T_{SL,ISA}},\qquad \delta_t = \frac{p_t}{p_{SL,ISA}}\] (Eqs. 7.33 and 7.34).

2. **Thrust Lapse for Turbofan Engines**
   - Let \(B\) be the bypass ratio and \(\theta_{t,\text{break}}\) the total temperature threshold beyond which the throttle is reduced. Typical \(\theta_{t,\text{break}}\) ranges from 1.06–1.08.
   - The thrust lapse factor \(\alpha_T\) depends on \(B\), \(\theta_t\), and \(M\):
     - For \(0 < B < 5\) and \(\theta_t \le \theta_{t,\text{break}}\):
       \[\alpha_T = \delta_t\] (Eq. 7.35).
     - For \(0 < B < 5\) and \(\theta_t \ge \theta_{t,\text{break}}\):
       \[\alpha_T = \delta_t\left(1 - 2.1\tfrac{\theta_t - \theta_{t,\text{break}}}{\theta_t}\right)\] (Eq. 7.36).
     - For \(5 \le B < 15\) and \(\theta_t \le \theta_{t,\text{break}}\):
       \[\alpha_T = \delta_t\Bigl(1 - (0.43 + 0.014B)M\Bigr)\] (Eq. 7.37).
     - For \(5 \le B < 15\) and \(\theta_t \ge \theta_{t,\text{break}}\):
       \[\alpha_T = \delta_t\Bigl(1 - (0.43 + 0.014B)M - 1.5 (M^2 - 1) \tfrac{\theta_t - \theta_{t,\text{break}}}{\theta_t}\Bigr)\] (Eq. 7.38).
   - Low-bypass turbofans may show a positive thrust change with Mach number for small altitudes when \(\theta_t \le \theta_{t,\text{break}}\), while higher bypass ratios experience stronger lapse effects.

3. **Assignment Steps**
   - Identify the cruise altitude of the aircraft (choose if unspecified).
   - Compute \(\alpha_T\) for the chosen engine using the above equations and the bypass ratio appropriate for your design. For propeller-driven aircraft, compute the analogous power lapse \(\alpha_P\) using the same approach.

These equations allow you to estimate the reduction in available thrust (or power) at cruise conditions, which is needed for constructing constraint curves in subsequent design steps.
