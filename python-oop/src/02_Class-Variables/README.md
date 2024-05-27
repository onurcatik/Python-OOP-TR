# Sınıf Değişkenleri

Bu eğitimde, Python Nesne Yönelimli Programlama (OOP) içindeki sınıf değişkenlerini keşfedeceğiz. Önceki eğitimde, her örnek için benzersiz verileri saklayan örnek değişkenlerini ele aldık. Şimdi, bir sınıfın tüm örnekleri arasında paylaşılan sınıf değişkenlerini inceleyeceğiz.

## Sınıf Değişkenlerine Giriş

- Sınıf değişkenleri, bir sınıfın tüm örnekleri için aynı olan niteliklerdir. 
- Örnek değişkenlerinin aksine, her örnek için benzersiz olan sınıf değişkenleri, tüm örnekler arasında tutarlı bir değer korur.

### Örnek: Employee Sınıfı

- Her çalışanın `name`, `email` ve `pay` gibi niteliklere sahip olduğu bir `Employee` sınıfını düşünelim.
- Bu nitelikler, her çalışana özeldir ve örnek değişkenleridir.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay
```

### Bir Sınıf Değişkeni Ekleme

- Diyelim ki şirketimiz her yıl tüm çalışanlara zam yapıyor. 
- Tüm çalışanlar için aynı olan zam miktarı, sınıf değişkeni için uygun bir adaydır.
- Sınıf değişkenini oluşturmadan önce, zam miktarını bir yöntem içinde kodlayalım:

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
```

`apply_raise` yöntemini test etme:

```python
emp1 = Employee('John', 'Doe', 50000)
print(emp1.pay)  # Çıktı: 50000
emp1.apply_raise()
print(emp1.pay)  # Çıktı: 52000
```

### Sınıf Değişkenlerinin Tanıtılması

- Zam miktarını kodlamak ideal değildir. 
- Bunun yerine, bir sınıf değişkeni tanıtalım:

```python
class Employee:
    raise_amount = 1.04  # Sınıf değişkeni

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
```

Sınıf değişkenlerine erişim:

```python
print(Employee.raise_amount)  # Çıktı: 1.04
print(emp1.raise_amount)      # Çıktı: 1.04
```

### Sınıf ve Örnek Değişkenleri

- Niteliklere erişirken, Python öncelikle örneğin ad alanını kontrol eder. 
- Bulunamazsa, sınıfın ad alanını kontrol eder.
- Örneğin, ad alanını yazdırmayı düşünelim:

```python
emp1 = Employee('John', 'Doe', 50000)
print(emp1.__dict__)  # Örnek ad alanı: {'first': 'John', 'last': 'Doe', 'email': 'John.Doe@company.com', 'pay': 50000}
print(Employee.__dict__)  # Sınıf ad alanı (içinde 'raise_amount' bulunur)
```

### Sınıf Değişkenlerini Değiştirme

Sınıf değişkenini değiştirmek tüm örnekleri etkiler:

```python
Employee.raise_amount = 1.05
print(Employee.raise_amount)  # Çıktı: 1.05
print(emp1.raise_amount)      # Çıktı: 1.05
```

Bir örnek aracılığıyla değiştirilirse, yalnızca o örneği etkiler:

```python
emp1.raise_amount = 1.06
print(emp1.raise_amount)      # Çıktı: 1.06
print(Employee.raise_amount)  # Çıktı: 1.05
```

### Örnek: Çalışan Sayısını Takip Etme

- Sınıf değişkenlerinin yaygın bir kullanım durumu, tüm örnekler arasında paylaşılan verileri izlemektir.
- Örneğin, çalışan sayısını takip etmek:

```python
class Employee:
    num_of_employees = 0  # Sınıf değişkeni

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay
        Employee.num_of_employees += 1
```

`num_of_employees` değişkenini test etme:

```python
emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Smith', 60000)
print(Employee.num_of_employees)  # Çıktı: 2
```

## Sonuç

Sınıf değişkenleri, Python OOP'de güçlü bir özelliktir ve tüm örnekler arasında paylaşılan nitelikleri tanımlamaya olanak tanır. Sınıf değişkenleri, sınıf boyunca tutarlı özellikler ve davranışlar tanımlamak için kullanışlıdır.