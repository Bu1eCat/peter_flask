### Python 常用方法

##### .format()

```python
class Person:
    """docstring for Person."""
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print('Hello,how are you? my name is {0}'
                                                .format(self.name))
p = Person('Person')
p.say_hi()

在拼接字符串中使用{} ,可以在.format() 中传入对应的参数，默认以{0}开始。
```
##### .strftime()
```python
now = time.strftime("%Y-%m-%d %H:%M:%S")   #获取当前时间
```

##### python字段迭代

默认情况下，dict迭代的是key。
如果要迭代value，可以用for value in d.values()，
如果要同时迭代key和value，可以用for k, v in d.items()  

##### 判断参数是否可迭代：
``` python
>>> from collections import Iterable
>>> isinstance('abc', Iterable)
>>> True
```
#####  对list实现下标循环
``` python
>>> for i, value in enumerate(['A', 'B', 'C']):
... print(i, value)
...
0 A
1 B
2 C
```

##### isinstance函数
判断一个变量是不是字符串：
``` python
>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False
```
##### join()函数
语法：  'sep'.join(seq)
``` python
>>> seq1 =['hello','good','boy','doiido']

>>> print ' '.join(seq1)
hello good boy doiido
>>> print ':'.join(seq1)
hello:good:boy:doiido
```
参数说明

sep：分隔符。可以为空

seq：要连接的元素序列、字符串、元组、字典(只能对key进行提取合并)
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串

返回值：返回一个以分隔符sep连接各个元素后生成的字符串

##### os.path.join()函数

语法：  os.path.join(path1[,path2[,......]])

返回值：将多个路径组合后返回

注：第一个绝对路径之前的参数将被忽略
