def test_operacion(app, client):
    res = client.get('/operacion/+/2/5')
    expected = '2 + 5 = 7'
    assert expected in res.get_data(as_text=True)