from proyecto import obtener_fecha, obtener_campos

def test_obtener_fecha():

    assert obtener_fecha("2025-09-30T23:00") == (2025, 9, 30, 1380)
    assert obtener_fecha("2026-03-24T07:00") == (2026, 3, 24, 420)
    assert obtener_fecha("0000-00-00T00:01") == (0, 0, 0, 1)

def test_obtener_campos():
    registro = ["2026-02-15T13:00","Mexico City",19.4326,-99.1332,25.3,25.0,271.0,4.5,184.0,0.0,9.25,70,0]
    assert obtener_campos(registro, ["City", "Latitude", "Longitude"]) == ["Mexico City",19.4326,-99.1332]
    assert obtener_campos(registro, ["City", "Latitude", "Timestamp", "Longitude"]) == ["Mexico City",19.4326, "2026-02-15T13:00", -99.1332]
    assert obtener_campos(registro, ["City"]) == ["Mexico City"]