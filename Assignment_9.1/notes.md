# Estimating Group Mass Fractions

Summary of Part 3 p.234 describing how to estimate operating empty mass fractions for aircraft components based on multiple reference airplanes.

## Group Mass Fractions
- Operating empty mass (OEM) is divided into component groups.
- Fractions are normalized with respect to maximum take-off mass (m_MTO) and denoted with a hat symbol (m̂).
- Groups include propulsion, fixed equipment, wing, tail, fuselage, nacelle and landing gear.

## Method with Multiple References
1. **Gather Data**: Collect group mass fractions from K reference aircraft similar to the design.
2. **Average Fractions**: For each component i, compute the average mass fraction normalized to the design MTO mass using
   
   \[ \hat m_{i,av} = \frac{\sum_{k=1}^{K} \hat m_{i,k} \hat m_{OE,k}^{ref}}{K \hat m_{OE}} \]  (Eq. 9.1)
3. **Unaccounted Mass**: Sum all averaged group fractions. Any difference with the overall OEM fraction is the unaccounted mass:
   
   \[ \hat m_{unacc} = \hat m_{OE} - \sum \hat m_{i,av} \]  (Eq. 9.2)
4. **Redistribute**: Scale each averaged fraction by
   
   \[ \hat m_i = \frac{\hat m_{i,av}}{1 - \hat m_{unacc}} \]  (Eq. 9.3)
5. **Check**: Ensure the recomputed fractions sum to the OEM fraction (Eq. 9.4).

## Example Procedure
- Select three jet transports as references (e.g., DC‑9‑30, MD‑80, 737‑200).
- Record each group’s fraction and the OEM fraction.
- Compute the unaccounted percentage for each reference (e.g., 5% for the 737‑200).
- Use Eq. 9.1 to average the fractions, then apply Eq. 9.3 to redistribute the remaining fraction so that Eq. 9.4 is satisfied.
- The resulting column gives estimated group mass fractions for the new airplane.
