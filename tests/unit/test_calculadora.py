import pytest
from src.calculadora import calcular_desconto, calcular_imposto, calcular_preco_final


@pytest.mark.unit
class TestCalcularDesconto:
    def test_desconto_normal(self):
        assert calcular_desconto(100.0, 10) == 90.0

    def test_desconto_zero(self):
        assert calcular_desconto(100.0, 0) == 100.0

    def test_desconto_total(self):
        assert calcular_desconto(100.0, 100) == 0.0

    def test_desconto_percentual_negativo(self):
        with pytest.raises(ValueError, match="entre 0 e 100"):
            calcular_desconto(100.0, -5)

    def test_desconto_percentual_acima_de_100(self):
        with pytest.raises(ValueError):
            calcular_desconto(100.0, 110)

