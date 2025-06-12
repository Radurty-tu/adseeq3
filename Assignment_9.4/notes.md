# Landing-Gear Wheel Count (Part 3 p.247)

Part 3 outlines an iterative process for CS‑25 airplanes to decide how many wheels belong on each strut. Key steps:

1. **Derived single wheel load**: From the ACR computed earlier, obtain the derived single wheel load
   \(\text{DSWL} = \frac{G_1 \cdot 100 \cdot g}{2}\). This uses the first ACR entry (in hundreds of kilograms).
2. **Weight fractions**: Assume fractions of the aircraft weight carried by the main landing gear \(f_{mlg}\) and by the nose gear \(f_{nlg}\). At least 8% of the weight must rest on the nose gear; normally no more than 15% does so.
3. **Initial layout guess**: Based on reference aircraft, pick the number of main‑gear struts, wheels and wheel assemblies per strut. Do the same for the nose gear (see Table 9.1).
4. **Distribution factor**: Select a distribution factor \(DF\) for the main gear and nose gear from the wheel‑assembly table.
5. **Compute wheel numbers**:
   \[
   N_{w,mlg} \approx \frac{f_{mlg} W_{MTO}\,DF_{mlg}}{\text{DSWL}}, \qquad
   N_{w,nlg} \approx \frac{f_{nlg} W_{MTO}\,DF_{nlg}}{\text{DSWL}}.
   \]
6. **Round the results** so each gear has an even number of wheels and matches possible layouts:
   - if \(N_{w,mlg} \le 2\), set \(N_{w,mlg}=2\);
   - if \(N_{w,mlg} > 2\), round up to the nearest multiple of 4;
   - if \(N_{w,nlg} \le 1\), choose 1 or 2 wheels;
   - otherwise set \(N_{w,nlg}=2\).
7. **Check against the assumptions** made in step 3. If the computed wheel count differs, adjust the distribution factor or start over with a new layout guess.
8. **Choose number of struts** for the main gear using empirical guidelines:
   - \(N_{w,mlg} \le 12 \Rightarrow N_{s,mlg}=2\);
   - \(N_{w,mlg} > 12 \Rightarrow N_{s,mlg}=3\) or 4.

These steps size each landing‑gear truck so pavement loading and redundancy requirements are satisfied before selecting tire pressure and dimensions.
