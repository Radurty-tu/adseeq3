# Runway Surface Selection and Pavement Classification

This note summarizes Part 1 pages 23-26 of the "Airplane Design" manual. The section explains how to select the appropriate runway surfaces for a new aircraft and how to determine the pavement classification rating (PCR) and aircraft classification rating (ACR).

## Choosing Airports
- Pick one or more reference airports that your aircraft must operate from. Choose carefully: basing requirements only on airports with strong surfaces will make the airplane unsuitable for softer fields.
- Identify the softest runway surface among those airports. Surfaces may range from soft grass to rigid concrete.

## Determining PCN and PCR
- For paved runways, obtain each runway's published Pavement Classification Number (PCN). The PCN is publicly available from airport data.
- The PCR used by ICAO has five entries: `G1/G2/G3/G4/G5`.
  - `G1` is twice the Derived Single Wheel Load (DSWL) and reflects pavement strength.
  - `G2` indicates pavement type: rigid (R) or flexible (F).
  - `G3` denotes subgrade strength: A (high) to D (ultra-low).
  - `G4` is the maximum allowable tire pressure: W (no limit), X (1.75 MPa), Y (1.25 MPa), Z (0.5 MPa).
  - `G5` shows the evaluation method: U (using aircraft experience) or T (technical evaluation).
- Compute a PCR estimate from the published PCN using:
  
  `[G1/G2/G3/G4/G5]_PCR ≈ [12 · G1/G2/G3/G4/G5]_PCN`

## Determining ACR
- The Aircraft Classification Rating (ACR) uses the same five entries but depends on the aircraft's weight.
- To operate on a runway, ensure `ACR ≤ PCR` for the relevant mass.
- Steps to derive the ACR requirement:
  1. Select reference airports.
  2. Qualitatively classify the softest runway surface.
  3. Gather PCN values for the reference runways.
  4. From these, note the lowest allowed `G1` (load) and `G4` (tire pressure).
  5. Convert the lowest PCN into PCR using the formula above, adopting the lowest tire pressure.
  6. State the ACR requirement at maximum take-off mass.

## Softer vs. Harder Surfaces
- **Softer surfaces (grass, gravel, sand):**
  - Allow operations from less-developed fields but demand larger tires and lower pressures to spread the load.
  - Higher rolling resistance and potential damage risk.
- **Harder surfaces (asphalt, concrete):**
  - Permit higher tire pressure and smaller wheels, leading to lighter, more compact landing gear.
  - Require well-maintained runways and limit operations in remote or undeveloped locations.
