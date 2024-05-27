# Özel (Magic/Dunder) Yöntemler

Bu eğitimde Python'daki özel yöntemleri (magic yöntemler veya dunder yöntemler olarak da bilinir) inceleyeceğiz. Bu yöntemler, sınıflarımızda yerleşik davranışları taklit etmemize ve operatör aşırı yüklemeyi uygulamamıza olanak tanır. Kendi özel yöntemlerimizi tanımlayarak, nesnelerimizin yerleşik fonksiyonlar ve operatörlerle nasıl etkileşime girdiğini değiştirebilir, kullanışlılıklarını ve esnekliklerini artırabiliriz.

## Özel Yöntemleri Anlamak

Özel yöntemler, çift alt çizgi ile çevrilidir (`__`), bu nedenle "dunder" (çift alt çizgi anlamına gelir) adı verilir. Bu yöntemler, çeşitli işlemleri gerçekleştirmek için Python tarafından örtük olarak çağrılır. Örneğin, bir nesne örneği oluşturulduğunda `__init__` yöntemi çağrılır ve başlangıç durumu ve öznitelikleri ayarlanır.

### Yaygın Özel Yöntemler

1. **`__init__`**: Bir sınıfın yeni bir örneğini başlatır.
2. **`__repr__`**: Nesnenin belirsiz bir temsilini sağlar, genellikle hata ayıklama için kullanılır.
3. **`__str__`**: Nesnenin okunabilir bir string temsilini döner, son kullanıcılar için kullanılır.

### Örnek: Nesne Temsilini Özelleştirme

Bir `Employee` sınıfını düşünün. Varsayılan olarak, bu sınıfın bir örneğini yazdırmak belirsiz bir çıktı verir. Bunu iyileştirmek için `__repr__` ve `__str__` kullanabiliriz.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.first} {self.last} - {self.email}"

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.com"

# Örnek kullanım
emp1 = Employee('John', 'Doe', 50000)
print(emp1)          # __str__ çağırır
print(repr(emp1))    # __repr__ çağırır
```

### Aritmetik İşlemler

Özel yöntemler, aritmetik işlemleri de özelleştirmemize olanak tanır.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __add__(self, other):
        return self.pay + other.pay

# Örnek kullanım
emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Smith', 60000)
print(emp1 + emp2)  # Çıktı: 110000
```

### Uzunluk Hesaplama

`len()` fonksiyonunu özel nesnelerde kullanmak için `__len__` yöntemini uygularız.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    def __len__(self):
        return len(self.full_name)

# Örnek kullanım
emp1 = Employee('John', 'Doe', 50000)
print(len(emp1))  # Çıktı: 8 ("John Doe" uzunluğu)
```

## Gerçek Dünya Örnekleri

### Tarih ve Zaman İşlemleri

Standart kütüphanede, `datetime` modülü özel yöntemleri yoğun bir şekilde kullanır. Örneğin, `timedelta` sınıfı `__add__` yöntemini zaman ekleme işlemleri için uygular.

```python
from datetime import timedelta

td1 = timedelta(days=5)
td2 = timedelta(days=10)
print(td1 + td2)  # Çıktı: 15 days, 0:00:00
```

### Eşitlik ve Karşılaştırma

`__eq__`, `__lt__` ve `__gt__` gibi özel yöntemler karşılaştırma işlemlerini etkinleştirir.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __eq__(self, other):
        return self.pay == other.pay

    def __lt__(self, other):
        return self.pay < other.pay

# Örnek kullanım
emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Smith', 60000)
print(emp1 == emp2)  # Çıktı: False
print(emp1 < emp2)   # Çıktı: True
```

## Sonuç

Özel yöntemler, Python sınıflarının işlevselliğini ve esnekliğini önemli ölçüde artırır. Bu yöntemleri anlayarak ve kullanarak, daha sezgisel ve güçlü özel nesneler oluşturabilirsiniz.