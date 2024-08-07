# Проект "Анализ рынка недвижимости"

## Описание проекта
Проект по анализу рынка недвижимости основан на данных из датасета `kc_house_data.csv`. В проекте проводится анализ различных характеристик недвижимости, таких как стоимость, площадь, наличие вида на набережную, этажность, состояние дома и другие. Для анализа используются различные статистические методы и визуализации.

## Установленные библиотеки
- pandas
- matplotlib
- seaborn
- scipy
- numpy

### 1. Распределение домов от наличия вида на набережную

Изучив данные о наличии вида на набережную, мы обнаружили, что всего лишь 0.8% домов имеют такой вид.

### 2. Распределение этажей домов

Большинство домов имеют 1 или 2 этажа.

### 3. Распределение состояния домов

Большинство домов имеют среднее состояние, причем доля домов в плохом состоянии крайне мала.

### Влияние характеристик на стоимость недвижимости

1. **Площадь недвижимости и количество комнат:** Цена недвижимости сильно зависит от площади, а также от количества комнат, что подтверждается высокой корреляцией между этими параметрами.

2. **Вид на набережную:** Цена недвижимости также зависит от наличия вида на набережную, при этом объекты с видом на набережную имеют более высокую стоимость.

3. **Оценка дома:** Индекс оценки недвижимости также влияет на стоимость дома, причем чем выше оценка, тем выше цена.

4. **Состояние дома:** Состояние недвижимости оказывает существенное влияние на ее цену. Видно, что средняя цена домов растет с улучшением состояния.

5. **Количество ванных комнат:** Цена недвижимости также увеличивается с увеличением количества ванных комнат.

Эти выводы могут быть полезны при анализе рынка недвижимости и принятии решений о покупке или продаже объектов недвижимости.
