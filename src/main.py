from data_loader import GymDataLoader, BodyDataLoader
from data_processor import DataProcessor
from visualizer import GymVisualizer, BodyVisualizer

def main():
    #Load Apple Health data
    bodyloader = BodyDataLoader('data/export.xml')
    df = bodyloader.load_applehealth()
    bodyvisualizer = BodyVisualizer(df)
    bodyvisualizer.plot_weight_change()
    
    # Load Strong App data
    loader = GymDataLoader('data/strong.csv')
    data = loader.load_gymdata()
    if data is None:
        return

    # Process data
    processor = DataProcessor(data)
    volume_per_session = processor.calculate_volume_per_session()
    volume_per_exercise = processor.calculate_volume_per_exercise()

    # Visualize data
    visualizer = GymVisualizer(data)
    visualizer.plot_volume_per_session(volume_per_session)
    visualizer.plot_weight_over_time()
    visualizer.plot_volume_per_exercise(volume_per_exercise)

if __name__ == "__main__":
    main()
