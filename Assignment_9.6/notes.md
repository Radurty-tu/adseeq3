# Landing Gear Tire and Rim Sizing

Summary of Part 3 p.253 (Airplane Design Part 3) on how to size landing-gear tires and rims using rated loads.

* **Rated Tire Load Calculation**
  * For main gear tires, distribute the maximum take-off weight over the number of main wheels while using the aft center-of-gravity load fraction. This yields the rated load per tire:
    
    \( F_{t,mlg} = \frac{f_{mlg} W_{MTO}}{N_{w,mlg}} \)  
    *(Eq. 9.22)*【F:page125.txt†L80-L94】
  * Nose gear tires experience their highest loads during braking with the CG forward. For twin nose wheels a factor \( f_{dif}=1.07 \) accounts for unequal wear and inflation:
    
    \( F_{t,nlg} = \frac{f_{nlg} f_{dif} W_{MTO}}{N_{w,nlg}} \)  
    *(Eq. 9.23)*【F:page126.txt†L5-L13】【F:page126.txt†L20-L21】

* **Selecting Tires and Rims**
  1. Choose tire pressure from runway surface type or PCR and update the aircraft classification rating if needed.【F:page126.txt†L32-L35】
  2. Compute the rated tire load for main and nose gear using the equations above.【F:page126.txt†L38-L41】
  3. Use a tire database or Figure 9.6 to pick the smallest tire whose rated load exceeds the calculated load. The figure relates rated load and tire pressure to tire diameter, width, and rim diameter.【F:page126.txt†L21-L31】【F:page126.txt†L40-L41】

* **Additional Considerations**
  * Choose smaller tires when possible to reduce drag and stowage volume.
  * Keep margin between rated load and maximum load so later weight growth does not require larger tires.【F:page128.txt†L12-L23】

Assignment 9.6 asks you to apply this method: select tire pressure, calculate maximum rated loads for main and nose gear, and specify tire and rim dimensions.【F:page128.txt†L29-L39】
