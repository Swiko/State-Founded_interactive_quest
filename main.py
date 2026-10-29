import matplotlib.pyplot as plt


def run_simulation():
    # Стартовые показатели (Metrics)
    stats = {"Human Capital": 50, "Industrial Capacity": 50, "Logistics & Utilities": 50}
    budget = 100  # $ Millions
    history = {k: [v] for k, v in stats.items()}  # Для отслеживания динамики на графике
    steps = ["Start"]

    print("=" * 60)
    print("Welcome to the State-Funded Infrastructure Simulation!")
    print("Research Topic: State Capital Investments & Socio-Economic Outcomes")
    print("=" * 60)

    # --- YEAR 1 ---
    print(f"\n[YEAR 1] Current Stats: {stats}")
    print("Choose your primary Greenfield Investment (Cost: $40M):")
    print("1. Heavy Industrialization (Build state factories & power plants)")
    print("2. Human-Centric Foundation (Build modern hospitals & schools)")

    choice1 = input("Enter 1 or 2: ")
    if choice1 == "1":
        stats["Industrial Capacity"] += 40
        stats["Logistics & Utilities"] += 15
        stats["Human Capital"] -= 15
        steps.append("Year 1: Industry")
    else:
        stats["Human Capital"] += 45
        stats["Industrial Capacity"] -= 10
        stats["Logistics & Utilities"] -= 10
        steps.append("Year 1: Social")

    budget -= 40
    for k, v in stats.items(): history[k].append(max(0, v))

    # --- YEAR 2 (The Bottleneck & Interdependency check) ---
    # Проверка на дисбаланс (Structural Bottleneck Penalty)
    max_val = max(stats.values())
    min_val = min(stats.values())
    penalty = 0
    if (max_val - min_val) > 30:
        penalty = 15
        print(
            f"\n⚠️ WARNING: Structural Bottleneck Detected! Severe imbalance between sectors. Penalty applied: -15 to all metrics.")
        for k in stats: stats[k] = max(0, stats[k] - penalty)

    print(f"\n[YEAR 2] Current Stats: {stats} | Remaining Budget: ${budget}M")
    print("Infrastructure demands expansion. Where do you allocate the next $30M?")
    print("1. Logistics & Supply Chains (Highways and cargo ports)")
    print("2. Power Grids & Civil Utilities (Energy stability)")

    choice2 = input("Enter 1 or 2: ")
    if choice2 == "1":
        stats["Logistics & Utilities"] += 30
        stats["Industrial Capacity"] += 10
    else:
        stats["Logistics & Utilities"] += 25
        stats["Human Capital"] += 15

    budget -= 30
    steps.append("Year 2: Grid") if choice2 == "2" else steps.append("Year 2: Logistics")
    for k, v in stats.items(): history[k].append(max(0, v))

    # --- YEAR 3 (The Black Swan / Crisis) ---
    print(f"\n[YEAR 3] Current Stats: {stats}")
    print("🚨 CRISIS ALERT: A severe winter storm hits the nation, testing your infrastructure!")

    if stats["Logistics & Utilities"] < 50:
        print(
            "❌ Crisis Outcome: Low Logistics & Utilities capacity caused a massive blackout. Factories stopped, hospitals lost power.")
        stats["Industrial Capacity"] -= 25
        stats["Human Capital"] -= 20
    else:
        print(
            "✅ Crisis Outcome: Your robust Logistics & Energy network successfully absorbed the shock with minimal damage.")
        stats["Industrial Capacity"] -= 5
        stats["Human Capital"] -= 5

    steps.append("Year 3: Crisis")
    for k, v in stats.items(): history[k].append(max(0, v))

    # --- FINAL EVALUATION ---
    sustainability_score = sum(stats.values()) / 3
    print("\n" + "=" * 60)
    print("SIMULATION COMPLETE - FINAL SOCIO-ECONOMIC OUTCOME")
    print("=" * 60)
    print(f"Final Metrics: {stats}")
    print(f"Sustainability Score: {sustainability_score:.1f}%")

    if sustainability_score >= 65:
        print("🏆 RESULT: The Economic Miracle. Balanced investments triggered sustainable long-term growth.")
    elif 45 <= sustainability_score < 65:
        print("⚠️ RESULT: Unbalanced Growth. The state is developing, but faces severe structural bottlenecks.")
    else:
        print(
            "❌ RESULT: The White Elephant Trap. Misallocated funds led to crumbling infrastructure and systemic crisis.")

    # --- GENERATING THE DATA DASHBOARD ---
    plt.figure(figsize=(10, 6))
    for metric, values in history.items():
        plt.plot(steps, values, marker='o', linewidth=2.5, label=metric)

    plt.title("State-Funded Capital Investments: Socio-Economic Simulation Dashboard", fontsize=14, fontweight='bold')
    plt.ylabel("Development Level (%)", fontsize=12)
    plt.xlabel("Simulation Stages", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.ylim(0, 110)
    plt.legend(loc="upper left", fontsize=11)

    # Текстовая аннотация с итогом на самом графике
    plt.text(0.5, 15,
             f"Final Sustainability Score: {sustainability_score:.1f}%\nStatus: {'Stable' if sustainability_score >= 50 else 'Fragile'}",
             bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'), fontsize=11)

    plt.show()


if __name__ == "__main__":
    run_simulation()
