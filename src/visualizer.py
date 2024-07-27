import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, data):
        self.data = data

    def plot_volume_per_session(self, volume_per_session):
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=volume_per_session, x='Date', y='Volume', marker='o')
        plt.title('Total Volume per Session Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Volume')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_weight_over_time(self):
        plt.figure(figsize=(14, 8))
        for exercise in self.data['Exercise Name'].unique():
            exercise_data = self.data[self.data['Exercise Name'] == exercise]
            sns.lineplot(data=exercise_data, x='Date', y='Weight', label=exercise, marker='o')
        plt.title('Weight Lifted Over Time for Each Exercise')
        plt.xlabel('Date')
        plt.ylabel('Weight')
        plt.legend(title='Exercise Name', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_volume_per_exercise(self, volume_per_exercise):
        plt.figure(figsize=(12, 6))
        sns.barplot(data=volume_per_exercise, x='Volume', y='Exercise Name', palette='viridis')
        plt.title('Total Volume Lifted Across Different Exercises')
        plt.xlabel('Total Volume')
        plt.ylabel('Exercise Name')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
