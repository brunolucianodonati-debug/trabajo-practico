import unittest

from .services import calcular_emisiones_carbono, obtener_metricas_consumo


class TestCalculoEmisiones(unittest.TestCase):

    # valores nominales con el factor por defecto (0.4)
    def test_calculo_nominal_default(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertEqual(resultado, 40.0)

    # valor nominal con decimales
    def test_calculo_nominal_decimal(self):
        resultado = calcular_emisiones_carbono(1250.5)
        self.assertAlmostEqual(resultado, 500.2)

    # factor de emision personalizado
    def test_calculo_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(250, factor_emision=0.5)
        self.assertEqual(resultado, 125)

    # caso limite: consumo cero
    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0)

    # consumo fuera de rango: debe elevar ValueError
    def test_consumo_negativo(self):
        self.assertRaises(ValueError, calcular_emisiones_carbono, -50)

    # consumo negativo muy pequeño tambien debe fallar
    def test_consumo_negativo_decimal(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-0.1)


class TestMetricasConsumo(unittest.TestCase):

    def test_metricas_total_y_planta_mayor(self):
        registros = [
            {"planta": "Planta A", "consumo_kwh": 100.0},
            {"planta": "Planta B", "consumo_kwh": 300.0},
            {"planta": "Planta A", "consumo_kwh": 50.0},
        ]

        metricas = obtener_metricas_consumo(registros)

        self.assertAlmostEqual(metricas["total_global_emisiones"], 180.0)
        self.assertEqual(metricas["planta_mayor_consumo"], "Planta B")
        self.assertAlmostEqual(metricas["emisiones_por_planta"]["Planta A"], 60.0)

    def test_metricas_lista_vacia(self):
        metricas = obtener_metricas_consumo([])

        self.assertEqual(metricas["total_global_emisiones"], 0.0)
        self.assertIsNone(metricas["planta_mayor_consumo"])
