# Отчет о проекте "Скрапинг новостей с Hacker News"

## URL сайта:
URL сайта: [Hacker News](https://news.ycombinator.com/)

## Описание:
Цель проекта - извлечение заголовков статей и соответствующих URL ссылок с главной страницы Hacker News.

## Подход:
1. Использовался Selenium для автоматизации веб-браузера и загрузки страницы Hacker News.
2. Затем страница была пропарсена с помощью BeautifulSoup для извлечения данных.
3. С использованием Selenium и CSS-селекторов были найдены и извлечены заголовки статей и соответствующие URL ссылок.

## Трудности:
1. Одной из проблем была динамическая загрузка контента на странице Hacker News. Решение: использование явных ожиданий с помощью метода WebDriverWait для ожидания загрузки элементов.
2. Еще одной проблемой была необходимость правильного выбора CSS-селекторов для точного нахождения элементов. Решение: использование инструментов разработчика браузера для анализа структуры страницы и тестирования селекторов.

## Результаты:
Образец извлеченных данных был сохранен в файл JSON:

```json
[
    {
        "title": "Sphinx: Open source search engine",
        "link": "https://github.com/sphinxsearch/sphinx"
    },
    {
        "title": "Many AWS services currently down [status.aws.amazon.com]",
        "link": "https://status.aws.amazon.com/"
    },
    {
        "title": "Scott Aaronson's 20-page rebuttal to those claiming P vs NP is ‘easy’",
        "link": "https://www.scottaaronson.com/blog/?p=5599"
    },
    ...
]
