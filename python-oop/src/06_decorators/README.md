# Property Dekoratörleri - Getters, Setters ve Deleters

Bu eğitim, Python'da property dekoratörlerinin getter, setter ve deleter işlevselliğini uygulamak için nasıl kullanılacağını anlatmaktadır. Property dekoratörleri, diğer programlama dillerindeki özelliklere benzer şekilde, sınıf niteliklerini daha sezgisel ve temiz bir yaklaşımla yönetmeyi sağlar.

## Property Dekoratörlerine Giriş

Python'daki property dekoratörü, bir yöntemin bir öznitelikmiş gibi erişilmesine izin verir. Bu özellik, özellikle bir niteliğin değerinin sınıf içindeki diğer niteliklere bağlı olduğu durumlarda kullanışlıdır.

### Örnek Senaryo

`email` niteliğinin `first_name` ve `last_name` niteliklerinden türetildiği bir `Employee` sınıfını düşünün. `first_name` veya `last_name` değiştiğinde, `email`in otomatik olarak bu değişiklikleri yansıtacak şekilde güncellenmesi gerekir. Property dekoratörleri kullanarak, bunu sınıfın arayüzünü değiştirmeden başarabiliriz.

### İlk Ayar

İlgili niteliklere ve yöntemlere odaklanan sadeleştirilmiş bir `Employee` sınıfı:

```python
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name}.{last_name}@email.com"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

### Sorun

İlk uygulamada, `first_name` veya `last_name` değiştirildiğinde `email` niteliği otomatik olarak güncellenmez. Bu durum tutarsızlıklara yol açabilir. Örneğin:

```python
emp = Employee('John', 'Smith')
emp.first_name = 'Jim'
print(emp.email)  # Çıktı: John.Smith@email.com (Yanlış)
```

### Property Dekoratörlerinin Kullanımı

#### Getter

Öncelikle, `email` niteliğini bir property'ye dönüştüreceğiz. Bu, bir `email` yöntemi tanımlamayı ve `@property` dekoratörünü kullanmayı içerir.

```python
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

Bu değişiklikle, `email` mevcut `first_name` ve `last_name` değerlerine dayalı olarak dinamik olarak hesaplanır.

#### Setter

`full_name`in doğrudan ayarlanmasına izin vermek için, hem `first_name` hem de `last_name`i güncelleyecek şekilde, `@<property_name>.setter` dekoratörünü kullanacağız.

```python
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last
```

Artık `full_name`i doğrudan ayarlayabilir ve bu, `first_name` ve `last_name`i uygun şekilde güncelleyecektir:

```python
emp = Employee('John', 'Smith')
emp.full_name = 'Jim Beam'
print(emp.first_name)  # Çıktı: Jim
print(emp.last_name)   # Çıktı: Beam
print(emp.email)       # Çıktı: Jim.Beam@email.com
```

#### Deleter

Son olarak, `full_name` niteliği silindiğinde temizlik işlemlerini gerçekleştirmek için bir deleter tanımlayabiliriz.

```python
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self():
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        print("Deleting name!")
        self.first_name = None
        self.last_name = None
```

Deleter ile, `full_name` niteliği silindiğinde temizlik kodu tetiklenecektir:

```python
emp = Employee('John', 'Smith')
del emp.full_name
print(emp.first_name)  # Çıktı: None
print(emp.last_name)   # Çıktı: None
```

### Sonuç

Python'daki property dekoratörleri, sınıf niteliklerini yönetmek için güçlü bir mekanizma sağlar. `@property`, `@<property_name>.setter` ve `@<property_name>.deleter` kullanarak, nitelik değişikliklerinin doğru şekilde yönetildiğinden emin olabiliriz, sınıf arayüzünü bozmadan. Bu yaklaşım, kod okunabilirliğini ve sürdürülebilirliğini artırırken, karmaşık nitelik yönetimi için gereken esnekliği sağlar.