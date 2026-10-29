import os
import json
import matplotlib

# Переключаем matplotlib в режим без экрана (для работы в GitHub Actions)
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class EconomicEngine:
    def __init__(self, scenario_path="simulation/scenarios.json"):
        # Загружаем строки и профили
        with open(scenario_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        self.stats = {"Human Capital": 50, "Industrial Capacity": 50, "Logistics & Utilities": 50}
        self.budget = 100
        self.history = {k: [v] for k, v in self.stats.items()}
        self.steps = ["Baseline"]
        self.logs = []

    def log(self, text):
        print(text)
        self.logs.append(text)

    def apply_bottleneck_penalty(self):
        """Проверка на дисбаланс развития (Interdependency Check)"""
        max_val = max(self.stats.values())
        min_val = min(self.stats.values())
        if (max_val - min_val) > 30:
            penalty = 15
            self.log(f"\n⚠️ STRUCTURAL BOTTLENECK DETECTED! Severe imbalance over 30 points.")
            self.log(f"Penalty applied: -{penalty}% to all sectors due to system friction.")
            for k in self.stats:
                self.stats[k] = max(0, self.stats[k] - penalty)

    def execute_year_1(self, choice):
        if str(choice) == "1":
            self.stats["Industrial Capacity"] += 40
            self.stats["Logistics & Utilities"] += 15
            self.stats["Human Capital"] -= 15
            self.steps.append("Y1: Heavy Industry")
            self.log("Action Taken: Capital directed to heavy manufacturing and state factories.")
        else:
            self.stats["Human Capital"] += 45
            self.stats["Industrial Capacity"] -= 10
            self.stats["Logistics & Utilities"] -= 10
            self.steps.append("Y1: Social Welfare")
            self.log("Action Taken: Strategic funding of healthcare institutions and specialized universities.")

        self.budget -= 40
        for k, v in self.stats.items(): self.history[k].append(max(0, v))

    def execute_year_2(self, choice):
        self.apply_bottleneck_penalty()

        if str(choice) == "1":
            self.stats["Logistics & Utilities"] += 35
            self.stats["Industrial Capacity"] += 10
            self.steps.append("Y2: Logistics Hubs")
            self.log("Action Taken: Developed nationwide highways and deepwater cargo ports.")
        else:
            self.stats["Logistics & Utilities"] += 25
            self.stats["Human Capital"] += 15
            self.steps.append("Y2: Energy Grid")
            self.log("Action Taken: Upgraded municipal heating, power grids, and water systems.")

        self.budget -= 30
        for k, v in self.stats.items(): self.history[k].append(max(0, v))

    def simulate_crisis_year_3(self):
        """Проверка инфраструктуры внешним шоком (Black Swan Event)"""
        self.log("\n🚨 SYSTEM TRANSITION: External Shock (Severe Weather & Infrastructure Stress)")
        if self.stats["Logistics & Utilities"] < 50:
            self.log("❌ CRISIS IMPACT: Low grid/logistical resilience caused cascading utility failures.")
            self.stats["Industrial Capacity"] -= 25
            self.stats["Human Capital"] -= 20
        else:
            self.log("✅ CRISIS MITIGATED: Highly developed networks absorbed the macroeconomic shock.")
            self.stats["Industrial Capacity"] -= 5
            self.stats["Human Capital"] -= 5

        self.steps.append("Y3: Shock Test")
        for k, v in self.stats.items(): self.history[k].append(max(0, v))

    def generate_final_report(self):
        sustainability_score = sum(self.stats.values()) / 3

        self.log("\n" + "=" * 60)
        self.log("FINAL EVALUATION & FORECAST")
        self.log("=" * 60)
        self.log(f"Final Indices: {self.stats}")
        self.log(f"Macroeconomic Sustainability Score: {sustainability_score:.1f}%")

        if sustainability_score >= 65:
            status = "The Economic Miracle Scenario (Sustainable Equilibrum)"
        elif 45 <= sustainability_score < 65:
            status = "Unbalanced Growth Trap (Structural Friction)"
        else:
            status = "The White Elephant Dilemma (Systemic Fragility)"

        self.log(f"Classification: {status}")

        # Экспорт артефактов в папку outputs
        os.makedirs("outputs", exist_ok=True)
        self.save_plots(sustainability_score, status)
        self.save_markdown_report(sustainability_score, status)

    def save_plots(self, score, status):
        plt.figure(figsize=(10, 6))
        for metric, values in self.history.items():
            plt.plot(self.steps, values, marker='o', linewidth=2.5, label=metric)

        plt.title("State Capital Investments: Development Vectors", fontsize=12, fontweight='bold')
        plt.ylabel("Development Level (%)")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.ylim(0, 120)
        plt.legend(loc="upper left")

        plt.text(0.5, 10, f"Sustainability: {score:.1f}%\nOutcome: {status}",
                 bbox=dict(facecolor='white', alpha=0.9, boxstyle='round,pad=0.5'), fontsize=9)

        plt.savefig("outputs/dashboard.png", dpi=300)
        plt.close()

    def save_markdown_report(self, score, status):
        report_md = f"""# Analytical Research Report: Infrastructure & State Investments

## Macroeconomic Simulation Output
* **Final Sustainability Index:** {score:.1f}%
* **Development Trajectory:** {status}

### Final Metrics Breakdowns
* **Human Capital (Education/Health):** {self.stats['Human Capital']}%
* **Industrial Capacity (Production/Manufacturing):** {self.stats['Industrial Capacity']}%
* **Logistics & Utilities (Transport/Energy):** {self.stats['Logistics & Utilities']}%

### Simulation Execution Log
```text
{"".join([line + "\\n" for line in self.logs])}
```

*Report automatically compiled via GitHub Actions CI/CD Pipeline.*
"""
        with open("outputs/report.md", "w", encoding="utf-8") as f:
            f.write(report_md)
