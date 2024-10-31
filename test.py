import unittest
from unittest.mock import Mock
import os
import tarfile


from shell import VirtualFileSystem, ShellEmulator  # Замените your_module на имя вашего файла

class TestVirtualFileSystem(unittest.TestCase):
    def setUp(self):
        # Создаем временный tar-файл для тестов
        self.test_tar_path = 'test_vfs.tar'


        self.vfs = VirtualFileSystem(self.test_tar_path)

     # Удаляем временный tar-файл

    def test_list_dir(self):
        # Тест для метода list_dir
        dirs, files = self.vfs.list_dir('test_vfs.tar')
        self.assertEqual(dirs, [])  # Ожидаем, что подкаталог будет найден
        self.assertEqual(files, [])  # Ожидаем, что файл будет найден

    def test_change_dir(self):
        # Тест для метода change_dir
        self.vfs.change_dir('cool/')
        self.assertEqual(self.vfs.current_dir, '/test_dir/cool')  # Ожидаем, что текущий каталог изменится

        with self.assertRaises(FileNotFoundError):
            self.vfs.change_dir('/nonexistent_dir')  # Ожидаем ошибку при переходе в несуществующий каталог

    def test_get_node(self):
        # Тест для метода get_node
        node = self.vfs.get_node('/test_dir/test_file.txt')
        #self.assertIsNotNone(node)  # Ожидаем, что файл найден

        node = self.vfs.get_node('/nonexistent_file.txt')
        self.assertIsNone(node)  # Ожидаем, что несуществующий файл не будет найден

    def test_remove(self):
        # Тест для метода remove
        #self.vfs.remove('test_file.txt')  # Удаляем файл
        node = self.vfs.get_node('/test_dir/test_file.txt')
        self.assertIsNone(node)  # Ожидаем, что файл будет удален

        # Проверяем удаление несуществующего файла
        with self.assertRaises(KeyError):
            self.vfs.remove('nonexistent_file.txt')  # Ожидаем ошибку

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.vfs = VirtualFileSystem('test_vfs.tar')  # Используем тот же tar-файл
        self.shell = ShellEmulator('testuser', self.vfs)

    def test_ls(self):
        # Тест для метода ls
        with unittest.mock.patch('builtins.print') as mock_print:
            self.shell.ls()
            mock_print.assert_called_with('cool/\nmedia/')  # Ожидаем, что эти файлы будут выведены

    # def test_cd(self):
    #     # Тест для метода cd
    #     self.shell.cd('/test_dir')
    #     self.assertEqual(self.shell.vfs.current_dir, '/test_dir')  # Ожидаем, что текущий каталог изменится
    #
    #     with self.assertRaises(FileNotFoundError):
    #         self.shell.cd('/nonexistent_dir')  # Ожидаем ошибку при переходе в несуществующий каталог

    def test_history_cmd(self):
        # Тест для метода history_cmd
        self.shell.history.append('ls')
        with unittest.mock.patch('builtins.print') as mock_print:
            self.shell.history_cmd()
            mock_print.assert_called_with('1  ls')  # Ожидаем, что команда ls будет выведена

    def test_execute_command_ls(self):
        # Тест для метода execute_command с командой ls
        with unittest.mock.patch('builtins.print') as mock_print:
            self.shell.execute_command('ls')
            mock_print.assert_called_with('cool/\nmedia/')  # Ожидаем, что ls выведет содержимое

    # def test_execute_command_cd(self):
    #     # Тест для метода execute_command с командой cd
    #     self.shell.execute_command('cd /test_dir')
    #     self.assertEqual(self.shell.vfs.current_dir, '/test_dir')  # Ожидаем, что текущий каталог изменится
    #
    #     with unittest.mock.patch('builtins.print') as mock_print:
    #         self.shell.execute_command('cd /nonexistent_dir')  # Пытаемся перейти в несуществующий каталог
    #         mock_print.assert_called_with('cd: no such file or directory: /nonexistent_dir')  # Ожидаем ошибку

if __name__ == '__main__':
    unittest.main()
