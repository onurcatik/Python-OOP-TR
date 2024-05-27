# `classmethods` ve `staticmethods`

Bu derste, Python'daki regular methods, class methods ve static methods arasındaki farkları inceleyeceğiz. Bu ayrımları anlamak, temiz ve verimli nesne yönelimli kod yazmak için çok önemlidir.

## Regular Methods

Bir sınıftaki regular methods otomatik olarak ilk argüman olarak instance'ı alır. Bu argümana genellikle `self` adını veririz. Bu yöntemler instance üzerinde çalışır ve instance özelliklerine erişebilir ve bunları değiştirebilir.

```python
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
```

Yukarıdaki örnekte, `fullname`, `self`'i ilk argüman olarak alan ve bu sayede `first_name` ve `last_name` gibi instance özelliklerine erişebilen bir regular method'dur.

## Class Methods

Class methods, ilk argüman olarak sınıfın kendisini alır, buna genellikle `cls` deriz. Bir class method tanımlamak için `@classmethod` decorator'ını kullanın.

### Class Method Oluşturma

Bir class-level değişken ayarlamak için bir class method tanımlayalım.

```python
class Employee:
    raise_amount = 1.04
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
```

Burada, `set_raise_amount`, `raise_amount` class değişkenini ayarlayan bir class method'dur. Geleneksel olarak, sınıfı temsil ettiğini belirtmek için ilk parametre adı olarak `cls` kullanırız, bu bir instance değildir.

### Class Methods'u Alternatif Yapıcılar Olarak Kullanma

Class methods, nesneleri başlatmanın farklı yollarını sağlayarak alternatif yapıcılar olarak da kullanılabilir.

```python
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
    
    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, int(pay))

emp_str = 'John-Doe-70000'
new_emp = Employee.from_string(emp_str)
print(new_emp.email)
```

Bu örnekte, `from_string`, bir dizeyi ayrıştıran ve yeni bir `Employee` instance'ı döndüren bir class method'dur.

## Static Methods

Static methods herhangi bir özel ilk argüman almaz. Normal fonksiyonlar gibi davranırlar ancak sınıfın ad alanına aittirler. Bir static method tanımlamak için `@staticmethod` decorator'ını kullanın.

### Static Method Oluşturma

Static methods, sınıfla mantıksal bir bağlantıya sahip olan ancak sınıf veya instance değişkenlerine ihtiyaç duymayan yardımcı işlevler için kullanılır.

```python
class Employee:
    
    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)  # 5 = Cumartesi, 6 = Pazar
```

Bu örnekte, `is_workday`, verilen bir günün iş günü olup olmadığını kontrol eden bir static method'dur. `self` veya `cls`'ye erişmesi gerekmediği için static method olarak uygundur.

### Static Methods'u Kullanma

Static methods sınıf veya instance üzerinden çağrılabilir.

```python
import datetime

my_date = datetime.date(2023, 5, 15)
print(Employee.is_workday(my_date))  # True ise my_date bir iş günüdür
```

## Özet

- **Regular Methods**: Instance üzerinde çalışır ve ilk argüman olarak `self` alır.
- **Class Methods**: Sınıf üzerinde çalışır ve ilk argüman olarak `cls` alır. Alternatif yapıcılar olarak kullanılabilir.
- **Static Methods**: İlk argüman olarak `self` veya `cls` almaz. Sınıfla mantıksal olarak bağlantılı yardımcı işlevler için kullanılır.

Bu farklı türdeki methodları anlamak, Python'da sağlam ve esnek sınıflar tasarlama yeteneğinizi artıracaktır.