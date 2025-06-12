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

