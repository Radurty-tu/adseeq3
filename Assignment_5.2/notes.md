# Estimating the Zero-Lift Drag Coefficient (Part 2, pp. 83-85)

The drag at zero lift can be approximated by relating the equivalent friction coefficient \(\bar{C}_f\) of the aircraft skin to its wetted area \(S_{\text{wet}}\) using

\[ \bar{C}_f S_{\text{wet}} = C_{D0} S_w \quad (5.14) \]

which rearranges to

\[ C_{D0} = \bar{C}_f \frac{S_{\text{wet}}}{S_w} \quad (5.15) \]

Hence, the estimation requires the ratio \(S_{\text{wet}}/S_w\) and the average friction coefficient.

## Wetted Area Ratio

Figure&nbsp;5.3 suggests typical ratios of wetted area to wing reference area for different aircraft types. Rough guidelines are:

- single‑engine light aircraft: \(~4\)
- twin‑prop commuter: \(~5\)
- commercial jet transport: \(~6\)

When only a flying wing is considered, the ratio may be slightly above 2. These values provide an initial assumption until detailed geometry is available.

## Estimating Wetted Area

1. **Assume \(S_{\text{wet}}/S_w\)** for the airplane using Fig.&nbsp;5.3 and reference aircraft.
2. **Approximate wetted areas of reference aircraft** using their wing area and the assumed ratio.
3. **Estimate the wetted area of the new design** by averaging or scaling from the references.

## Friction Coefficient

The equivalent friction coefficient depends on size, surface quality and shape. Figure&nbsp;5.4 shows a decreasing trend with wetted area. Placeholder values from the figure are approximately

- \(\bar{C}_f \approx 0.0045\) for very small airplanes
- \(\bar{C}_f \approx 0.0030\) for typical single‑aisle transports

Larger aircraft approach an even lower value, provided the surface finish is similar.

## Five‑Step Procedure

1. Choose an initial \(S_{\text{wet}}/S_w\) ratio.
2. Estimate the wetted areas of reference aircraft.
3. Derive the wetted area of the design aircraft.
4. Determine \(\bar{C}_f\) using Fig.&nbsp;5.4.
5. Compute \(C_{D0}\) from equation&nbsp;(5.15).

This procedure allows a preliminary estimate of the zero‑lift drag coefficient before a detailed geometry definition is available.
