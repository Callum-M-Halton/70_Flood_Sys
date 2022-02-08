from floodsystem.station import MonitoringStation

class StockStation(MonitoringStation):
    '''
    Child Class of MonitoringStation which simplifies creation of stock
    Monitoring Stations. It reduces the amount of input needed to create
    a station with only a few custom attributes. This is useful for creating
    lists of arbitrary stations for testing where only a few attributes change.
    '''
    def __init__(self, custom):
        # Always Stock for existing tests
        s_id = "test-s-id"
        m_id = "test-m-id"
        town = "My Town"

        # Sometimes Custom for tests
        name = custom['name'] if 'name' in custom else "stockStation"
        coord = custom['coord'] if 'coord' in custom else (0, 0)
        typical_range = custom['typical_range'] if 'typical_range' in custom else (-1, 1)
        river = custom['river'] if 'river' in custom else "stockRiver"

        super().__init__(s_id, m_id, name, coord, typical_range, river, town)