# State-Funded Infrastructure & Capital Investments: Simulation Model

An interactive macroeconomic simulation model built in Python to evaluate the socio-economic outcomes of state-funded capital investments (hospitals, schools, factories, and energy grids). 

This project explores the delicate equilibrium between human capital expansion, industrial capacity growth, and logistical connectivity.

## Technical Architecture & Automation
The repository features a built-in CI/CD pipeline powered by **GitHub Actions**. It supports two distinct operating modes:
1. **Interactive Presentation Mode:** Designed for live demonstrations where parameters are adjusted manually via console inputs.
2. **Automated Pipeline Mode:** Tailored for automated workflows, running benchmark historical scenarios inside headless Ubuntu environments.

---

## Theoretical Framework & Simulation Mechanics

The underlying simulation engine treats public infrastructure investment not as isolated spending, but as a system of highly interdependent vectors:
* **Human Capital (HC):** Represents public health investments, schools, universities, and social safety nets.
* **Industrial Capacity (IC):** Represents state-owned manufacturing facilities, manufacturing plants, and import substitution assets.
* **Logistics & Utilities (LU):** Represents systemic lifelines—highways, heavy railroads, cargo sea ports, and electricity grids.

### ⚠️ System Interdependency & Structural Bottlenecks
In real-world economics, infrastructure cannot function in a vacuum. Building massive manufacturing plants without public utilities results in stagnant production, while funding advanced schools without an industrial job market triggers a severe brain drain.

To simulate this friction, the engine calculates a **Structural Bottleneck Penalty**:
\[\text{If } (\text{Max Index} - \text{Min Index}) > 30 \implies \text{Penalty} = -15\% \text{ to all sectors}\]

### 🏁 Macroeconomic Sustainability Score
The final long-term evaluation is measured dynamically at the end of the fiscal lifecycle using the following formula:
\[\text{Sustainability Score} = \frac{\text{HC} + \text{IC} + \text{LU}}{3} - \text{Active Penalties}\]

---

## Project Structure

```text
state-building-simulation/
├── .github/
│   └── workflows/
│       └── run_simulation.yml    # CI/CD pipeline configuration
├── simulation/
│   ├── __init__.py               # Python package initialization
│   ├── engine.py                 # Core mathematical & simulation engine
│   └── scenarios.json            # Preconfigured benchmark macro profiles
├── outputs/                      # Automated analytical dashboard artifacts
├── .gitignore                    # Version control exclusions
├── README.md                     # Academic project documentation
├── requirements.txt              # Pipeline dependencies
└── run.py                        # Central orchestration entrypoint
```

---

## Deployment & Local Installation

### 1. Prerequisites
Ensure you have Python 3.10+ installed. Clone the repository and install the visualization dependencies:
```bash
pip install -r requirements.txt
```

### 2. Running Live Presentation Mode (Interactive)
To launch the interactive simulation during a project presentation:
```bash
python run.py --mode interactive
```

### 3. Running Automated Headless Scenarios
To test a predefined automated benchmark locally (simulating the GitHub Actions server behavior):
```bash
python run.py --mode automated --scenario industrial_overdrive
```

## Analytics & Reporting
Upon execution, the engine automatically compiles a comprehensive markdown report (`outputs/report.md`) and renders a high-resolution developmental data dashboard plot (`outputs/dashboard.png`).

*Developed for the English Research and Simulation Project.*
