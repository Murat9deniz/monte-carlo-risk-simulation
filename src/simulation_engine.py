import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class MonteCarloProfitSimulator:
    """A stochastic simulation engine to evaluate business risk and profit distributions.
    Models demand variability, unit production costs, and fixed operational
    expenses.
    """

    def __init__(
        self,
        mean_demand: float,
        std_demand: float,
        unit_price: float,
        cost_mean: float,
        cost_std: float,
        fixed_costs: float,
    ):
        self.mean_demand = mean_demand
        self.std_demand = std_demand
        self.unit_price = unit_price
        self.cost_mean = cost_mean
        self.cost_std = cost_std
        self.fixed_costs = fixed_costs
        self.results = None

    def run_simulation(
        self, num_trials: int = 500, random_seed: int = 42
    ) -> pd.DataFrame:
        """Executes N stochastic simulation trials using normal distributions."""
        np.random.seed(random_seed)

        # Generate stochastic variables
        simulated_demand = np.maximum(
            0, np.random.normal(self.mean_demand, self.std_demand, num_trials)
        )
        simulated_unit_cost = np.maximum(
            0.1, np.random.normal(self.cost_mean, self.cost_std, num_trials)
        )

        # Financial calculations
        total_revenue = simulated_demand * self.unit_price
        variable_costs = simulated_demand * simulated_unit_cost
        total_costs = variable_costs + self.fixed_costs
        net_profit = total_revenue - total_costs

        self.results = pd.DataFrame(
            {
                "Trial": np.arange(1, num_trials + 1),
                "Simulated_Demand": simulated_demand,
                "Unit_Cost": simulated_unit_cost,
                "Total_Revenue": total_revenue,
                "Total_Cost": total_costs,
                "Net_Profit": net_profit,
            }
        )
        return self.results

    def get_summary_statistics((self) -> dict:
        """Calculates key statistical metrics and downside risk indicators."""
        if self.results is None:
            raise ValueError(
                "Run the simulation first using run_simulation()"
            )

        profits = self.results["Net_Profit"]
        loss_trials = (profits < 0).sum()
        prob_of_loss = (loss_trials / len(profits)) * 100

        stats = {
            "Mean_Profit": np.mean(profits),
            "Median_Profit": np.median(profits),
            "Std_Dev_Profit": np.std(profits),
            "5th_Percentile_VaR": np.percentile(profits, 5),
            "95th_Percentile": np.percentile(profits, 95),
            "Probability_of_Loss_%": prob_of_loss,
        }
        return stats


if __name__ == "__main__":
    # Example execution with baseline industrial parameters
    simulator = MonteCarloProfitSimulator(
        mean_demand=10000,
        std_demand=1800,
        unit_price=45.0,
        cost_mean=22.0,
        cost_std=3.5,
        fixed_costs=120000.0,
    )

    df_results = simulator.run_simulation(num_trials=500)
    summary = simulator.get_summary_statistics()

    print("--- Monte Carlo Simulation Summary Statistics ---")
    for key, val in summary.items():
        print(f"{key}: {val:,.2f}")
