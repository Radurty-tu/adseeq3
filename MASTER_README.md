# Master Design Notes

## Manual Overview
Pages 27-30 discuss deriving **top-level aircraft requirements**. Clear payload and mission definitions drive fuselage size and mass. Figure 3.1 illustrates a mission profile that helps quantify requirements like take-off distance, climb rate and diversion range. These requirements must be specific enough to check compliance later.

## Python Iteration Considerations
The manual emphasizes selecting analysis methods to quantify performance and verify requirements. Calculations such as mass breakdowns, drag coefficients, matching diagrams and mission fuel estimates can be iterated with Python. High-level choices—mission profile, payload definition and regulatory constraints—should be set by the designer before running scripts.


# Source: ./Assignment_1.1/notes.md

# Defining a Design Problem (Part 1 pp. 1-2)

These notes summarize the opening pages of *Airplane Design and Analysis* Part 1. The text outlines an eight‑step engineering design process. The first two pages focus on framing a design problem before exploring potential solutions.

## Key Ideas
- A clear design problem statement is essential. It defines what needs to be solved and may be broken down into smaller problems. Example: reducing greenhouse-gas emissions of regional travel.
- Requirements come from customers, regulations and suppliers. Specify only those relevant for the current phase.
- State a design objective to compare options, typically by minimizing or maximizing a performance metric.
- Brainstorm multiple design options, learning from past successes and failures. Consider functions first, then whether to adapt an existing design or create something original.

The text proposes the following guiding questions:

1. **What air transportation needs do you foresee in the near future?**
2. **What transportation need would you like to focus on during the course of this book?**
3. **If there are existing design solutions for these transportation needs, how do you want your design solution to distinguish itself from what is already existing?**
4. **Having answered these questions, write down your design problem statement.**【F:Assignment_1.1/notes.md†L1-L18】

If answering these questions is difficult, the authors suggest using an existing airplane as a basis. Designing a new airplane should surpass existing aircraft in cost or emissions when serving the same role. A brand‑new concept may target unmet needs but must still be attractive by keeping life‑cycle costs low.【F:Assignment_1.1/notes.md†L20-L22】

## Pros and Cons of a New Versus Existing Airplane
**Inventing a New Airplane**
- **Pros:** Can serve novel market needs; opportunity to reduce operating cost or emissions beyond current designs.
- **Cons:** Higher risk and development cost; market objectives may be less clear.

**Adapting an Existing Airplane**
- **Pros:** Easier to start from proven technology; existing data helps answer the design questions.
- **Cons:** Improvements may be limited; less freedom to address new requirements.

## Initial Design Problem Statement
*Example*: Rising demand for short-haul flights risks increasing global emissions. Develop a regional aircraft concept with substantially lower life‑cycle carbon footprint than current models while maintaining competitive operating costs.

# Source: ./Assignment_3.1/notes.md

# Assignment 3.1 – Payload Related Requirements

The textbook *Airplane Design Part 1* (pp. 18–20) describes how to establish the payload requirement before sizing the aircraft. The passage emphasizes that the payload definition strongly affects the fuselage size and overall mass.

Average passenger data collected at European airports in 2022:

- 76 kg passenger mass
- 8 kg carry-on luggage mass
- 16 kg checked luggage mass (bounded by airline allowances such as 23 kg)

This results in an average payload of **100 kg per passenger**.

To estimate luggage and cargo volumes, the book suggests placeholder densities:

- Luggage density $\rho_{\text{luggage}} \approx 170\;\mathrm{kg/m^3}$
- Cargo density $\rho_{\text{cargo}} \approx 160\;\mathrm{kg/m^3}$

## Assignment instructions (Part 1, pp. 18‑20)

### a. Maximum‑capacity condition

1. How many passengers are required to be transported?
2. What is the mass of the passengers plus their luggage?
3. How are the passengers divided among different classes?
4. What seat width and seat pitch do you require?
5. How many cubic meters of luggage do you need?
6. How much volume is required in the cabin for carry‑on luggage?
7. How much volume is needed in a cargo hold for luggage?
8. What is the cargo mass?
9. How much cargo volume is required?
10. What is the maximum structural payload mass?

### b. Design condition (*skip if identical to the maximum‑capacity condition*)

1. How many passengers are required to be transported?
2. What is the mass of the passengers plus their luggage?
3. How are the passengers divided among different classes?
4. What seat width and seat pitch do you require?
5. How many cubic meters of luggage do you need to transport?
6. How much volume is required in the cabin for carry‑on luggage?
7. How much volume is needed in a cargo hold for luggage?
8. How much cargo volume is required?
9. What is the cargo mass?
10. What is the design payload mass?

These questions form the basis for defining your top‑level payload requirements before proceeding to mission and performance calculations.

# Source: ./Assignment_3.2/notes.md

# Mission Profile Derivation (Part 1 pp.20-22)

Part 1 describes how a mission profile is used to derive top-level aircraft requirements. The mission profile plots altitude against distance and shows each phase of flight, starting with taxi and ending with landing. Example 3.3 illustrates a typical transport-airplane mission profile and lists the resulting requirements. Example 3.4 does the same for a high‑altitude reconnaissance airplane.

### Drawing the mission profile
1. Draw a two‑dimensional graph with distance on the horizontal axis and altitude on the vertical axis.
2. Sketch the following sequence:
   - Taxi and take‑off at the origin.
   - Climb to cruise altitude and cruise to destination (nominal range).
   - Descent and approach to the destination.
   - Diversion leg from the destination to an alternate airport.
   - Loiter (holding pattern) before landing.
3. Label each mission leg (taxi, take‑off, climb, cruise, descent, diversion cruise, loiter, land + taxi) as in Figure 3.1.

### Requirements extracted from Example 3.3
- **Nominal range:** 3,000 km.
- **Diversion range:** 400 km.
- **Loiter time:** 30 minutes at the alternate airport before landing.

### Assignment 3.2 tasks
- Draw and annotate the mission profile as outlined above.
- State the required nominal range, diversion range and loiter time for the design payload.

# Source: ./Assignment_3.3/notes.md

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

# Source: ./Assignment_3.4/notes.md

# Flight-Phase Requirements Summary (Part 1, pp.27-30)

These pages introduce how to derive **Top-Level Aircraft Requirements (TLARs)** from the mission profile. Figure 3.1 in the text provides a typical transport-aircraft mission and is used to extract specific performance targets for each phase. The resulting requirements offer measurable criteria for verifying the design.

## Take‑Off
Questions to define this phase:
1. What runway length is assumed?
2. At what altitude and ambient temperature must take‑off occur?
3. What surface conditions (paved/unpaved, wet/dry) are considered?

*Example placeholder:* 2.5 km paved runway at sea level, ISA +15 °C.

## Climb
Questions to define this phase:
1. What climb rate or gradient is required?
2. At which altitude and speed should this be achieved?
3. At what mass fraction (e.g. % of MTOM) is the requirement evaluated?

*Example placeholder:* 1 m/s at top‑of‑climb around 35 000 ft (ISA +10 °C) with 98 % of MTOM.

## Cruise
Questions to define this phase:
1. What cruise Mach number or true airspeed is required?
2. At which cruise altitude and temperature offset?
3. What mission range does the cruise segment cover?

*Example placeholder:* Mach 0.8 at 35 000 ft, ISA +5 °C, nominal range 3 000 km.

## Landing
Questions to define this phase:
1. What landing distance is permissible and on what runway type?
2. At what altitude and atmospheric conditions must landing performance be met?
3. Are specific weather scenarios (e.g. wet or icy runway) considered?

*Example placeholder:* Land on a 2.9 km paved runway at sea level in all‑weather conditions.

## Key Idea
For each phase, quantifying altitude and temperature conditions ensures the TLARs are specific and measurable. These placeholders should be replaced by project‑specific data once available.

# Source: ./Assignment_3.5/notes.md

# Airworthiness Regulations – Summary (Part 1 pp. 31–33)

These pages discuss how to determine which set of airworthiness requirements apply at the start of a new aircraft project. The applicable code (e.g. CS‑23 or CS‑25) drives the entire certification process, so defining the certification basis early is vital.

## Key Criteria

1. **Weight of the aircraft** – The take‑off mass determines whether the design falls in the “Large Airplane” scope of CS‑25 or the smaller airplane categories covered by CS‑23.
2. **Number of passengers** – Passenger capacity is another factor in selecting the appropriate category. Larger passenger numbers typically push the design towards CS‑25.
3. **Powerplant type** – Whether the airplane has piston engines, turboprops or turbofan engines influences which regulation is applicable. For example, a twin turbofan transport with many seats qualifies as a CS‑25 large airplane.

For light aircraft, EASA’s CS‑VLA or CS‑LSA may apply, imposing fewer tests and lower costs than CS‑23. A short‑range two‑seater may therefore be certified under CS‑VLA, while aircraft like the Pipistrel Velis Electro or Cirrus SF‑50 are examples within CS‑23 categories. Larger transports such as the Embraer E190E2 fall under CS‑25.

## Structure of the Regulations

Each code consists of two books:

- **Book 1 (Airworthiness Code)** – Contains all mandatory requirements, organized in subparts for the aircraft structure, equipment, powerplant, etc.
- **Book 2 (Acceptable Means of Compliance)** – Offers guidance on how to demonstrate compliance with each requirement in Book 1.

The combination of these documents forms the certification basis. With hundreds or thousands of requirements possible, designers must identify at the outset which specific regulations apply.

# Source: ./Assignment_3.6/notes.md

# Stall or Approach Speed Requirements (Part 1 pp. 33-35)

This note summarizes the stall or approach speed requirements discussed in **Part 1** of the course notes (pp. 33‑35). These pages focus on how certification basis determines the speed criteria that must be met and which conditions to specify when defining the requirement.

## CS‑23 Stall Speed Requirement

CS/FAR‑23 sets a maximum stall speed of **61 knots** (31 m/s) at maximum weight for:

- Single‑engine aeroplanes
- Twin‑engine aeroplanes up to **2722 kg (6000 lb)** that cannot meet the one‑engine‑inoperative climb rate

Very Light Aircraft (VLA) or Light‑Sport Aircraft (LSA) must not exceed **45 knots** (23 m/s). These limits come directly from CS/FAR 23.49, and apply to small aircraft certified under CS‑23.

## CS‑25 Approach Speed Requirement

CS‑25 does not prescribe a minimum stall speed. Instead, a final approach speed (\(V_{REF}\)) is defined. According to CS‑25.125, \(V_{REF}\) must be at least **1.23** times the stall speed in the landing configuration (\(V_{SR0}\)):

```
Vapp = 1.23 · VS0
```

This ensures a **23% margin** between approach speed and stall speed when flaps and gear are fully deployed.

The CS‑25 requirement usually appears in the Top‑Level Aircraft Requirements (TLARs) as a specified approach speed rather than a direct stall speed limit.

## Choosing Which Criteria Apply

- **Use CS‑23 criteria** when the aircraft falls under CS‑23 (including CS‑VLA or LSA). Here you set a stall speed limit and specify conditions.
- **Use CS‑25 criteria** for large airplanes certified under CS‑25. Instead of a stall speed limit, define the final approach speed and ensure the 1.23 factor to derive the stall speed.

## Conditions to Specify

Assignment 3.6 requires that stall or approach speed be stated together with:

1. **Altitude** (e.g. sea level or 1500 m)
2. **Airplane mass** relative to MTOM (e.g. 100 % MTOM or 85 % MTOM)
3. **Temperature** (e.g. ISA, ISA + 10 °C)

These conditions clarify how density and mass affect the speed requirement.

When documenting your own design, include example placeholders similar to the following:

| Certification basis | Speed requirement | Altitude | Weight | Temperature |
|---------------------|------------------|---------|--------|-------------|
| CS‑23 | VS₀ ≤ 61 kt (or 45 kt for CS‑VLA/LSA) | [e.g. 0 ft] | [e.g. 100 % MTOM] | [e.g. ISA+0 °C] |
| CS‑25 | Vapp = 1.23 × VS₀ | [e.g. 5000 ft] | [e.g. 90 % MTOM] | [e.g. ISA+10 °C] |

Replace the placeholders with your actual design values when completing the assignment.

# Source: ./Assignment_3.7/notes.md

# Climb-Gradient Requirements Summary

This note summarizes the discussion on climb-gradient regulations from *Airplane Design and Analysis Part 1* pages 35–36. The text introduces relevant certification paragraphs and explains which operating conditions must be logged when formulating these requirements for a new design.

## Referencing regulation paragraphs

The book lists the following paragraphs from CS/FAR regulations as the main sources for climb-gradient limits:

- **CS/FAR 23.65** – Climb performance with all engines operating.
- **CS/FAR 23.67** – One-engine-inoperative climb requirements.
- **CS/FAR 23.77** – Balked landing (go‑around) climb.
- **CS/FAR 25.111** – Take‑off path description.
- **CS/FAR 25.117** – General climb conditions.
- **CS/FAR 25.119** – Landing climb, all engines operating.
- **CS/FAR 25.121** – One-engine-inoperative climb during take‑off and approach.

The book explains that paragraph numbers in the text should be cited exactly (e.g. *“CS 25.119”* or *“CS/FAR 23.65”*) so that the reader can locate the corresponding section in the regulations.

## Information to record for each requirement

Assignment 3.7 asks the designer to note, for each applicable regulation paragraph, the required climb gradient together with these operating conditions:

1. **Weight** – typically either maximum take‑off mass \(m\_{MTO}\) or maximum landing mass \(m\_{ML}\).
2. **Thrust available** – expressed relative to the maximum thrust available (e.g. AEO or OEI power setting).
3. **Landing gear configuration** – whether the gear is extended (↓) or retracted (↑).
4. **Wing flap configuration** – configuration of the high‑lift devices (landing, take‑off, or cruise).

The text also highlights that multi‑engine airplanes must consider climb‑gradient tables for different numbers of engines (two, three or four), since regulations prescribe stricter gradients as the number of engines increases.

# Source: ./Assignment_3.8/notes.md

# Emergency Exit Requirements (Part 1 pp. 36-38)

The regulations in CS/FAR‑23 and CS/FAR‑25 require that passengers must be able to evacuate the aircraft within **90 seconds**. During conceptual design this requirement is addressed through rules on the number, type and distribution of exits.

## CS 23.807 Highlights
- At least one exit opposite the main passenger door for aircraft with two or more seats (excluding canopy aircraft).
- Exits must open from inside and outside and provide a clear opening of **48 × 66 cm**.
- Commuter aircraft require additional exits:
  - For up to 15 passengers, one exit per side.
  - For 16–19 passengers, three exits: one on the entry door side and two on the opposite side.

These limits ensure compliance with the 90‑second rule and guide fuselage layout early in design.

## CS 25.807 Highlights
- Exits must be **uniformly distributed** with floor-level exits near each end of the cabin when more than one per side is needed.
- No passenger exit may be more than **18.3 m** from the next exit on the same side.
- The allowed passenger capacity per exit depends on exit type. Table 1 summarizes the standard exit types and maximum passengers per side.

### Table 1 – Passenger capacity per exit type

| Exit Type | Max passengers (each side) |
|----------|---------------------------|
| Type A   | 110 |
| Type B   | 75 |
| Type C   | 55 |
| Type I   | 45 |
| Type II  | 40 |
| Type III | 35 |
| Type IV  | 9  |

Additional rules for seating configurations:
1. Up to 9 seats: one **Type IV** (or larger) exit per side, or at least a **Type III** if no over‑wing exits.
2. More than 9 seats: all exits must be **Type III** or larger.
3. 10–19 seats: at least one **Type III** (or larger) per side.
4. 20–40 seats: two exits per side, one being **Type II** or larger.
5. 41–110 seats: two exits per side, one being **Type I** or larger.
6. More than 110 seats: at least two **Type I** or larger per side.
7. Maximum combined seating for all Type III exits is **70**.
8. If Type A/B/C exits are installed, at least two Type C (or larger) exits are required per side.

## Impact on Fuselage Design
Determining exit number and location dictates fuselage structural openings, door mechanisms and seat layout. Designers must balance the required exit spacing with structural integrity and cabin arrangement, influencing fuselage length and window/door placement.


# Source: ./Assignment_3.9/notes.md

# Reference Aircraft Selection Notes

This summary is based on Part 1, pp. 50–52, which discuss how to pick suitable reference aircraft at the start of the design process.

## Why use reference aircraft?
* To make initial assumptions before analysis results are available.
* Choose aircraft with similar Top Level Aircraft Requirements (TLARs) to your design.
* Newer aircraft usually have technology closer to what you need; older aircraft may provide historical context but might not match modern technology.
* Typically select 5–10 aircraft; more recent examples take priority when available.

## Example from the text
The book illustrates selecting five regional airliners (~50 passengers, range ≈ 1000 km) as reference aircraft:
ATR 42‑600, Antonov An‑148, Bombardier CRJ700, De Havilland Canada Dash 8 Q400, and Fokker 50.

## Recommended data to collect for each reference
* **Manufacturer**
* **Aircraft name**
* **Entry‑into‑service year**
* **Number of passengers**
* **Maximum payload mass (kg)**
* **Maximum range (km or nmi)**
* **Maximum take‑off mass (MTOM)**
* **Empty mass or operating empty mass (OEM)**
* **Wing area (m²)**
* **Wing span (m)**
* **Maximum take‑off power or thrust**
* **Photo** showing the aircraft

## Pros and cons of different references
* **Newer aircraft** – closer to current technology and regulations.
* **Older aircraft** – may differ in available technology but can offer additional examples if modern references are scarce.
* Prioritize aircraft that best match your TLARs, even if passenger count or range is slightly different.

## Plotting OEM vs. MTOM
The assignment suggests creating a diagram with operating empty mass (OEM) on the vertical axis and maximum take‑off mass (MTOM) on the horizontal axis, plotting each reference aircraft as a point. This helps visualize how your selected references compare in terms of mass distribution.

# Source: ./Assignment_4.1/notes.md

# Choosing an Energy Carrier

This summary covers the main points from **Part 1, page 55** of the course reader regarding selection and integration of the onboard energy source. Storing the energy in the wing is preferred when possible because the wing volume is usually not needed for payload, and wing tanks reduce bending moments on the structure. When wing storage is not feasible, the fuselage or external tanks may be used, especially for cryogenic fuels. The three broad energy carrier options are:

- **Conventional liquid fuel** (kerosene, avgas, diesel, etc.)
  - High mass-specific and volumetric energy.
  - Infrastructure and handling are well established.
  - Significant CO₂ and pollutant emissions.
- **Cryogenic fuel** (LH₂ or LNG)
  - Can lower or eliminate CO₂ emissions in operation.
  - Requires insulated pressurized tanks that add weight and take up volume.
  - Effective specific energy depends on tank efficiency.
- **Battery**
  - Very efficient conversion to propulsion power and no emissions in flight.
  - Mass does not decrease with discharge and charging is slow.
  - Needs thermal management and cannot be fully discharged.

Placeholder values from Table 4.1 illustrate the relative magnitude of specific energy (MJ/kg):

| Energy carrier       | Spec. energy (MJ/kg) |
|----------------------|---------------------|
| Jet A               | ~43                 |
| LH₂ (physical)      | ~120                |
| LNG                 | ~49                 |
| Biofuel/kerosene    | ~44                 |
| Li‑ion battery      | ~1.1                |

These figures show why hydrocarbon fuels remain attractive from a performance perspective. Cryogenic fuels and batteries offer environmental benefits but come with integration challenges. The location of the tanks or battery packs has a large influence on the airplane configuration and structure.

# Source: ./Assignment_4.2/notes.md

# Notes on Energy Carrier Storage (Part 1 p.56)

## Deciding Where to Store the Energy Carrier
- Once the energy carrier has been selected, it must be integrated into the airframe. The two most common locations are the wing and the fuselage.
- **Wing tanks** utilize otherwise empty wing volume and reduce wing bending moments by providing bending moment relief, which can lower wing weight. This leads to the rule of thumb: *if the energy carrier can be stored in the wing, it should be stored in the wing*.
- **Fuselage tanks** may be necessary when wing storage is impractical—e.g., detachable wings on small aircraft or cryogenic fuels that require large pressurized tanks which cannot fit within the wing. External tanks under the wing are also an option.

## Initial Efficiency Assumptions for Cryogenic Fuels
- Cryogenic fuels require additional volume to allow fuel boil-off. The volumetric efficiency is therefore assumed to be $\eta_V = 0.85$.
- Tank mass significantly affects the usable energy. A gravimetric efficiency of $\eta_f = 0.4$ is assumed, meaning 40% of the tank-plus-fuel mass is fuel.
- These efficiencies lead to reduced effective specific energy and energy density for fuels like liquid hydrogen or LNG.


# Source: ./Assignment_4.3/notes.md

# Propulsion System Selection and Integration (Part 1 pp.61-62)

## Key Points
- Different engine counts and mounting locations each bring distinct trade-offs.
- **Single propeller** aircraft normally use a nose-mounted tractor arrangement for best propeller efficiency. A rear pusher needs a foreplane and shifts the wing aft.
- **Twin propeller** designs commonly mount engines below the wing in tractor configuration. An inline tractor/pusher pair reduces yawing moment after an engine failure but complicates landing gear and tail integration.
- **More than two propellers** are usually wing mounted. Four engines lessen thrust loss after an engine outage and may be required when individual engines lack sufficient power. Distributed propulsion with many small motors can ease landing gear design and maintain efficiency.
- **Jet engines** may be wing mounted or fuselage mounted. Wing mounting lightens bending loads but introduces aerodynamic interference and debris ingestion risk. Fuselage mounting gives a clean wing and smaller yawing/pitching effects but increases wing structural mass and may need a raised tail. Over‑the‑wing installations permit short landing gear yet require careful aero‑structural design.

## Assignment 4.3 Questions
a. What propulsion system do you choose for your airplane? Why?

b. What is the cruise speed or cruise Mach number of your airplane?

c. How many engines/motors have you selected for your design? Please, motivate this decision.

d. How do you intend to integrate the engines/motors with your airframe? Why do you choose this integration solution?

e. For propeller airplanes, how do you intend to comply with blade failure requirements for the chosen configuration? See Example 3.19 for more details on blade failure.

f. For turbine engines, how do you intend to comply with turbine-disk failure requirements for your chosen configuration? See Example 3.18 for more details on turbine-disk failure.

g. Has the integration of the propulsion system changed your design decision regarding the wing configuration? If so, explain.

**Placeholder Cruise Speed:** _(insert final cruise speed/Mach once determined)_

# Source: ./Assignment_4.4/notes.md

# Wing Configuration Choice (Part 2 p. 68)

This page discusses the three main wing positions described on p. 68 of Part 2 and gives initial reasoning on which to adopt for our design.

## High‑Wing
**Advantages**
- Fuselage can be close to the ground, easing cargo loading/unloading.
- Engines sit higher above the ground, reducing risk of debris or water ingestion.
- Landing gear may be fuselage mounted so the aircraft can "kneel" for ramps.
- Provides greater lateral stability in sideslip.

**Disadvantages**
- Wing‑mounted main gear would be tall; fuselage‑mounted gear requires external sponsons, increasing drag and mass.
- Wing is high off the ground, making inspection and fueling more difficult.

## Low‑Wing
**Advantages**
- Short, wide‑track landing gear integrated directly in the wing box for low weight and drag.
- Easy access to wing and engines for fueling or maintenance.
- Common choice for passenger aircraft, so airport servicing equipment exists.

**Disadvantages**
- Fuselage sits higher from the ground; often needs stairs or lifts for boarding and cargo.
- Lower lateral stability (can be offset with wing dihedral).
- Ground clearance for engines or propellers may require taller gear or fuselage‑mounted engines.

## Mid‑Wing
**Advantages**
- Little or no wing‑body fairing is needed, minimizing friction drag.
- Wing‑body blending reduces aerodynamic interference.
- Lateral stability unaffected; good pilot visibility.

**Disadvantages**
- Difficult structural integration because highest bending loads occur at the wing root.
- For passenger aircraft the wing box would pass through the cabin; alternatively the wing must be behind the cabin, complicating balance.
- Engine inlet ducts may interfere with wing structure on combat aircraft.

## Initial Choice for the Project
Our top‑level requirements (e.g. around 87 passengers and a 2100 km design range) suggest a regional passenger transport. For such aircraft, a low‑wing layout offers efficient landing‑gear integration and straightforward engine installation while keeping drag and weight down. Although a high‑wing improves lateral stability and ground clearance, the added structural drag and servicing complications make it less attractive. A mid‑wing would complicate the fuselage structure. Therefore the **low‑wing** configuration is the most suitable starting point for our project.

# Source: ./Assignment_4.5/notes.md

# Landing Gear Layout Decision (Part 2 p.69)

Part 2 discusses two main landing gear arrangements and gives guidance on how to choose
between them. The assignment on page 69 asks which layout you select and where you
will attach the landing gear to the airframe.

## Conventional or "tail-dragger" landing gear
- Main wheels are ahead of the center of gravity with a small tail wheel.
- Allows three-point or tail-wheel landings that reduce speed quickly thanks to the
  nose-high attitude.
- High propeller clearance during taxiing.
- Drawbacks: poor forward visibility while taxiing, increased drag during take-off
  until the tail lifts, possibility to bounce in a two-wheel landing, and risk of
  nose-over or ground loop because the center of gravity is behind the main gear.

## Tricycle landing gear
- Places the center of gravity ahead of the main gear, preventing ground loops and
  nose-overs.
- Keeps the aircraft level on the ground for lower drag and easier passenger and
  cargo loading.
- Good over-the-nose visibility and tends to place the nose wheel firmly on the
  runway after a hard landing.
- Heavier than a tail wheel because the nose gear must carry high loads and the
  airframe requires local reinforcement at the nose gear attachment.

## Attachment points
- Structural frames in the fuselage provide attachment points for the wing, tail
  and possibly the landing gear. Some frames are strengthened with plates and act
  as bulkheads to distribute concentrated loads.

## Retractable vs. fixed gear (placeholder)
- The text continues with a discussion on whether the landing gear should retract
  or remain fixed. A retractable system lowers drag but adds mass, complexity and
  maintenance requirements. Further analysis is needed for our design choice.

# Source: ./Assignment_4.6/notes.md

# Tail Configuration Options (Part 2, pp. 70–72)

This note summarizes the discussion in **Airplane Design Part 2** on the various tail configurations and how they relate to overall aircraft layout. The text covers conventional arrangements as well as more exotic options and stresses matching the tail choice with the wing position and propulsion installation.

## Common configurations

### Low tail
- The horizontal and vertical tails attach directly to the fuselage, making integration simple.
- Staggering one surface ahead of the other on the fuselage helps reduce aerodynamic interference.
- Works well with most wing positions, although propeller slipstream or jet exhaust can reduce its effectiveness if the wing or engines are mounted high.

### Cruciform tail
- Moves the horizontal tail halfway up the vertical fin.
- Keeps the tail relatively close to the fuselage so only part of the fin structure must carry tailplane loads, saving weight compared with a T‑tail.
- Allows a lower taper ratio on the vertical fin, further reducing weight.
- Useful when a low tail would be immersed in wing wake or propeller slipstream but full T‑tail height is unnecessary.

### T-tail
- Places the horizontal tail on top of the vertical fin for maximum vertical separation from the wing.
- Yields high stabilizing effectiveness and can allow a smaller tailplane, reducing drag. The horizontal tail also end‑plates the vertical tail for better yaw effectiveness.
- Requires a strong fin to carry loads, often leading to high aspect ratio limitations and a taper ratio near one to provide area at the tip.
- Vulnerable to deep stall if the wing’s wake blankets the tail at high angle of attack. Some aircraft use stick‑pusher or flight envelope protections to avoid this.

## Other configurations

### Multiple vertical tails
- Twin or triple fins add redundancy and can lower overall height to fit hangars.
- End‑plate effect when fins are placed on the tips of the horizontal tail increases tail effectiveness.
- Increase part count and may suffer aerodynamic interference if positioned too close together.

### V-tail
- Uses two surfaces arranged in a V to provide both pitch and yaw control (using "ruddervators").
- Reduces total tail area and thus friction drag.
- Ruddervator deflections for yaw also introduce a rolling moment to the opposite side, which needs to be managed.

### Inverted Y-tail
- Similar to a V-tail but with an additional ventral fin forming an inverted Y.
- Avoids the adverse roll‑yaw coupling of a V-tail.
- Proximity to the ground can limit rotation angle during takeoff and landing but protects a rear propeller from striking the ground.

### Twin‑boom
- Two tail booms extend from the wings with a tailplane between them. Often chosen when an aft-mounted engine prevents a central tail boom.
- Frequently paired with a T-tail to keep the tailplane clear of jet exhaust.

### Tailless arrangements
- Flying wings, blended‑wing‑bodies and flying‑V designs eliminate horizontal tailplanes entirely.
- Offer low weight and drag with high internal volume efficiency, but integrating stability and control into the wing is complex.

## Synergies with wing position
- A low fuselage tail is easiest to integrate with a low or mid wing. High-mounted wings or wing‑mounted engines can interfere with a low tail, favoring a cruciform or T‑tail.
- A high wing combined with a T-tail provides ample separation of the lifting surfaces but may be prone to deep stall if the wing stalls first.
- V‑tails or twin‑boom tails can be advantageous for pusher configurations, where the tail must avoid the propeller slipstream.
- The choice of tail should therefore be made together with decisions on wing placement and propulsion layout to avoid aerodynamic interference and structural penalties.


# Source: ./Assignment_5.1/notes.md

# Aspect Ratio Choice (Part 2 pp. 82–83)

Part 2 emphasises that the wing aspect ratio $A_w$ is a key design parameter. A large
aspect ratio decreases lift‑induced drag, improving the maximum lift‑to‑drag ratio
in Eq. (5.12), but it also makes the wing slender and structurally heavy. Lower
aspect ratio wings are lighter yet suffer more induced drag. Because the trade‑off
cannot be quantified at this early stage, designers are advised to inspect
reference aircraft to see which aspect ratios are feasible.

**Assignment guidance (5.1):**
1. Compute $A_w=b^2/S$ for each reference aircraft using their wing span $b$ and
   reference area $S$.
2. Choose an aspect ratio for your design and justify it by comparing with the
   reference aircraft values.
3. Discuss how your choice is expected to influence induced drag, wing mass and
   the internal volume for fuel/systems.

This qualitative reasoning helps pick a practical value before detailed structural
analysis is available.

# Source: ./Assignment_5.2/notes.md

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

# Source: ./Assignment_5.3/notes.md

# Oswald Efficiency Factor Estimation

Based on *Airplane Design Part 2*, page 85, the Oswald efficiency factor `e` accounts for changes in lift‑induced drag compared to an ideal wing. For a configuration without flap deflection, the induced drag is modeled as:

\[
C_{D_i} = \psi \, C_L^2 + \frac{C_L^2}{\pi A_w \phi}
\]

where `ψ` is a parasite drag parameter depending on lift coefficient and `φ` is the span efficiency factor.

Equation (5.17) provides `e` as:

\[
e = \frac{1}{\psi \, \pi A_w + \tfrac{1}{\phi}}
\]

**Example assumptions**

1. Take the parasite drag parameter as `ψ = 0.0075`.
2. Assume the span efficiency factor `φ = 0.83`.
3. Using the equation above yields `e ≈ 0.71` for the example four‑seat aircraft.

These assumptions match those used for the dashed trend line in Figure 5.5.

# Source: ./Assignment_5.4/notes.md

# Propulsion System Efficiencies (Part 2 pp. 90-91)

This section introduces how the bypass ratio of a turbofan influences fuel consumption and explains how to choose efficiency values for different propulsion types.

* **Turbofan TSFC relation** – For cruise conditions the thrust specific fuel consumption (TSFC) depends on the bypass ratio B. Using published data the following relation applies for 1 ≤ B ≤ 15:

  \[\text{TSFC} = 22 B^{-0.19} \;[\text{g}/\text{kN}/\text{s}]\]

  This allows estimating the jet efficiency via Eq. (5.21). Increasing B generally improves efficiency but makes the engine diameter larger.

* **Assignment 5.4 inputs** – To evaluate propulsion performance provide the following according to the engine type:
  - If using an **electric motor**, assume a motor efficiency \(\eta_{em}\).
  - For **piston or turboprop engines**, assume a (thermal) engine efficiency \(\eta_{eng}\).
  - When a **propeller** is present, specify the propulsive efficiency \(\eta_p\).
  - For **turbofan engines**, select a bypass ratio B and compute the resulting jet efficiency \(\eta_j\).

These values are needed for later calculations of range and energy usage.

# Source: ./Assignment_5.5/notes.md

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

# Source: ./Assignment_5.6/notes.md

# Notes: Estimating Operating Empty-Mass Fraction (Part 2 pp. 94-96)

- The unity equation links mass fractions of the aircraft. After fuel/battery mass is set, the remaining unknown is the (operating) empty-mass fraction $m_{OE}/m_{MTO}$.
- Distinguish **empty mass** from **operating empty mass**:
  - For small aircraft the crew is part of the payload, so empty mass is often used.
  - Larger aircraft usually have crew plus additional operational items separate from payload, so the operating empty mass must be considered.
  - Decide whether to use $m_E$ or $m_{OE}$ by checking what is reported for the reference aircraft.
- To estimate $m_{OE}/m_{MTO}$, gather data from reference airplanes similar in passenger capacity, range and technological level.
- Example 5.9 demonstrates the approach for a four-seat twin piston‑prop design. Six reference aircraft are listed with their range, maximum take-off mass and empty mass, yielding empty-mass ratios around $0.62$–$0.68$.
- Consider influence of mission range and year of first flight:
  - Range differences affect fuel mass fraction and thus empty-mass fraction.
  - Newer aircraft tend to be lighter due to improved technology, so recent designs may be more representative.
- After assessing range and technological similarity, select a reasonable value (e.g., in the example a value of $m_E/m_{MTO} \approx 0.64$ close to the mean was chosen).
- Discard reference aircraft whose range is far from requirements or that are outdated in technology.
- Use this estimated fraction as a starting point; later design phases (e.g., Chapter 12) refine the (operating) empty mass calculation.


# Source: ./Assignment_5.7/notes.md

# Assignment 5.7 Notes

This section (Part 2, pp. 100–102) introduces **Assignment 5.7**, which asks you to calculate the characteristic masses of your airplane and then plot the result on the reference diagram from Assignment 3.9.

## Tasks

1. **Compute Maximum Take-Off Mass (MTOM)** – determine the total mass at take-off based on payload, empty mass and energy mass.
2. **Compute (Operating) Empty Mass (OEM)** – estimate the mass of the structure, installed systems and any operational items such as crew and catering.
3. **Compute Energy Mass in the Design Condition** – quantify how much fuel or battery mass is needed to fly the design mission.
4. **Compute Reserve Energy Mass** – determine the additional energy mass needed for contingencies (diversion, holding, etc.).
5. **Plot on Reference Diagram** – place your aircraft’s point on the Assignment 3.9 diagram and compare it with the reference aircraft data.

## Context

After obtaining these values you can gauge where your design sits relative to regulations (e.g. CS/FAR 23 limits) and you can proceed with subsequent sizing and performance analysis. The text emphasizes keeping track of earlier design choices—such as energy carrier, aspect ratio and propulsion system—because they influence your mass estimates and the overall design process.

# Source: ./Assignment_5.8/notes.md

# Payload-Range Diagram Notes (Part 2 p.103)

The text on p.103 continues the discussion on constructing the payload–range
(PR) diagram. When extra tank volume is available, payload can be traded for
additional fuel once the design range is exceeded. Doing so moves the **second
kink** in the PR diagram—as well as the **ferry‑range point**—to the right.

## Steps from Assignment 5.8
The page lists the tasks for creating a PR diagram:

1. **State the design range and design payload.**
2. **Check for a maximum structural payload requirement.** If one exists,
   report the mass $m_{pl\,max}$ and compute the achievable range at this
   payload.
3. **Compute the ferry range** for $m_{pl}=0$.
4. **Plot the PR diagram** using the results from the previous steps.

## Identifying Key Points
- **Maximum structural payload** corresponds to the highest payload mass the
  aircraft structure is permitted to carry. For fuel‑powered aircraft the
  available fuel with this payload is
  \[m_f = m_{MTO} - m_{OE} - m_{pl\,max}\]【F:Airplane_Design_Part_2.pdf†L1814-L1822】.
  The associated range is found with the Breguet equation, subtracting the
  auxiliary range.
- **Ferry range** is the maximum distance flown with no payload. It is
  computed by setting $m_{pl}=0$ in the range equation while using the same
  fuel mass as for the design condition. The page notes that practical ferry
  range might include the mass of a pilot if one is required to fly the
  aircraft【F:Airplane_Design_Part_2.pdf†L1725-L1755】.

Use these points—design payload, any maximum structural payload, and ferry
range—to sketch the complete payload–range diagram.

# Source: ./Assignment_6.1/notes.md

# Notes on Fuselage Payload Distribution (Part 2 pp.118-120)

## Overview
These pages discuss considerations for arranging passenger and cargo volumes in the fuselage. Designers are asked to determine how much of the design payload must be allocated to passengers, luggage and cargo, then distribute these volumes under or behind the cabin floor. A key decision is whether to use bulk storage or unit load devices (ULDs) for baggage and freight.

## Bulk vs. Container Loading
**Bulk loading** (loose bags placed in the hold)
- + Low equipment cost and simpler ground handling.
- + Flexible for irregular luggage shapes or small aircraft.
- - Labor intensive loading/unloading.
- - Harder to secure and organize; risk of damage or misplacement.

**Container/ULD loading**
- + Speeds up turn-around because containers are pre-packed and moved as units.
- + Protects luggage/cargo and uses space efficiently.
- - Requires standardized containers and supporting equipment, increasing weight and acquisition cost.
- - Floor height and cross-section must fit container dimensions, limiting design freedom.

## Passenger and Luggage Assumptions (placeholders)
- Average passenger mass: **95 kg** (including 15 kg carry-on).
- Checked luggage per passenger: **20 kg**.
- Assume typical cargo density around **160 kg/m³** and luggage density around **200 kg/m³** for volume estimates.

## Distributing Payload in the Fuselage
1. Compute passenger cabin dimensions (seats abreast, aisle width, etc.) to size the cross-section.
2. Evaluate under‑floor volume to see if bulk or containerized holds fit beneath the passenger deck.
3. Allocate remaining fuselage volume aft of the cabin for additional cargo if needed.
4. Choose bulk or ULD based on desired ground operations speed, available equipment, and structural considerations.

These guidelines help ensure the fuselage layout meets payload requirements while keeping the envelope compact to minimize structural weight and drag.

# Source: ./Assignment_6.2/notes.md

# Fuselage Cross-Section Design (Part 3 p.125)

This section provides an example-based method to size the fuselage cross-section. The design is illustrated with an eight-step sequence that starts from seat and aisle dimensions and finishes with the location of overhead bins. The steps are as follows:

1. **Set cabin dimensions** – Use eq. (6.5) along with Tables 6.2–6.3 to select the seat arrangement and aisle width. Compute cabin width $w_{\text{cabin}}$, floor width $w_{\text{floor}}$, and headroom width $w_{\text{headroom}}$ using eqs. (6.6)–(6.8). Record armrest, shoulder and headroom heights.
2. **Choose drawing scale** – Select the paper width and derive an appropriate scale (e.g. 1:20) based on $w_{\text{cabin}}$.
3. **Draw blocks** – Sketch rectangles for the seat rows and aisle. Add a symmetry line to indicate the center plane.
4. **Add floor depth** – Draw the passenger floor beneath the seats with the chosen floor depth.
5. **Insert cargo shape** – If required, draw the cargo container or luggage volume below the passenger floor.
6. **Fit an inner circle** – Enclose the seat blocks and cargo with the smallest possible circle. The circle diameter is $d_{f,\text{inner}}$.
7. **Determine outer diameter** – Apply eq. (6.3) to offset the circle by the wall thickness $t_{\text{wall}}$ and obtain $d_{f,\text{outer}}$. Measure deck heights $h_{\text{ld}}$ and $h_{\text{md}}$ from the lowest point.
8. **Trace overhead bins** – Draw a dashed line representing the overhead bin perimeter while maintaining aisle and headroom clearances.

The **perimeter length** of a circular fuselage section is the circumference of the outer circle, computed as
$$P_{\text{fus}} = \pi\, d_{f,\text{outer}}.$$
For a non-circular section the perimeter should be measured along the drawn outline.

# Source: ./Assignment_6.3/notes.md

# Fuselage Top View Design Notes

Summary of Part 3 p.128 describing how to draw the fuselage in top view.

## Key Ideas
- Minimize drag while keeping an adequate tail arm.
- Fuselage top view has three parts: nose cone, cylindrical section, and tail cone.

## Design Sequence
1. **Compute cabin length** from seating layout.
2. **Select**:
   - nose length `l_n`
   - tail-cone slenderness ratio `l_tc/d_fus`
   - tail-to-tail-cone ratio `l_t/l_tc`
   Then compute fuselage length `l_fus`.
3. Determine the drawing scale based on `l_fus` and paper size.
4. Draw fuselage length.
5. Draw fuselage width from cross-section.
6. Choose nose-cone slenderness ratio `l_nc/d_fus` and draw nose and tail cone bounds.
7. Construct fuselage perimeter in top view.
8. Draw the aft cabin wall.

## Parameters and Placeholder Values
Using the four‑seat reference aircraft from Example 6.5 as a starting point:
- `l_n` ≈ 3.0 m
- `l_nc/d_fus` ≈ 1.4
- `l_tc/d_fus` ≈ 3.1
- `l_t/l_tc` ≈ 0.8

These values act as placeholders until dimensions from the chosen reference aircraft are measured.

# Source: ./Assignment_6.4/notes.md

# Fuselage Side View Design (Part 3 p.134)

The design of the fuselage side view combines the cross-section and top-view layouts with
three main requirements:

* **Emergency evacuation** – exit doors must comply with the relevant regulations.
* **Pilot visibility** – the cockpit must offer unobstructed forward and upward vision.
* **Ground clearance** – enough clearance is needed to avoid tail strikes and nacelle contact.

The book proposes a nine‑step sequence for drawing the side view. Key steps related to the
above requirements include:

1. Determine fuselage height using the cross‑section.
2. Copy nose‑cone and tail‑cone locations from the top view.
3. Locate the flight deck and draw main and lower deck floors.
4. Set the pilot eye position and sketch the visibility angles.
5. Choose an upsweep angle for the tail cone and set the nose point height.
6. Draw the crown and belly curves.
7. Scale and locate passenger doors to meet emergency‑exit rules.

### Example angles

Example 6.7 illustrates how these steps apply. The pilot’s eye is placed 1 m behind the start
of the flight deck and 1.1 m above it, with a **20° over‑nose angle** and a **25° upward view**.
A **4° upsweep angle** is selected for the tail cone. The cockpit windshield uses a
**25° grazing angle**. For a 180‑passenger layout, two pairs of Type B exits and one pair of
Type III exits are drawn along the cabin.

These choices satisfy visibility and tail‑clearance targets while meeting evacuation spacing
requirements.

# Source: ./Assignment_7.1/notes.md

# Notes on CL_max Assumptions (Part 3 p.147)

Part 3 explains that selecting the wing's maximum lift coefficient for cruise (CL_max,CR), take‑off (CL_max,TO) and landing (CL_max,L) requires assuming plausible values before the high‑lift system is fully designed. Table 7.1 lists typical minimum and maximum CL_max values for several airplane types—homebuilts, single‑engine props, twin engines, business jets, regional turboprops and transport jets. These ranges help pick initial coefficients.

Key points:

- Landing configuration usually yields the highest CL_max, while cruise has the lowest. Take‑off settings fall between to balance added lift and the drag penalty of flaps.
- When choosing CL_max values, ensure that
  - CL_max,L ≥ CL_max,CR
  - CL_max,CR ≤ CL_max,TO ≤ CL_max,L.
- The chosen assumptions will later be refined once the high‑lift devices are specified in Chapter 10.

These assumed coefficients feed into sizing constraints, such as the stall speed requirement used in matching diagrams.

# Source: ./Assignment_7.10/notes.md

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

# Source: ./Assignment_7.2/notes.md

# Minimum-Speed Constraint Notes

This note summarizes the steps from Airplane Design Part 3 on how to include a minimum-speed requirement in the matching diagram.

1. **Specify the speed requirement** – Begin with the stall or approach speed from Assignment 3.6. Record the altitude `h`, temperature deviation `ΔT`, and mass ratio `β` associated with this requirement.
2. **Determine maximum wing loading** – Use the minimum-speed requirement to calculate the allowable take-off wing loading `W_TO/S_w`.
3. **Choose diagram bounds** – Set suitable limits for the matching diagram. Select an upper bound for wing loading and a bound for thrust-to-weight or power loading as applicable.
4. **Set up the matching diagram** – Prepare the axes using the chosen bounds and plot other constraints as needed.
5. **Draw the minimum-speed line** – Plot the constraint line that enforces the stall or approach speed. Mark the infeasible region on the diagram.

Altitude and temperature affect air density, so if the speed requirement is given for non‑standard conditions you must account for the resulting density when calculating wing loading.

# Source: ./Assignment_7.3/notes.md

# Adding Landing Field Length Constraint

Summary from *Airplane Design Part 3*, page 153:

- Equation (7.15) provides the maximum wing loading allowed by the landing-field-length requirement. The parameters involved are the landing distance `LFL`, altitude `h`, temperature deviation `ΔT`, and the mass ratio `β`.
- Example 7.4 demonstrates applying this formula for propeller and jet aircraft, yielding respective limits on `W_TO/S_w`.
- Figures 7.7 and 7.8 show matching diagrams with the new landing-field-length constraint lines for both aircraft types.
- The assignment steps are:
  1. State `LFL`, `h`, `ΔT`, and `β` for your own aircraft.
  2. Compute the corresponding air density `ρ`.
  3. Calculate the maximum wing loading implied by the landing field length.
  4. Add this constraint to your matching diagram and determine the resulting maximum wing loading.

# Source: ./Assignment_7.4/notes.md

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

# Source: ./Assignment_7.5/notes.md

# Cruise-Speed Constraint Curve (Part 3, pp. 160-161)

- The thrust-to-weight ratio required to meet the cruise speed can be plotted as a curve on the matching diagram. 
- For the aircraft to satisfy this requirement, its thrust-to-weight ratio for any given wing loading must lie above this curve.
- Lower wing loadings demand higher thrust (or power) to maintain cruise speed at altitude, due in part to engine thrust lapse with altitude.
- **Assignment 7.5 tasks:**
  1. Using the cruise conditions from Assignment 7.4, determine the engine lapse ratio \(\alpha_P\) or \(\alpha_T\).
  2. If a cruise Mach number is specified, compute the cruise speed \(V_{CR}\) with equation (7.30).
  3. Tabulate power loading or thrust-to-weight ratio versus wing loading, following the method in Example 7.5.
  4. Plot the resulting cruise-speed constraint curve on the matching diagram.

# Source: ./Assignment_7.6/notes.md

# Rate-of-Climb Constraint (Part 3 p.165)

This page outlines how to build the rate-of-climb constraint for the matching diagram. The key steps are:

1. **State the requirement** – specify climb rate $c$, altitude $h$, weight fraction $\beta$, and temperature deviation $\Delta T$.
2. **Find atmospheric properties** – compute $T$, $p$, and $\rho$ at the given altitude and temperature.
3. **Determine the optimal lift coefficient** where the highest climb rate occurs.
4. **For a range of wing loadings**, calculate the speed that yields the best climb rate.
5. **(Jet only)** Compute the corresponding Mach number for each wing loading and determine the total temperature ratio $\theta_t$ and total pressure ratio $\delta_t$.
6. **(Jet only)** Use $\theta_t$ and $\delta_t$ to evaluate the thrust lapse $\alpha_T$.
7. **Compute take‑off power loading or thrust‑to‑weight ratio** versus wing loading.
8. **Plot the constraint** in the matching diagram.

Propeller aircraft skip the Mach number and thrust lapse calculations because the thrust lapse relation for turbofans requires additional steps.

# Source: ./Assignment_7.7/notes.md

# Drag Polar Construction

This page condenses the key steps from *Airplane Design Part 3* p.170. It describes how to estimate drag polars for different flight phases so that constraint curves can be constructed later in the matching diagram.

## Flap and Gear Effects
- **Oswald factor change** due to flap deflection is approximated using Obert's relation (Eq. 7.62). The effect is larger for fuselage-mounted engines than for wing-mounted engines.
- **Zero-lift drag increment** for flap deflection is crudely estimated as 1.3 drag counts per degree of deflection (Eq. 7.63).
- **Landing gear drag increment** adds 100–250 drag counts to the zero-lift drag coefficient (Eq. 7.64).

These relations provide quick estimates until more refined analyses are available.

## Example Configuration
- Starting cruise condition: $C_{D0}=0.0180$, $e=0.80$ and aspect ratio $A=8$.
- Flap settings examined:
  - Cruise: flaps up, gear up.
  - Take‑off 1: flaps 15°, gear up.
  - Take‑off 2: flaps 15°, gear down.
  - Landing: flaps 35°, gear down.
- For each case, Eqs. 7.62–7.64 are used to adjust $e$ and $C_{D0}$.

## Assignment 7.7 Tasks
1. Compute $e$ in cruise (Eq. 5.17).
2. Select landing flap deflection.
3. Choose an intermediate take‑off flap setting.
4. Find $C_{D0}$ for take‑off and landing with Eq. 7.63–7.64.
5. Compute $e$ for take‑off and landing using Eq. 7.62.
6. Tabulate the resulting coefficients similar to the example table.

This procedure yields a set of drag polars in cruise, take‑off and landing, allowing subsequent performance calculations.

# Source: ./Assignment_7.8/notes.md

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

# Source: ./Assignment_7.9/notes.md

# Notes on Adding Take‑Off Field‑Length Constraint (Part 3 p.179)

Part 3 page 179 describes "Assignment 7.9" where the reader builds the constraint
curve for the take‑off field‑length requirement. Steps **e**–**h** apply only to
jet aircraft. The procedure is:

1. **State the requirement** – specify the required take‑off field length `L_TO`,
   the take‑off altitude `h`, the temperature offset `ΔT`, and whether the
take‑off distance is based on all‑engine operating (AEO) or continued take‑off
after one engine inoperative (OEI).
2. **Define drag and lift parameters** – list the zero‑lift drag coefficient
   `C_D0` and Oswald factor `e` for the take‑off configuration.
3. **Compute atmospheric properties** – determine `T`, `p` and `ρ` for the
   take‑off conditions.
4. **Find the lift coefficient `C_L2`** – use the minimal allowable margin above
   stall speed to calculate `C_L2`.
5. **Determine safety speed `V₂`** – for a range of wing loadings `W/S`, compute
   the take‑off safety speed.
6. **Calculate Mach numbers** for the corresponding `V₂` values.
7. **Evaluate total temperature ratio `θ_t` and pressure ratio `δ_t`** based on
   those Mach numbers.
8. **Compute thrust lapse `α_T`** for each wing loading using `θ_t` and `δ_t`.
9. **Find the required power loading or thrust-to-weight ratio** for the take‑off
   field length requirement across the chosen wing loading range.
10. **Plot the resulting constraint curve** in the matching diagram.

These steps add the take‑off field‑length limit to the matching diagram so the
feasible design space reflects this performance constraint.

# Source: ./Assignment_8.1/notes.md

# Wing Sweep Angle Guidance (Part 3 p.188)

From Part 3 of *Airplane Design* the recommended quarter‑chord sweep angle depends on the airplane's cruise Mach number:

- **Below Mach 0.66**: no sweep is required.
- **Above Mach 0.66**: apply increasing sweep to delay compressibility effects. For instance at a cruise Mach number of 0.78 a sweep of about 25° is suggested.

The cruise Mach number is computed from the cruise speed using the local speed of sound. Modern airfoils allow sufficient structural thickness without sweep at low Mach numbers. When Mach number exceeds roughly 0.66, sweep is used to keep the effective Mach number normal to the quarter chord below the critical value while providing enough wing volume for fuel and systems.

# Source: ./Assignment_8.10/notes.md

# Determining Engine/Motor Dimensions and Envelope

Summary of the approach presented in *Airplane Design Part 3* p.221 for sizing a nacelle (engine enclosure):

- The cone at the exit of the gas turbine is sized using:
  - $$D_c \approx 0.55 D_{eg}$$
  - $$l_c \approx 1.5 D_c$$
- With these dimensions, the nacelle layout can be drawn. Example 8.14 describes the procedure for a jet engine (Type C nacelle, fan cowl fraction \(\phi=0.75\)):
  1. **Inlet diameter** \(D_i\) from mass flow using Eqs. (8.24)--(8.25). Example: \(D_i = 1.6\,\text{m}\).
  2. **Highlight diameter** \(D_h\) (droop neglected). Often set equal to the inlet diameter.
  3. **Nacelle length** \(l_n\) via Eq. (8.27) and Table 8.1. Example: \(l_n = 4.8\,\text{m}\).
  4. **Fan cowling length** \(l_f\) from Eq. (8.28). Example: \(l_f = 3.6\,\text{m}\).
  5. **Position of maximum diameter** located at \(\beta l_f\) using Table 8.1. Example: \(\beta = 0.39\) \(\Rightarrow\) 1.4 m from the highlight plane.
  6. **Maximum diameter** \(D_n\) from Eq. (8.29). Example: \(D_n = 1.9\,\text{m}\).
  7. **Fan cowling exit diameter** \(D_{ef}\) via Eq. (8.30). Example: \(D_{ef} = 1.5\,\text{m}\).
  8. **Gas turbine diameter at fan cowl exit** \(D_g\) from Eq. (8.32). Example: \(D_g = 1.0\,\text{m}\).
  9. **Gas turbine exit diameter** \(D_{eg}\) from Eq. (8.33). Example: \(D_{eg} = 0.56\,\text{m}\).
  10. **Cone size** using the relations above for \(D_c\) and \(l_c\). Example: \(D_c = 0.36\,\text{m}\) and \(l_c = 0.54\,\text{m}\).
  11. **Draw the nacelle outline** with all computed dimensions.
  12. **Connect the points** to complete the nacelle envelope.

The example ends by noting that a symmetry line is used as a reference when drawing because the nacelle is assumed axisymmetric. Assignment 8.15 encourages repeating these steps for a specific design.

# Source: ./Assignment_8.11/notes.md

**Integration of Nose-Mounted Propellers with Cowlings**

Summary of *Airplane Design Part 3* page 212:

- The engine and propeller should be integrated into the nose of the fuselage in the top, side, and front views.
- A well-shaped engine cowling must be added to provide a smooth transition between the engine and fuselage surfaces.

These steps ensure the propeller installation is aerodynamically clean and fits within the overall fuselage design.


# Source: ./Assignment_8.12/notes.md

# Notes on Wing-Mounted Propeller Fairings (Part 3 p. 214)

- When a fairing is added around wing-mounted engines, a sizable volume forms behind the engine. Designers may allocate this space for functions such as baggage or fuel storage.
- In the example, the fairing's trailing edge is kept horizontal because the engine envelope is wider than it is tall, though its exact shape can be adjusted aesthetically.
- Integrating electric motors with the wing uses the same steps as piston engines. All guidelines for propeller-wing integration from p. 212 remain valid. With smaller electric motor envelopes, ensure enough distance between the leading edge and the propeller disk.
- Turboshaft engines can also follow piston-engine integration guidelines. Example 8.13 illustrates mounting turboshafts on a high‑wing transport aircraft.
- For the example, inboard engines are positioned so their envelopes touch the front spar while maintaining a clearance of **0.15 Dp** from the fuselage side to the propeller tip.

# Source: ./Assignment_8.13/notes.md

# Assignment 8.13 Notes

Summary of Airplane Design Part 3 p.218 on sizing jet-engine mass flow.

The mass flow rate \(\dot{m}\) required for a turbofan engine at take-off is computed using the thrust requirement and key engine parameters:

- **Bypass ratio** \(B\) is the ratio of air through the fan duct to that through the core.
- **Turbine inlet temperature** \(T_{t4}\) influences the gas generator function \(G\). Higher TIT allows a smaller mass flow for the same thrust but increases NO\(_x\) emissions.
- **Number of engines** \(N_e\), speed of sound at sea level \(a_0\), nozzle efficiency \(\eta_{\text{noz}}\), and combined turbine/fan efficiency \(\eta_{tf}\) also enter the calculation.

Equation (8.22) relates these parameters to the required mass flow:

\[
\dot{m}=\frac{T_{TO}(1+B)}{N_e\,a_0\,\eta_{\text{noz}}\,G\,(1+\eta_{tf}B)}.
\]

Here \(T_{TO}\) is the total thrust at take-off. The gas generator function \(G\) depends on TIT via

\[
G\approx\frac{T_{t4}}{600}-1.25\tag{8.23}
\]

A higher \(T_{t4}\) (typically 1830–1970 K for modern engines) reduces the mass flow needed per unit thrust, enabling a smaller and lighter nacelle.

The assignment asks to choose \(B\) and \(T_{t4}\) for your design, assume values for \(\eta_{tf}\), \(\eta_{\text{noz}}\), and \(G\), and compute \(\dot{m}\) accordingly.


# Source: ./Assignment_8.14/notes.md

# Assignment 8.14 – Selecting a Turbofan Nacelle Type

Part 3 p.219 describes three nacelle configurations. Type A is meant for turbojet engines and is not considered for turbofan installations. The two relevant types for turbofans are:

- **Type B** – a full-length nacelle that encloses both the fan bypass flow and the gas‑turbine core. The bypass and core flows mix ahead of the nozzle, improving thrust-specific fuel consumption and reducing noise. The downside is a larger wetted surface and therefore more friction drag.
- **Type C** – a split design consisting of a shorter fan cowl combined with a separate core cowl. This exposes part of the engine core, decreasing wetted area compared with Type B. However, without forced mixing it may not reduce noise and fuel burn as effectively.

Both configurations assume an axisymmetric approximation in the textbook, even though real nacelles are slightly drooped. Choosing between Type B or Type C involves balancing drag versus mixing/noise advantages.

# Source: ./Assignment_8.15/notes.md

# Nacelle Sizing Assignment Summary

This summary is based on **Part 3 p. 223** of the design notes. Assignment 8.15 focuses on computing dimensions for a turbofan engine nacelle and creating a scaled drawing. Key instructions include:

- Select a cowl fraction \(\phi\) for the nacelle. If the nacelle type is **B**, then \(\phi = 1\).
- Follow the sizing procedure from Example 8.14 to determine:
  - Inlet/highlight diameter \(D_h = D_i\)
  - Nacelle length \(l_n\)
  - Fan cowling length \(l_f = \phi l_n\)
  - Location of maximum diameter at \(\beta l_f\)
  - Maximum diameter \(D_n\)
  - Fan cowl exit diameter \(D_{ef}\)
  - Gas-turbine cowling diameter at the fan cowl exit \(D_g\)
  - Gas-turbine exit diameter \(D_{eg}\)
  - Cone diameter \(D_c\) and length \(l_c\)
- Record these values in a table for reference.
- Draw the nacelle outline using the computed dimensions. Apply the same drawing scale used for previous fuselage and wing assignments.


# Source: ./Assignment_8.16/notes.md

Part 3 page 226 discusses how under-wing jet engines are mounted using a pylon connecting the nacelle to the wing box.
Key points include:
- **Lateral positioning**: Outboard placement relieves wing bending but increases yawing moment in an engine-out case. Typical lateral positions are 35% of semi-span for one engine per wing half, or 40% and 70% when two per wing half.
- **Longitudinal positioning**: Rotating parts should be kept ahead of the front spar to mitigate turbine disk failure risks. The engine should sit as far forward as practical to reduce aerodynamic interference, while remaining close to the wing box to minimize pylon mass.
- **Vertical positioning**: Moving the engine closer to the wing increases aerodynamic interference but improves ground clearance. Lower engines may require taller landing gear, whereas higher placement shortens the moment arm between thrust vector and center of gravity, reducing pitching moment.

Example 8.15 illustrates these principles by integrating a sample nacelle with the wing in top, front and side views. The assignment that follows (8.16) instructs designers to integrate their own under-wing engine(s) in these three views and to mark the pylon location in the front view.

# Source: ./Assignment_8.17/notes.md

The assignment on page 229 of Part 3 instructs you to integrate fuselage-mounted jet engines into your aircraft views and mark the pylon locations:

* Draw the engines attached to the fuselage in the top, side and front views.
* In the top and front views, add lines showing where the pylons meet the fuselage and nacelle.

# Source: ./Assignment_8.2/notes.md

# Wing Taper Ratio Guidance

This summary is based on Part 3 p.189 of **Airplane Design**.

- **Definition**: The taper ratio \(\lambda\) is the tip chord divided by the root chord.
- **Manufacturing**: A rectangular planform (\(\lambda = 1\)) simplifies rib geometry and joints, lowering cost. Tapering increases manufacturing effort.
- **Lift Distribution**: Reducing tip chord shifts lift inboard. Combined with sweep, taper alters how lift varies along the span and therefore affects induced drag.
- **Induced Drag**: With no sweep, a taper ratio near 0.4 produces an almost elliptical lift distribution, minimizing induced drag.
- **Structural Mass**: Concentrating area at the root lowers bending moments and increases the airfoil thickness at the root, allowing lighter spar caps and skins.
- **Tip Stall**: Thinner tip chords stall sooner, particularly with sweep, which can reduce aileron effectiveness.
- **Typical Values**: Propeller aircraft show taper ratios from about 0.35 to 0.8. Greater sweep angles tend to coincide with lower taper ratios.
- **Trend Line**: A simple relationship relating sweep angle to taper ratio is suggested:
  \[
  \lambda \approx 0.2\left(2 - \frac{\Lambda_{c/4}}{180}\right),
  \]
  where \(\Lambda_{c/4}\) is the quarter–chord sweep in degrees. This yields \(\lambda = 0.4\) for zero sweep.
- **Design Choice**: Any value between 0 and 1 is possible; the designer must weigh drag, structure and stall behavior in selecting \(\lambda\).


# Source: ./Assignment_8.3/notes.md

# Assignment 8.3 Notes

Summary of instructions from Part 3 p. 190 about drawing the wing planform:

- Determine the wing planform geometry using the chosen aspect ratio, quarter-chord sweep angle and taper ratio.
- Compute wing span, root chord and tip chord using the wing area.
- Draw the wing planform in top view:
  1. Draw the root chord and span line.
  2. Add the quarter-chord sweep line.
  3. Draw the tip chord and connect leading and trailing edges to complete the trapezoidal planform.
- **Assignment 8.3** specifically instructs to sketch the planform (one half wing is allowed) at the **same scale** used for the fuselage top view (Assignment 6.3) and side view (Assignment 6.4).


# Source: ./Assignment_8.4/notes.md

# Notes on Marking the Mean Aerodynamic Chord

Summary of Part 3, p.192: how to mark the mean aerodynamic chord (MAC) on the wing drawing.

1. After defining the wing planform, draw the **50%-chord line** across the wing.
2. From the trailing edge of the root, extend the root chord by a tip-chord length. Likewise extend the tip chord forward by one root-chord length.
3. Connect these extension points diagonally. At the intersection with the 50%-chord line, draw the MAC from leading to trailing edge.
4. Copy the MAC to the symmetry plane of the aircraft to show the full-wing MAC. The leading edge position of the MAC (LEMAC) and its length are important references for later layout steps.
5. This graphical approach works for all straight‑tapered wings and effectively represents the wing in one dimension.

These steps are derived from the book's explanation and match the process in Figure 8.7.

# Source: ./Assignment_8.5/notes.md

The textbook recommends placing the front spar at 20% of chord and the rear spar at 70%. These two spars form the sides of the wing box, a volume that can be used for fuel storage. Placing high‑lift devices outside the box leaves this space clear. The rear spar position is critical for the main landing gear integration, while the front spar location must accommodate any wing‑mounted engines or motors.

# Source: ./Assignment_8.6/notes.md

# Thickness-to-Chord Ratio Selection (Part 3 p. 206)

* **Structural Benefits**
  * Higher thickness-to-chord ratio increases bending stiffness, reducing required skin or spar cap area.
  * Allows more internal volume for landing gear, fuel, and systems, leading to lower wing mass.
* **Aerodynamic Considerations**
  * Thicker wings increase form drag; zero-lift drag correlates with thickness-to-chord ratio.
  * Stall characteristics impose limits: very thick or very thin airfoils reduce the maximum lift coefficient.
  * For swept wings at high Mach numbers, thickness must be limited to avoid strong shock formation.
* **Recommended Approach**
  1. Use the zero-lift drag budget to compute the maximum allowable t/c via the form-drag correlation.
  2. Determine minimum and maximum t/c from lift requirements using airfoil data (Fig. 8.9).
  3. At cruise Mach numbers above 0.65, further restrict t/c using the wave-drag relation.
  4. Choose the highest t/c that satisfies all constraints to maximize structural volume and minimize mass.
* **Iteration**
  * If no single t/c satisfies drag and lift budgets, either compromise between minimum and maximum values or revisit earlier assumptions (e.g., reduce required CL_max or adjust friction coefficient).

# Source: ./Assignment_8.7/notes.md

# Dihedral Angle and Ground Clearance (Part 3 p. 211)

This note summarizes the guidance from **Airplane Design Part 3** on
computing the wing dihedral angle and evaluating ground clearance.

## Computing Dihedral Angle

The text proposes choosing a baseline dihedral angle of **3°** for an
unswept mid‑wing. Adjustments are then made according to sweep and wing
placement:

- Reduce the angle by **1° for every 10°** of quarter‑chord sweep.
- For **high‑wing** airplanes subtract **2°** and for **low‑wing**
  airplanes add **2°**.

Example 8.4 applies these rules for a low‑wing with 26° sweep, resulting
in a dihedral angle of approximately **2.3°**.

## Ground Clearance Considerations

A positive dihedral raises the wing tip and any wing‑mounted engine or
propeller. When landing on one wheel with a bank angle, this extra height
improves clearance. The text notes that a **minimum ground clearance
angle of 8°** is desirable, with more margin preferred for safe
maneuvering. Increasing the dihedral can lower landing‑gear height and
mass on a low‑wing aircraft, so selecting a slightly higher dihedral than
the baseline may be justified.

## Assignment 8.7

- **Compute** the dihedral angle using the above guidelines.
- **Evaluate** whether additional dihedral is needed for ground
  clearance and determine a final angle accordingly.

# Source: ./Assignment_8.8/notes.md

# Notes on Front and Side Wing Views

## Source
Airplane Design Part 3, p. 217 (section 8.1.7)

## Key Ideas
- Once the wing's thickness-to-chord ratio and dihedral angle are chosen, draw front and side views using the American three‑view convention.
- **Step 1:** Determine wing root thickness from the thickness ratio. In front view, show the root as a line. In side view, sketch an airfoil using the root chord and thickness.
- **Step 2:** Through the root centerline, draw a dashed line for the dihedral angle extending the wing span.
- **Step 3:** Measure the vertical displacement of the tip (Δzᵀ) in front view. Using the thickness ratio, sketch the tip airfoil in side view and mark its position in front view.
- **Step 4:** Connect the leading and trailing edges between root and tip in side view. In front view, connect the top and bottom edges of the root and tip profiles.

### Example 8.5 Highlights
- Root thickness 60 cm for t/c = 10.5 %.
- Dihedral angle Γ = 5°, higher than Example 8.4 due to engine mounting.
- Tip vertical displacement Δzᵀ = 1.3 m, tip thickness 0.19 m.
- Final views show connected profiles in front and side projections.

### Assignment 8.8 Instructions
Add front and side views to your wing drawing from Assignment 8.3.
Follow the American convention and keep the same scale.

# Source: ./Assignment_8.9/notes.md

# Notes on Propeller Diameter Sizing

This summary is based on Part 3, p. 205–206 (original numbering) of the course text.

The text explains that propeller noise and efficiency depend strongly on the diameter and rotational speed. To estimate the propeller diameter for a tractor configuration, Ref. [12]'s method is modified, resulting in equation (8.14):

```
Dp = 0.554 * sqrt(P_TO / (1000 * N_e))
```

where:
- `Dp` is the propeller diameter in meters,
- `P_TO` is the take‑off power in kW, and
- `N_e` is the number of engines or motors.

The formula gives a first estimate for tractor propeller diameter. A survey of civil and military propeller aircraft shows most propellers fall within about ±5 % of the prediction; military examples may be underestimated by up to 15 %.

**Example 8.6** evaluates the formula for a 152 kW single‑engine airplane, yielding a diameter of approximately 1.9 m.

**Assignment 8.9** instructs students to apply this method to their own aircraft designs to determine the propeller diameter.

# Source: ./Assignment_9.1/notes.md

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

# Source: ./Assignment_9.10/notes.md

# Notes on Part 3 p. 269

Summary of instructions for sizing the horizontal tailplane and integrating it into the three-view drawing.

## Horizontal Tailplane Design
- Select a longitudinal location for the horizontal tail aerodynamic center relative to the fuselage reference frame.
- Measure the tail arm $l_h$ between the wing aerodynamic center and the tail aerodynamic center.
- Choose an appropriate tail volume coefficient $V_h$ and compute the horizontal tail area $S_h$.
- Decide on the planform parameters (aspect ratio $A_h$, taper ratio $\lambda_h$, and quarter-chord sweep $\Lambda_{h,c/4}$).
- From these parameters determine the span, root chord, tip chord and mean aerodynamic chord of the horizontal tail.
- Add the horizontal tail to the top, front and side views of the drawing.

## Tuning the Three-View Drawing
- Remove hidden wing lines inside the fuselage; keep only the visible portion.
- Include spar locations and landing gear wheels, showing stowed wheels if retractable.
- Mark the wing mean aerodynamic chord on the centerline along with forward and aft CG limits.
- Indicate boundaries of reference wing and horizontal tail areas, plus pressure bulkheads and emergency exits where visible.
- In the front view, show the vertical and horizontal tails. If the design has a low tail, a small dihedral can prevent tail scraping when rotating.
- Apply any yehudi step to the wing thickness in the front view and only show the portion of the wing outside the fuselage in the side view. The same rule applies to the horizontal tail.
- Depict the vertical tail mean aerodynamic chord in the side view and adjust the drawing for proper wing root profile if a yehudi is used.


# Source: ./Assignment_9.11/notes.md

# Final Three-View Clean-Up (Part 3 p. 272)

Summary of guidelines for refining the final three-view drawing:

- **Include axes**: Every view (top, front, side) should show its own axis system.
- **Top view clean up**:
  - Remove wing lines hidden inside the fuselage; only show the exposed wing.
  - Mark spar locations and landing gear wheels; show retracted wheels if applicable.
  - Indicate the wing mean aerodynamic chord (MAC) on the centerline and add the forward and aft CG positions.
  - Delineate the bounds of reference wing area $S_w$ and tailplane area $S_h$.
  - Draw front and aft pressure bulkheads for pressurized cabins.
  - Add visible emergency exit locations.
- **Front view details**:
  - Draw vertical and horizontal tails, adding a small dihedral angle for low‑tail layouts.
  - If a yehudi step is present, thicken the inner wing in front view.
  - Show deployed landing gear and its stowed position if retractable.
  - Include the passenger floor with thickness.
- **Side view details**:
  - Ensure the wing (and yehudi step if present) is properly drawn; only show external portions of wing and horizontal tail.
  - Show MAC of the vertical tail and the vertical tail area $S_v$.
  - Mark emergency exits, landing gear (and stowed position if any), pressure bulkheads, passenger floor and pilot’s eye.
- **Overall**: Indicate the stowed landing gear positions, depict reference areas with shading or light hash marks, draw MAC lines for wing and tail surfaces, add a scale bar, and include a ground plane in the side view.

# Source: ./Assignment_9.2/notes.md

# Wing Positioning with Mass Fractions (Part 3 p.241)

Part 3 outlines a simplified method to locate the wing on the fuselage by
examining how payload and fuel masses shift the aircraft's center of gravity
(CG).  The approach normalizes all masses by the maximum take‑off mass so the
results apply to any airplane size.

**Summary of the procedure:**

1. **Group components** into wing and fuselage assemblies.
2. **Estimate weight fractions** of each component statistically.
3. **Compute assembly CGs** for the wing and fuselage.
4. **Select the desired OEM CG** position relative to the mean aerodynamic
   chord (MAC).
5. **Solve for the LEMAC position** in the fuselage reference frame so the OEM
   CG lies at the chosen fraction of the MAC.
6. **Determine payload and fuel CGs** – e.g. assume fuel CG at 15 % MAC if it is
   in the wings.
7. **Construct a simplified loading diagram** that plots CG location vs.
   mass fraction for key loading cases: OEM, OEM + payload, OEM + payload + fuel,
   and OEM + fuel.
8. **Estimate the vertical CG position**, often kept on the fuselage centerline.

By plotting these points, the forward and aft CG limits become evident. The wing
position—expressed by the LEMAC station—is adjusted so these limits fall within
acceptable bounds for stability and landing gear placement.

# Source: ./Assignment_9.3/notes.md

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

# Source: ./Assignment_9.4/notes.md

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

# Source: ./Assignment_9.5/notes.md

Summary of Part 3 p. 251 - Selecting Tire Pressure and Updating ACR
===============================================================

- **Tire pressure limits** are tied to runway surface. Table 9.2 lists maximum
  allowable pressures for surfaces ranging from soft sand to pavement. On paved
  runways most aircraft operate between **0.50 and 1.75 MPa**, which maps to
  classification ratings **X or Y** in the ACR system.
- **Assignment 9.5** asks to choose the tire pressure using the runway type and
  the current ACR's fourth entry (**G4**). If the pressure selection changes
  the classification, the ACR must be updated accordingly.
- The **tire selection process** (beginning of Section 9.2.2) involves:
  1. Selecting tire pressure based on surface type or PCR and updating the ACR
     if required.
  2. Determining the wheel loads for main and nose/tail gear.
  3. Choosing the smallest tire that can handle those loads at the selected
     pressure.
- **Example 9.5** illustrates this. For a PCR of **W** (no explicit maximum
  pressure), a practical value of **1.40 MPa** is selected. The ACR at
  maximum take-off mass is updated to **850/F/C/X/T**.

# Source: ./Assignment_9.6/notes.md

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

# Source: ./Assignment_9.7/notes.md

# Landing Gear Integration in Side View (Part 3 p.255)

- **Step 1** – Determine the required tip‑over angle (often around 15°) and the
  allowable scrape angle (about 12° in the example).
- **Step 2** – Set the minimum nose‑gear load fraction for steering
  (\(f_{\text{nlg,min}} \ge 0.06\)) and a maximum fraction to be
  supported structurally (typically 0.15–0.20).
- **Step 3** – Choose the fuselage pitch angle on the ground
  (\(\theta_{\text{fus}}\)).
- **Step 4** – In the side view, draw constraint lines for the chosen
  tip‑over and scrape angles (and any ground‑clearance limits) to position
  the main gear. The intersection of these lines usually gives the shortest
  and most forward location.
- **Step 5** – Draw the ground plane below the tire.
- **Step 6** – Draw constraint lines based on nose‑gear load requirements
  to locate the nose gear. Any position between the limits is acceptable;
  a forward location reduces load but increases turn radius.
- **Step 7** – If applicable, sketch retraction paths for the main and
  nose gear.

After placing the wheels, verify in the drawing that the tip‑over and scrape
angles are met. Measuring the tip‑over angle relative to a vertical line is
sufficient when the fuselage is level. A simple line from the lowest point of
the tire provides a useful approximation to check the scrape angle.
Keeping the reference \(X\)-axis below the ground plane ensures all
\(Z\)-coordinates remain positive if the gear height changes later.

# Source: ./Assignment_9.8/notes.md

# Landing Gear Integration (p.261 Part 3)

The text outlines a short procedure for setting the width (track) of the main landing gear and incorporating the gear in orthographic views:

1. **Select a suspension stroke** for the main landing gear along with the portion that is compressed under a 1‑g load.
2. **Determine the minimum lateral position** of each main strut to satisfy several constraints:
   - **Lateral turnover** requirement.
   - **Nacelle/propeller clearance** if the propulsion system is wing‑mounted.
   - **Tip clearance** at the wing tip.
   - **Engine clearance** for the fully compressed suspension with a deflated tire (wing‑mounted engines only).
3. **Integrate the gear in the front view**, showing retraction paths, any structural elements, and changes to the outer mold line as needed.
4. **Integrate the gear in the top view**, again indicating retraction paths, structural details, and any planform changes.

This sequence ensures that the landing gear layout provides adequate clearances and stability while fitting cleanly into the airplane’s overall geometry.

# Source: ./Assignment_9.9/notes.md

# Notes on Vertical Tailplane Design (Part 3 p.266)

Page 266 introduces **Assignment 9.9** which walks through sizing the vertical tailplane using the tail‑volume method and then drawing it in every view. The steps are:

1. Pick the longitudinal location of the vertical tail aerodynamic center.
2. Measure the moment arm `l_v` from this center to the aft CG.
3. Choose a volume coefficient and compute the tail area `S_v`.
4. Select aspect ratio `A_v`, taper ratio `λ_v` and leading‑edge sweep `Λ_{v,LE}`.
5. Derive span, root chord, tip chord and mean aerodynamic chord.
6. Place the vertical tail on the side view at the chosen location.
7. Add the tailplane to the front and top views as well.

A symmetric airfoil with a thickness ratio similar to the wing is adequate for now. Detailed airfoil design and integration with the horizontal tail are covered later in the course.
