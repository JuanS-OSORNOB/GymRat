from data_loader import DataLoader
from data_processor import DataProcessor
from visualizer import Visualizer

def main():
    # Load data
    loader = DataLoader('data/strong.csv')
    data = loader.load_data()
    if data is None:
        return

    # Process data
    processor = DataProcessor(data)
    volume_per_session = processor.calculate_volume_per_session()
    volume_per_exercise = processor.calculate_volume_per_exercise()

    # Visualize data
    visualizer = Visualizer(data)
    visualizer.plot_volume_per_session(volume_per_session)
    visualizer.plot_weight_over_time()
    visualizer.plot_volume_per_exercise(volume_per_exercise)

if __name__ == "__main__":
    main()
