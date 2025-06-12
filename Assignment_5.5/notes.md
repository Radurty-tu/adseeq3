# Fuel- and Battery-Mass Fraction

Summary of *Airplane Design Part 2* pp.92-94 on computing the mass fraction of the energy carrier.

## Key Formulas

The fuel or battery mass needed for the mission is obtained using the equivalent range $R_{eq}$ in the Breguet-type relations:

\[
\frac{m_f}{m_{MTO}} = 1 - \exp\!\left(\frac{-R_{eq}}{\eta_{eng}\,\eta_p\,(e_f/g)\,(L/D)}\right) \tag{5.5}
\]
\[
\frac{m_{bat}}{m_{MTO}} = \frac{R_{eq}}{\eta_{EM}\,\eta_p\,(e_{bat}/g)\,(L/D)} \tag{5.6}
\]
These equations show that the required energy mass fraction scales strongly with the lift-to-drag ratio $L/D$ and the efficiencies $\eta_p$ or $\eta_{EM}$ (for electric motors) or $\eta_{eng}$ (for engines). A higher $L/D$ or efficiency reduces the mass needed.

## Example 5.7 – Turbofan Fuel Fraction

Using an equivalent range of $R_{eq}=4400\,\text{km}$ with $\eta_j=0.33$ and $\left(L/D\right)_{CR}=16.7$, the fuel-mass fraction is computed from (5.5) as

\[
\frac{m_f}{m_{MTO}} \approx 0.14
\]
which means about 14\% of the maximum take-off mass is fuel. Varying $L/D$ or efficiency changes this fraction noticeably.【F:part2_p92-94.txt†L55-L63】

## Example 5.8 – Battery Fraction

For a single-prop electric airplane with $R_{eq}=620\,\text{km}$, $\left(L/D\right)=13.8$, motor efficiency $\eta_{EM}=0.94$, and battery specific energy $e_{bat}=350\,\text{Wh/kg}$ (\(1.26\,\text{MJ/kg}\)), equation (5.6) gives

\[
\frac{m_{bat}}{m_{MTO}} \approx 0.46
\]
indicating nearly half of the take-off mass must be batteries. This value is highly sensitive to the assumed $L/D$ and $\eta_{EM}$.【F:part2_p92-94.txt†L86-L98】

## Assignment Guidance

The text stresses that mass-fraction results depend on $L/D$, efficiencies, aspect ratio $A$, and energy carrier properties. The assignment asks for:
1. Estimating the maximum cruise $L/D$ from your aspect ratio, zero-lift drag coefficient and Oswald factor.
2. Using (5.5) or (5.6) to compute the fuel- or battery-mass fraction.
3. Including reserve energy if applicable.
A placeholder estimate for maximum $L/D$ should be obtained from these aerodynamic parameters prior to applying (5.5)/(5.6).【F:part2_p92-94.txt†L116-L128】
