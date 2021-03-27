Feature app calculadora

Scenario Outline: Obtener total del app calculadora
Given los <valores> para operar en la app
When la app opere los valores
Then el <total> de la operacion en app es correcto

Examples: valores
| valores  | total |
| +,5,7    | 12    |
| +,3,15   | 18    |
| -,20,5   | 15    |
| -,100,50 | 50    |