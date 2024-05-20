# Анализ данных по стоимости клиента (Customer Lifetime Value)

## Описание проекта

Цель данного проекта — провести анализ данных клиентов и их характеристик, чтобы понять факторы, влияющие на пожизненную стоимость клиента (Customer Lifetime Value, LTV). Кроме того, была поставлена задача построить модели машинного обучения для классификации клиентов на основе их LTV, используя различные алгоритмы.

## Структура проекта

Проект включает в себя следующие шаги:

1. **Загрузка данных**: Данные загружены из Google Drive с использованием библиотеки `gdown` и считаны в формате CSV.
2. **Предварительный анализ данных**: Проведен начальный осмотр данных с помощью функций `head()`, `info()`, `describe()`. Проверены пропуски и дубликаты данных.
3. **Визуализация данных**: Построены гистограммы для визуализации распределения LTV и countplot'ы для анализа распределения категориальных признаков.
4. **Преобразование данных**: Категориальные признаки были преобразованы в числовые с помощью `LabelEncoder`, а числовые признаки стандартизированы с помощью `StandardScaler`.
5. **Создание бинарной целевой переменной**: Бинарная переменная `LTV_binary` была создана на основе медианы LTV.
6. **Построение и оценка моделей**: Использованы три модели: логистическая регрессия, решающее дерево и случайный лес. Проведена кросс-валидация с оценкой по метрике ROC-AUC.
7. **Анализ важности признаков**: На основе обученной модели случайного леса проведена оценка важности признаков.

## Используемые библиотеки

- pandas
- matplotlib
- seaborn
- scikit-learn
- gdown

## Оценка моделей

Три модели машинного обучения были оценены с помощью кросс-валидации по метрике ROC-AUC:

- **Логистическая регрессия**: 0.7497
- **Решающее дерево**: 0.9877
- **Случайный лес**: 0.9992

### Итоговая модель

Случайный лес был выбран в качестве итоговой модели, так как он показал наивысшую точность (ROC-AUC 0.9992) и устойчивость к переобучению.

## Важность признаков

Анализ важности признаков, выполненный на модели случайного леса, показал, что наиболее важные переменные для классификации LTV включают:

- Месячная премия за автострахование
- Общее количество требований по страхованию
- Доход клиента
- Другие

## Использование

Для запуска проекта выполните следующие шаги:

1. Клонируйте репозиторий:

    ```sh
    git clone <https://github.com/eghrthrjdtsed/Data_Science.git>
    ```

2. Перейдите в директорию репозитория:

    ```sh
    cd <analysis_LTV>
    ```

3. Установите необходимые библиотеки:

    ```sh
    pip install -r requirements.txt
    ```

4. Запустите Jupyter Notebook и откройте файл `analysis_LTV.ipynb`.

5. Выполните все ячейки в ноутбуке для воспроизведения анализа и построения моделей.




