# Circuit Sage Output
## Prompt
```
I have a circuit with a 12V battery connected to a 4Ω resistor in series with a 6Ω resistor. What is the current through each resistor and the voltage drop across each?
```
## Response
Let's analyze this simple series circuit.  Since the resistors are in series, the same current flows through both. We can use Ohm's Law (V = IR) and Kirchhoff's Voltage Law (KVL) to solve this.

**1. Total Resistance:**

First, we find the total resistance (R<sub>total</sub>) of the circuit.  In a series circuit, the total resistance is simply the sum of the individual resistances:

R<sub>total</sub> = R<sub>1</sub> + R<sub>2</sub> = 4Ω + 6Ω = 10Ω

**2. Total Current:**

Next, we use Ohm's Law to calculate the total current (I<sub>total</sub>) flowing in the circuit.  We know the total voltage (V<sub>total</sub>) is 12V (from the battery):

I<sub>total</sub> = V<sub>total</sub> / R<sub>total</sub> = 12V / 10Ω = 1.2A

Since this is a series circuit, the current through both resistors is the same:

I<sub>R1</sub> = I<sub>R2</sub> = I<sub>total</sub> = 1.2A

**3. Voltage Drop Across Each Resistor:**

Now we use Ohm's Law again to find the voltage drop across each resistor:

* **Voltage drop across R1 (4Ω):**

V<sub>R1</sub> = I<sub>R1</sub> * R<sub>1</sub> = 1.2A * 4Ω = 4.8V

* **Voltage drop across R2 (6Ω):**

V<sub>R2</sub> = I<sub>R2</sub> * R<sub>2</sub> = 1.2A * 6Ω = 7.2V

**Summary:**

* **Current through R1 (4Ω):** 1.2A
* **Current through R2 (6Ω):** 1.2A
* **Voltage drop across R1 (4Ω):** 4.8V
* **Voltage drop across R2 (6Ω):** 7.2V

Notice that the sum of the voltage drops across the resistors (4.8V + 7.2V = 12V) equals the total voltage supplied by the battery. This confirms Kirchhoff's Voltage Law.

This is a fundamental circuit analysis problem.  If you'd like to explore more complex circuits or different circuit configurations (parallel, series-parallel), let me know, and I can guide you through those as well.  There are many excellent online resources and simulators (like Falstad Circuit Simulator) that you can use to visualize and experiment with these concepts.
