# Кофигурационное управление
### Домашнее задание 1

#### Условие задания
Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
tar. Эмулятор должен работать в режиме CLI.
Ключами командной строки задаются:
• Имя пользователя для показа в приглашении к вводу.
• Путь к архиву виртуальной файловой системы.
Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:
1. history.
2. wc.

Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 2 теста.


## Запуск программы
Откройте командную строку и выполните следующую команду, подставив свое имя пользователя и путь к tar-архиву
### python имя_вашего_файла.py --user ваше_имя_пользователя --vfs путь_к_tar_архиву


## Доступные функции и их описание
#### 1. ls

Описание: Отображает содержимое текущего каталога, включая подкаталоги и файлы.

Использование: Введите ls и нажмите Enter. Если в текущем каталоге есть файлы или папки, они будут перечислены.

#### 2. cd <путь>

Описание: Изменяет текущий каталог на указанный. Вы можете переходить в подкаталоги или подниматься на уровень вверх

Использование:

Для перехода в подкатолог: cd <ваш подкаталог>

Для перехода на уровень выше: cd ..

Чтобы вернуться в корень: cd / 

#### 3. exit

Описание: Завершает работу эмулятора.

Использование: Введите exit и нажмите Enter.

#### 4. history
   
Описание: Показывает историю введенных команд.

Использование: Введите history и нажмите Enter, чтобы увидеть список ранее выполненных команд.

#### 5. wc <имя_файла>

Описание: Отображает размер указанного файла в байтах.

Использование: Введите wc <имя_файла>




# Классы и функции 
Конечно! Вот описание классов и функций без вставок кода:

### Классы и их описание

1. **VirtualFileSystem**
   - **Методы**:
     - `__init__(self, tar_path)`: Инициализирует виртуальную файловую систему, открывая указанный tar-архив и строя файловую структуру.
     - `build_file_tree(self)`: Создает иерархию файлов и директорий из tar-архива.
     - `list_dir(self, path)`: Возвращает списки подкаталогов и файлов в указанном каталоге.
     - `change_dir(self, path)`: Меняет текущий каталог на указанный, проверяя его существование.
     - `get_node(self, path)`: Возвращает узел (файл или директорию) по указанному пути.
     - `remove(self, path)`: Удаляет указанный файл или директорию из текущего каталога.

2. **ShellEmulator**
   - **Методы**:
     - `__init__(self, username, vfs)`: Инициализирует эмулятор командной строки с указанным именем пользователя и виртуальной файловой системой.
     - `run(self)`: Запускает основной цикл командной строки, принимая и обрабатывая команды пользователя.
     - `execute_command(self, command)`: Обрабатывает и выполняет введенную команду.
     - `ls(self)`: Выводит содержимое текущего каталога.
     - `cd(self, path)`: Изменяет текущий каталог на указанный путь.
     - `history_cmd(self)`: Отображает историю введенных команд.
     - `wc(self, filename)`: Выводит размер указанного файла в байтах.

### Использование классов и методов

- **VirtualFileSystem** предоставляет функциональность для работы с виртуальной файловой системой, позволяя загружать структуру из tar-архива и взаимодействовать с файлами и директориями.
  
- **ShellEmulator** управляет взаимодействием с пользователем через командную строку, обрабатывая команды и выводя информацию о текущем состоянии файловой системы.

Эти классы и методы обеспечивают основные функции для работы с виртуальной файловой системой и эмуляции командной строки.


# Примеры использования

![image](https://github.com/user-attachments/assets/254b3bb8-ffd7-4eb5-8841-5719c18ed477)


![image](https://github.com/user-attachments/assets/f5c7755d-93d8-41e9-97a4-f6b0c156350d)


![image](https://github.com/user-attachments/assets/b1378f75-c692-4f34-91d1-19e2cf709e9c)


![image](https://github.com/user-attachments/assets/2c38856b-1222-4bfb-82de-87fdedbe0c1b)



# Тестирование
unittest — это модуль для тестирования в Python, который позволяет разработчикам создавать и выполнять тесты для своих программ. Он является частью стандартной библиотеки Python и предоставляет инструменты для написания, организации и выполнения тестов.

![image](https://github.com/user-attachments/assets/9a30b93d-76ad-45f2-8bb8-48892001468c)


![image](https://github.com/user-attachments/assets/1859ca94-bed3-463a-af2b-404950a45e21)


# Результаты тестирования
![image](https://github.com/user-attachments/assets/a6386da8-f992-4843-8e80-e065bcc64206)





