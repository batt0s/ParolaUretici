# Python Parola Üretici

Python ile yazılmış basit bir parola üretici. Kodları basit ama ürettiği parolalar güçlü.
##### ! : Ben python gurusu falan değilim sadece günlük hayatta kullandığım bir yazılım yapmak istedim.


### Kullanımı

```python3 PasswordGenerator.py``` komutundan sonra birkaç saniye bekleyip parolanızı alabilirsiniz. 
Daha sonra ```python3 StrongCheker.py``` ile parolanın gücünü kontrol edebilirsiniz.


### Nasıl Çalışıyor

##### ```PasswordGenerator.py``` :
```getquote.py``` içindeki get_quote fonksiyonu evrimagaci.org sitesinden sözler bölümündeki rastgele bir sözü dönüyor.
Daha sonra bu sözün baş harflerini alıp parolanın başına ekliyor. Bu harflerden sonra rastgele bir özel karakter ekliyor.
Bir söz daha alıyor ve bunun içinden 5 tane kelimeyi rastgele seçerek ilk harflerini büyütüp parolaya ekliyor. 
Bu kelimelerden sonra rastgele bir özel karakter daha ekliyor. En son olarak sonuna 6 tane rastgele rakam ekliyor.

##### ```StrengthChecker.py```:
Parolanızı aldıktan sonra bu parolanın [Utku Şen](http://github.com/utkusen)'in yapmış olduğu Türkçe wordlistin içinde olup olmadığını kontrol ediyor. İçinde ise skor 0/7. Eğer içinde değilse; parolanın uzunluğuna bakıp ona göre uzunluğa bağlı bir skor ekliyor daha sonra içinde bulunan karakter tiplerine göre. Toplam skor belli oluyor ve size parolanızın gücünü söylüyor.
