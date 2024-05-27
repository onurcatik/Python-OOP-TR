class Employee:
    # Sınıf değişkenleri
    raise_amount = 1.04  # Tüm çalışanlar için zam miktarı
    num_of_employees = 0  # Toplam çalışan sayısı

    def __init__(self, first, last, pay):
        # Örnek değişkenleri
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay
        
        # Her yeni çalışan oluşturulduğunda num_of_employees artırılır
        Employee.num_of_employees += 1

    def apply_raise(self):
        # Zam miktarını uygula
        self.pay = int(self.pay * self.raise_amount)

# Çalışan örnekleri oluşturalım
emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Smith', 60000)

# Başlangıç maaşlarını yazdıralım
print(f"{emp1.first} {emp1.last} maaş: {emp1.pay}")
print(f"{emp2.first} {emp2.last} maaş: {emp2.pay}")

# Zam miktarını uygulayalım
emp1.apply_raise()
emp2.apply_raise()

# Zam uygulanmış maaşları yazdıralım
print(f"{emp1.first} {emp1.last} zam sonrası maaş: {emp1.pay}")
print(f"{emp2.first} {emp2.last} zam sonrası maaş: {emp2.pay}")

# Sınıf değişkenlerine erişim
print(f"Zam miktarı: {Employee.raise_amount}")
print(f"Toplam çalışan sayısı: {Employee.num_of_employees}")

# Sınıf değişkenini değiştirme
Employee.raise_amount = 1.05

# Sınıf değişkeninin değişiklik sonrası durumu
print(f"Yeni zam miktarı: {Employee.raise_amount}")

# Bir örnek aracılığıyla sınıf değişkenini değiştirme
emp1.raise_amount = 1.06

# Örnek ve sınıf değişkenlerinin son durumu
print(f"{emp1.first} için zam miktarı: {emp1.raise_amount}")
print(f"{emp2.first} için zam miktarı: {emp2.raise_amount}")
print(f"Sınıf için zam miktarı: {Employee.raise_amount}")

# Örnek ad alanlarını yazdırma
print(f"{emp1.first} ad alanı: {emp1.__dict__}")
print(f"{emp2.first} ad alanı: {emp2.__dict__}")

# Sınıf ad alanını yazdırma
print(f"Employee sınıf ad alanı: {Employee.__dict__}")
