from data_loader import GymDataLoader, BodyDataLoader
from data_processor import DataProcessor
from visualizer import GymVisualizer, BodyVisualizer

def main():
    #region Apple Health
    #Load Apple Health app data

    record_types = ["HKQuantityTypeIdentifierBodyMass", "HKQuantityTypeIdentifierBodyFatPercentage", "HKQuantityTypeIdentifierLeanBodyMass", "HKQuantityTypeIdentifierBodyMassIndex", "HKQuantityTypeIdentifierHeartRateRecoveryOneMinute"]
    
    bodyloader = BodyDataLoader('data/export.xml')
    for record_type in record_types:
        df = bodyloader.load_applehealth(record_type)
        bodyvisualizer = BodyVisualizer(df, record_type)
        bodyvisualizer.plot_recordtype_change()
    #endregion
    #region Strong App
    # Load Strong app data
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
    #endregion
if __name__ == "__main__":
    main()
