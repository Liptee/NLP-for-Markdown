В данном репозитории представлена разработка приложения в области NLP (Natural Language Processing) для автоматического тэгирования и линкования текстовых документов в рамках приложения [Obsidian](https://obsidian.md/).

В папке **IMGS** содержатся изображения для .ipynb файлов в папке **documentations**, которая содержит туториалы по использованным в разработке библиотекам.

В папке **data** находятся сборники текстовых данных на которых производится тестирование различных моделей. Всего разработка ведется для двух языков, соответственно тестируемые текстовые корпуса разбиты на два набора: *ru* и *en*. 

Предусмотрено подключение виртуальной рабочей среды через [pipenv](https://pypi.org/project/pipenv/).

### conf.py
Данный файл содержит различные настройки, используемые для алгоритмов моделей.

### funcs.py
Содержит коллекцию часто используемых функций.

Далее будут мысли и записи о конкретных моделях и их проблемах.

## natasha_ru
**Текущее состояние файла**: полностью рабочий.
**Потенциал:** высокий

Модель использует библиотеку [natasha](https://pypi.org/project/natasha/), которая разработана для решения задач NLP для русского языка. Библиотека хвастается своей скоростью и удобством. Получилось добиться нахождения NER (именованных сущностей) от данной модели. 

## nltk_en.py
**Текущее состояние файла:** работает некорректно (ошибка кодировщика).
**Потенциал:** средний

Модель использует библиотеку [NLTK](https://pypi.org/project/nltk/) для решения проблемы в английском языке. Модель отстает по производительности от **SpaCy**, хотя есть подозрение, что текущий код можно оптимизировать. В целом неплохо справляется с нахождением NER.

**Дальнейшая разработка NER зависит от достижения результатов Spacy модели**

## nltk_ru.py
**Текущее состояние файла:** полностью рабочий.
**Потенциал:** низкий

Модель использует библиотеку NLTK для решения проблемы в русском языке. На сырой обработке показывает ужасные результаты для русскоязычной модели (в NER включает такие слова, как: "Такие", "Этот", "Но" и т.д.). Мало результативности.

## spacy_en.py
**Текущее состояние файла:** полностью рабочий.
**Потенциал:** выше среднего

Модель испольузет библиотеку [Spacy](https://spacy.io/) для решения проблемы в английском языке. Для данной модели в файле `conf.py` находятся три категории NER (положительные, нейтральные и отрицательные), что соответсвует критериям необходимости включения их в поиск NER. По субъективной оценке справляется чуть хуже, чем его аналог в `nltk_en.py`, но SpaCy имеет вполне понятную инструкцию по обучению или дообучению модели, а также множество возможных вариантов различных уже готовых моделей. На данный момент для работы использовалась только модель `en_core_web_sm`. Модель на основе SpaCy демонстрирует большую производительность по сравнению с его аналогом из NLTK.

## spacy_ru.py
**Текущее состояние:** работает. **Потенциал:** ниже среднего

Модель использует библиотеку SpaCy для решения проблемы для русского языка. На данный момент модель показывает низкие результаты, которые можно исправить.

## wiki_saver.py
**Текущее состояние:** работает

Инструмент для сохранения статей википедии в формате `.md`