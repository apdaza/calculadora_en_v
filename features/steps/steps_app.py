from behave import given, when, then
import requests

@given('los {valores} para operar en la app')
def step_given(context, valores):
    context.values = valores.split(',')
    context.api_url = 'http://localhost:5000/operacion/' + context.values[0] + "/" + context.values[1] + "/" + context.values[2]

@when('la app opere los valores')
def step_when(context):
    session = requests.Session()
    response = session.get(url=context.api_url, headers='')
    context.texto = response.text

@then('el {total} de la operacion en app es correcto')
def step_then(context, total):
    assert(str(total) in context.texto)