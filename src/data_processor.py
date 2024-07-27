class DataProcessor:
    def __init__(self, data):
        self.data = data

    def calculate_volume_per_session(self):
        return self.data.groupby('Date')['Volume'].sum().reset_index()

    def calculate_volume_per_exercise(self):
        return self.data.groupby('Exercise Name')['Volume'].sum().reset_index()

    def get_exercises(self):
        return self.data['Exercise Name'].unique()
