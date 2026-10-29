import argparse
import sys
from simulation.engine import EconomicEngine


def main():
    # Настраиваем аргументы командной строки для GitHub Actions
    parser = argparse.ArgumentParser(description="State Infrastructure Investment Simulation Runner")
    parser.add_argument(
        "--mode",
        choices=["interactive", "automated"],
        default="interactive",
        help="Run simulation interactively (for presentations) or automated (for GitHub Actions CI/CD)"
    )
    parser.add_argument(
        "--scenario",
        choices=["singapore_model", "industrial_overdrive"],
        default="singapore_model",
        help="Target profile from scenarios.json if running in automated mode"
    )

    args = parser.parse_args()

    # Инициализируем наш движок
    engine = EconomicEngine()

    engine.log(engine.config["strings"]["welcome"])

    if args.mode == "interactive":
        # === РЕЖИМ 1: ИНТЕРАКТИВНЫЙ (ДЛЯ ЗАЩИТЫ КУРСОВОЙ) ===
        engine.log("\n[!] Starting Interactive Presentation Mode...")

        # Год 1
        print(engine.config["strings"]["year1_prompt"].format(stats=engine.stats))
        choice_y1 = input("Choose capital strategy (1 or 2): ").strip()
        while choice_y1 not in ["1", "2"]:
            choice_y1 = input("Invalid input. Please enter 1 or 2: ").strip()
        engine.execute_year_1(choice_y1)

        # Год 2
        print(engine.config["strings"]["year2_prompt"].format(stats=engine.stats, budget=engine.budget))
        choice_y2 = input("Choose expansion strategy (1 or 2): ").strip()
        while choice_y2 not in ["1", "2"]:
            choice_y2 = input("Invalid input. Please enter 1 or 2: ").strip()
        engine.execute_year_2(choice_y2)

        # Год 3 (Кризис)
        engine.simulate_crisis_year_3()

    else:
        # === РЕЖИМ 2: АВТОМАТИЧЕСКИЙ (ДЛЯ GITHUB ACTIONS) ===
        engine.log(f"\n[!] Starting Automated CI/CD Pipeline Mode...")
        target_profile = args.scenario

        if target_profile in engine.config["historical_profiles"]:
            profile = engine.config["historical_profiles"][target_profile]
            engine.log(f"Loading Profile: {profile['name']}")
            engine.log(f"Description: {profile['description']}")

            # Извлекаем предустановленные шаги из JSON
            choices = profile["choices"]

            engine.log("\nExecuting Year 1...")
            engine.execute_year_1(choices["year1"])

            engine.log("\nExecuting Year 2...")
            engine.execute_year_2(choices["year2"])

            engine.simulate_crisis_year_3()
        else:
            engine.log(f"❌ Error: Scenario '{target_profile}' not found in configuration.")
            sys.exit(1)

    # Генерируем финальный аналитический отчет и сохраняем графики (.png и .md)
    engine.generate_final_report()
    engine.log("\n[✔] Simulation complete. Dashboard artifacts successfully saved in 'outputs/' folder.")


if __name__ == "__main__":
    main()
