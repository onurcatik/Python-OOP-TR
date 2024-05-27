# Sınıflar ve Örnekler

Bu eğitimde, Python'da sınıflar oluşturmayı ve kullanmayı öğreneceğiz ve dil içindeki nesne yönelimli programlama (OOP) kavramlarına odaklanacağız. Bu, OOP kavramlarını (kalıtım, sınıf ve örnek değişkenler, static methods, class methods ve daha fazlası) aşamalı olarak inceleyeceğimiz bir dizi eğitimin ilkidir.

## Neden Sınıflar Kullanılır?

- Sınıflar, OOP'nin temel bir parçasıdır ve çoğu modern programlama dilinde kullanılır. 
- Verilerimizi ve fonksiyonlarımızı (sırasıyla attributes ve methods olarak adlandırılır) mantıklı bir şekilde gruplayarak yeniden kullanılabilirliği ve ölçeklenebilirliği artırırlar. 
- Sınıf oluşturma ve bunları yönetme, verimli ve bakımı kolay kod yazmak için önemlidir.

## Temel Bir Sınıf Oluşturma

- Başlangıç olarak, bir çalışanı temsil eden basit bir sınıf oluşturalım. 
- Python'da bir sınıf, `class` anahtar kelimesi ve sınıf adı kullanılarak tanımlanır. 
- İşte boş bir sınıfın nasıl tanımlandığı:

```python
class Employee:
    pass
```

`pass` ifadesi, burada henüz tanımlanmamış attributes veya methods olduğunu belirtmek için kullanılır.

## Sınıf ve Örnek Farkı

- Bir sınıf, örnekler oluşturmak için bir şablon görevi görür. 
- Her örnek, sınıfa dayalı benzersiz bir nesneyi temsil eder. Örneğin:

```python
employee1 = Employee()
employee2 = Employee()
```

Bu örnekte, `employee1` ve `employee2` `Employee` sınıfının farklı örnekleridir.

## Örneklerin Attributes Eklemek

Örnek değişkenleri, her örneğe özgü verileri içerir. Bir örneğe manuel olarak attributes ekleyebiliriz:

```python
employee1.first_name = 'onur'
employee1.last_name = 'catik'
employee1.email = 'onur.catik@mail.com'
employee1.pay = 50000

employee2.first_name = 'Test'
employee2.last_name = 'User'
employee2.email = 'test.user@mail.com'
employee2.pay = 60000
```

## `__init__` Method Kullanımı

- Bu attributes'ları bir örnek oluştururken otomatik olarak ayarlamak için, `__init__` method kullanırız, bu initializer veya constructor olarak da bilinir. 
- `__init__` method, örnek değişkenlerini başlatmamızı sağlar. 
- İşte bunun nasıl tanımlandığı:

```python
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
```

Bir örnek oluştururken artık gerekli argümanları sağlıyoruz:

```python
employee1 = Employee('Corey', 'Schaefer', 50000)
employee2 = Employee('Test', 'User', 60000)
```

Bu yaklaşım daha verimlidir ve hataları azaltır.

## Methods Tanımlama

Methods, bir sınıfla ilişkili fonksiyonlardır. Bir çalışanın tam adını görüntülemek için bir method ekleyelim:

```python
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

Bu method'u bir örnek üzerinde şu şekilde çağırabiliriz:

```python
print(employee1.full_name())
print(employee2.full_name())
```

## Yaygın Hatalar: `self`'i Unutmak

- Yaygın hatalardan biri, metod tanımında ilk parametre olarak `self` eklemeyi unutmaktır.
- `self`'i ihmal etmek bir hataya neden olur çünkü Python, nesneyi metoda otomatik olarak geçirir.
- Bu yüzden her zaman `self` eklemeyi unutmayın.

```python
def full_name(self):
    return f"{self.first_name} {self.last_name}"
```

## Class Method ve Instance Method

Instance methods, `self` kullanarak instance'a başvururken, bunlar aynı zamanda sınıf adı kullanılarak da çağrılabilir, ancak bu durumda instance açıkça iletilmelidir:

```python
print(Employee.full_name(employee1))
```

Bu örnek, `Employee.full_name(employee1)` çağrısının `employee1.full_name()` ile eşdeğer olduğunu gösterir.

## Sonuç

- Bu eğitimde, sınıf ve örnek oluşturmanın temellerini, attributes'ları `__init__` method kullanarak başlatmayı ve methods tanımlamayı ele aldık. B
- u kavramları anlamak, Python'un OOP yeteneklerini kullanarak daha gelişmiş özellikler oluşturmak için çok önemlidir.
