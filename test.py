from proyecto import obtener_fecha, obtener_campos, carga_ordenada
from consultas_al_informe import adaptador_dioxido, ciudades_superiores_a

def test_obtener_fecha():

    assert obtener_fecha("2025-09-30T23:00") == (2025, 9, 30, 1380)
    assert obtener_fecha("2026-03-24T07:00") == (2026, 3, 24, 420)
    assert obtener_fecha("0000-00-00T00:01") == (0, 0, 0, 1)

def test_obtener_campos():
    registro = ["2026-02-15T13:00","Mexico City",19.4326,-99.1332,25.3,25.0,271.0,4.5,184.0,0.0,9.25,70,0]
    assert obtener_campos(registro, ["City", "Latitude", "Longitude"]) == ["Mexico City",19.4326,-99.1332]
    assert obtener_campos(registro, ["City", "Latitude", "Timestamp", "Longitude"]) == ["Mexico City",19.4326, "2026-02-15T13:00", -99.1332]
    assert obtener_campos(registro, ["City"]) == ["Mexico City"]


def test_adaptador_dioxido():
    informe = {
        "Rosario": {"Nitrogen_Dioxide_ug_m3": 18.5 },
        "Córdoba": {"Nitrogen_Dioxide_ug_m3": 27.0},
        "Santa Fe": {"Nitrogen_Dioxide_ug_m3": 41.3}
    }
    esperado = {
        "Rosario": 18.5,
        "Córdoba": 27.0,
        "Santa Fe": 41.3
    }
    assert adaptador_dioxido(informe) == esperado
    assert adaptador_dioxido({}) == {}

def test_ciudades_superiores_a():
    datos = {
        "Rosario": 18,
        "Córdoba": 35,
        "Santa Fe": 50,
        "Mendoza": 12
    }
    esperado = {
        "Córdoba": 35,
        "Santa Fe": 50
    }
    assert ciudades_superiores_a(datos, 30) == esperado

    datos = {
        "Rosario": 10,
        "Córdoba": 15,
        "Santa Fe": 20
    }
    assert ciudades_superiores_a(datos, 50) == {}

    datos = {
        "Rosario": 40,
        "Córdoba": 55,
        "Santa Fe": 80
    }
    assert ciudades_superiores_a(datos, 30) == datos

    datos = {
        "Rosario": 30,
        "Córdoba": 29.9,
        "Santa Fe": 30.1
    }
    esperado = {
        "Rosario": 30,
        "Santa Fe": 30.1
    }
    assert ciudades_superiores_a(datos, 30) == esperado

def test_carga_ordenada():
    historial = []

    assert carga_ordenada((2025, 9, 30, 1380), 5, 0, historial, 0) == [((2025, 9, 30, 1380), 5, 0)]
    assert carga_ordenada((2026, 3, 7, 420), 2, 1, historial, 1) == [((2025, 9, 30, 1380), 5, 0), ((2026, 3, 7, 420), 2, 1)]
    assert carga_ordenada((2025, 10, 1, 1), 1, 1, historial, 2) == [((2025, 9, 30, 1380), 5, 0), ((2025, 10, 1, 1), 1, 1), ((2026, 3, 7, 420), 2, 1)]
    assert carga_ordenada((0, 0, 0, 1), 0, 0, historial, 2) == [((0, 0, 0, 1), 0, 0),((2025, 9, 30, 1380), 5, 0), ((2025, 10, 1, 1), 1, 1), ((2026, 3, 7, 420), 2, 1)]
    assert carga_ordenada((0, 0, 2, 1), 0, 0, historial, 2) == [((0, 0, 0, 1), 0, 0), ((0, 0, 2, 1), 0, 0),((2025, 9, 30, 1380), 5, 0), ((2025, 10, 1, 1), 1, 1), ((2026, 3, 7, 420), 2, 1)]
    assert carga_ordenada((2025, 0, 2, 1), 0, 0, historial, 2) == [((0, 0, 0, 1), 0, 0), ((0, 0, 2, 1), 0, 0),((2025, 0, 2, 1), 0, 0),((2025, 9, 30, 1380), 5, 0), ((2025, 10, 1, 1), 1, 1), ((2026, 3, 7, 420), 2, 1)]
