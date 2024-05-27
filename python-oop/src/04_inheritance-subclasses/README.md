# Kalıtım - Alt Sınıflar Oluşturma

Python'da kalıtım, mevcut bir sınıftan (ebeveyn sınıf) özellikleri ve yöntemleri devralan yeni bir sınıf (alt sınıf) oluşturmamıza olanak tanır. Bu özellik, kodun yeniden kullanılmasını ve mantıksal bir sınıf hiyerarşisi oluşturulmasını sağlar, böylece kodumuz daha düzenli ve sürdürülebilir hale gelir.

## Alt Sınıflar Oluşturma

Çalışmakta olduğumuz `Employee` sınıfını düşünün. Daha spesifik türde çalışanlar oluşturmak için, örneğin geliştiriciler ve yöneticiler, alt sınıflar oluşturabiliriz. Hem geliştiricilerin hem de yöneticilerin isim, e-posta ve maaş gibi özellikleri olacaktır ve bunlar zaten `Employee` sınıfında tanımlanmıştır. `Employee` sınıfından kalıtım yaparak bu kodu kopyalamadan yeniden kullanabiliriz.

## Alt Sınıf Oluşturma Örneği

Başlangıç olarak `Employee` sınıfından kalıtım yapan bir `Developer` alt sınıfı oluşturalım.

```python
class Employee:
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay
        
    def fullname(self):
        return f"{self.first} {self.last}"
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Developer alt sınıfını oluşturma
class Developer(Employee):
    pass
```

Boş bir gövdeye sahip olsa bile, `Developer` `Employee` sınıfından tüm özellikleri ve yöntemleri devralır.

## Alt Sınıf Örnekleri Oluşturma

Şimdi `Developer` örnekleri oluşturabilir ve `Employee` gibi davrandıklarını görebiliriz.

```python
dev_1 = Developer('John', 'Doe', 50000)
print(dev_1.email)  # Çıktı: john.doe@company.com
```

## Alt Sınıfları Özelleştirme

Bir alt sınıfı özelleştirmek için yöntemleri ve özellikleri geçersiz kılabilir veya genişletebiliriz. Örneğin, geliştiricilerin farklı bir zam miktarına sahip olabileceğini varsayalım.

```python
class Developer(Employee):
    raise_amount = 1.10
```

Artık, bir `Developer` örneğine zam uyguladığımızda, geçersiz kılınan `raise_amount` kullanılır.

```python
dev_1 = Developer('John', 'Doe', 50000)
dev_1.apply_raise()
print(dev_1.pay)  # Çıktı: 55000 (10% zam)
```

## Yeni Özellikler Ekleme

Geliştiricinin bildiği programlama dilini gibi yeni bir özellik eklemek istediğimizi varsayalım. Bunun için `__init__` yöntemini geçersiz kılmamız gerekecek.

```python
class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
```

`super()` kullanarak, `Employee` sınıfının `__init__` yöntemini çağırırız ve `first`, `last` ve `pay`'in orada başlatılmasını sağlarız. Daha sonra `prog_lang`'i `Developer` alt sınıfında başlatırız.

```python
dev_1 = Developer('John', 'Doe', 50000, 'Python')
print(dev_1.prog_lang)  # Çıktı: Python
```

## Başka Bir Alt Sınıf Oluşturma: Manager

Yöneticiler için bir alt sınıf oluşturalım, yöneticiler çalışanları denetleyebilir.

```python
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())
```

## Manager Sınıfını Kullanma

```python
dev_1 = Developer('John', 'Doe', 50000, 'Python')
dev_2 = Developer('Jane', 'Doe', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_employee(dev_2)
mgr_1.print_employees()
# Çıktı:
# --> John Doe
# --> Jane Doe
```

## Built-in Fonksiyonlar: `isinstance` ve `issubclass`

Python, kalıtımla çalışmak için iki yerleşik fonksiyon sağlar:

- `isinstance(obj, class)`: `obj`'nin bir sınıfın örneği olup olmadığını kontrol eder.
- `issubclass(sub, sup)`: `sub`'ın `sup`'un bir alt sınıfı olup olmadığını kontrol eder.

```python
print(isinstance(mgr_1, Manager))  # True
print(isinstance(mgr_1, Employee))  # True
print(isinstance(mgr_1, Developer))  # False

print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Employee))  # True
print(issubclass(Manager, Developer))  # False
```

## Gerçek Dünya Örneği: Flask'ın HTTPException Sınıfı

Flask web framework'ünde, `HTTPException` sınıfı, farklı HTTP hataları için belirli istisnalar oluşturarak alt sınıflamayı gösterir.

```python
from werkzeug.exceptions import HTTPException

class BadRequest(HTTPException):
    code = 400
    description = 'Bad Request'
```

`HTTPException` sınıfından kalıtım yaparak, `BadRequest` bu sınıfın tüm işlevselliğini devralır ve yalnızca gerekli olanı özelleştirir.

## Sonuç

Kalıtım, ebeveyn sınıflardan alt sınıflara kod yeniden kullanımı ve mantıksal sınıf hiyerarşisi oluşturulmasını sağlar. İhtiyaç duyulduğunda işlevselliği geçersiz kılabilir ve genişletebiliriz, böylece kodumuz daha modüler ve yönetilebilir hale gelir.