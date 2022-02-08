from floodsystem.station import MonitoringStation

class StockStation(MonitoringStation):
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