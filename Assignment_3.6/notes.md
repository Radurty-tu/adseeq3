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
