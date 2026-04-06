from model.manager import comprobar_archivo_json, registro_valido

# mock variable

mockMapaTrue = {"fecha": "",
                "zona": "",
                "temperatura": "",
                "humedad": "",
                "viento": "",}

mockMapaFalse = {"fechas": "",
                "zona": "",
                "temperatura": "",
                "humedad": "",
                "viento": "",}

# test func

def test_comprobar_archivo_json():
    assert comprobar_archivo_json() == "data\\register.json"

def test_comprobar_archivo_json_not_match():
    assert comprobar_archivo_json() != "data\\reegister.json"

def test_registro_valido():
    assert registro_valido(mockMapaTrue)
    
def test_registro_no_valido():
    assert not registro_valido(mockMapaFalse)