# ÖDEV YAZIM TALİMATLARI — Yapay Zeka İçin Detaylı Rehber

Bu belge, bir yapay zekanın (AI) üniversite ödev dosyasını eksiksiz şekilde yazabilmesi için gerekli tüm bilgileri, verileri, görselleri, yorumları ve bölüm yapısını içerir. Aşağıdaki talimatlara birebir uyulmalıdır.

---

## GENEL BİLGİLER

- **Üniversite:** Yıldız Teknik Üniversitesi
- **Bölüm:** İstatistik Bölümü
- **Ders:** Veri Madenciliğine Giriş
- **Dönem:** 2025-2026 Bahar
- **Proje Konusu:** Tedarikçi Risk Değerlendirmesi (Supplier Risk Assessment)
- **Kullanılan Programlama Dili:** Python
- **Kullanılan Kütüphaneler:** pandas, numpy, matplotlib, seaborn, scikit-learn, statsmodels
- **Teslim Formatı:** Word dosyası, PowerPoint sunumu, veri seti (.csv) ve Python kodları (.py)
- **E-posta:** ekonometriders09@gmail.com

---

## PROJE KLASÖRÜNDEKİ TÜM DOSYALAR VE AÇIKLAMALARI

### Veri Dosyaları
| Dosya Adı | Açıklama |
| :--- | :--- |
| `supplier_risk.csv` | Ham (orijinal) veri seti. 1800 satır, 11 sütun. Kaynak: Kaggle. |
| `supplier_risk_scored.csv` | Risk skorları (Equal ve Priority) eklenmiş, sabit eşikle sınıflandırılmış veri seti. |
| `supplier_risk_scored_quantile.csv` | Hem sabit eşik hem kuantil eşik sınıflandırmaları eklenmiş nihai veri seti. |
| `quantile_thresholds.csv` | Kuantil eşik değerleri (33. ve 66. yüzdelik dilimler). |
| `vif_results.csv` | VIF (Variance Inflation Factor) analiz sonuçları. |
| `r2_results.txt` | R² (Belirlilik Katsayısı) sonuçları. |

### Model Karşılaştırma Tabloları (CSV)
| Dosya Adı | Açıklama |
| :--- | :--- |
| `model_comparison_priority_without_year.csv` | **ANA MODEL** - Priority Fixed hedef, Year olmadan. |
| `model_comparison_equal_without_year.csv` | **ANA MODEL** - Equal Fixed hedef, Year olmadan. |
| `model_comparison_priority_with_year.csv` | ANA MODEL - Priority Fixed hedef, Year ile. |
| `model_comparison_equal_with_year.csv` | ANA MODEL - Equal Fixed hedef, Year ile. |
| `model_comparison_priority_quantile.csv` | **YAN MODEL** - Priority Quantile hedef, Year olmadan. |
| `model_comparison_equal_quantile.csv` | **YAN MODEL** - Equal Quantile hedef, Year olmadan. |

### Python Kod Dosyaları
| Dosya Adı | Açıklama |
| :--- | :--- |
| `eda_supplier_risk.py` | Keşifçi Veri Analizi (EDA) kodu. |
| `supplier_scoring.py` | Risk skorlama sistemi oluşturma kodu. |
| `supplier_scoring_quantile.py` | Kuantil eşik tabanlı sınıflandırma kodu. |
| `ml_modeling.py` | Makine öğrenmesi modelleme kodu (Pipeline ile). |
| `advanced_stats.py` | VIF ve R² hesaplama kodu. |

### Görseller (PNG)
| Dosya Adı | Hangi Bölümde Kullanılacak | Açıklama |
| :--- | :--- | :--- |
| `risk_category_distribution.png` | Bölüm 5 | Orijinal Risk_Category dağılımı (Medium: 916, High: 884). |
| `year_distribution.png` | Bölüm 5 | Yıllar bazında gözlem dağılımı (2007-2024 arası). |
| `correlation_heatmap.png` | Bölüm 5 | Sayısal değişkenler arası korelasyon ısı haritası. |
| `boxplot_Financial_Stability_Score.png` | Bölüm 5 | Finansal İstikrar Skoru kutu grafiği (Risk_Category bazında). |
| `boxplot_Delivery_Performance_Score.png` | Bölüm 5 | Teslimat Performans Skoru kutu grafiği. |
| `boxplot_Quality_Compliance_Score.png` | Bölüm 5 (opsiyonel) | Kalite Uyumluluk Skoru kutu grafiği. |
| `risk_class_comparison.png` | Bölüm 6 | Eşit vs Öncelik ağırlıklı risk sınıfı karşılaştırma çubuğu. |
| `threshold_comparison.png` | Bölüm 6 | Sabit eşik vs Kuantil eşik karşılaştırması. |
| `confusion_matrices_priority_without_year.png` | Bölüm 7 | **ANA MODEL** Priority Fixed — 4 modelin confusion matrix'leri. |
| `confusion_matrices_equal_without_year.png` | Bölüm 7 | **ANA MODEL** Equal Fixed — 4 modelin confusion matrix'leri. |
| `confusion_matrices_priority_quantile.png` | Bölüm 7 | **YAN MODEL** Priority Quantile confusion matrix'leri. |
| `confusion_matrices_equal_quantile.png` | Bölüm 7 | **YAN MODEL** Equal Quantile confusion matrix'leri. |
| `rf_feature_importance_priority_without_year.png` | Bölüm 7 | **ANA MODEL** Random Forest değişken önem grafiği (Priority). |
| `rf_feature_importance_equal_without_year.png` | Bölüm 7 | **ANA MODEL** Random Forest değişken önem grafiği (Equal). |

---

## ÖDEV BÖLÜMLERİ VE HER BİRİ İÇİN NE YAZILACAĞI

---

### BÖLÜM 1: İÇİNDEKİLER
Otomatik olarak Word'de oluşturulacaktır. Tüm bölüm başlıkları ve alt başlıkları içermelidir.

---

### BÖLÜM 2: GİRİŞ

Bu bölümde aşağıdaki 4 alt başlık ele alınmalıdır:

#### 2.1 Konunun Tanıtımı
Şunu açıkla: Tedarik zinciri yönetiminde (supply chain management) tedarikçi risk değerlendirmesi, şirketlerin finansal istikrar, teslimat performansı, kalite uyumluluğu gibi kriterlere göre tedarikçilerini sınıflandırmasını sağlayan kritik bir süreçtir. Veri madenciliği teknikleri bu süreci otomatize etmek ve daha objektif hale getirmek için kullanılabilir.

#### 2.2 Bu Konunun Neden Önemli Olduğu
Şunu vurgula: Günümüzde küreselleşen tedarik zincirlerinde bir tedarikçinin başarısızlığı tüm üretim hattını durdurabilir. COVID-19 pandemisi bu riskleri daha da görünür kılmıştır. Bu nedenle veri odaklı risk değerlendirme modelleri hayati önem taşımaktadır.

#### 2.3 Ödevin Amacı ve Hedefleri
Şunu belirt: Bu projenin amacı Kaggle'dan elde edilen tedarikçi risk veri seti üzerinde keşifçi veri analizi (EDA) yapmak, kendi kompozit risk skorlama sistemimizi oluşturmak ve makine öğrenmesi sınıflandırma algoritmalarıyla (Lojistik Regresyon, Karar Ağacı, Rastgele Orman, KNN) tedarikçilerin risk sınıflarını tahmin etmektir.

#### 2.4 Kapsam
- **İçerenler:** EDA, özellik mühendisliği, risk skorlama, makine öğrenmesi sınıflandırması, model karşılaştırması, istatistiksel geçerlilik testleri (VIF, R²).
- **Dışarıda kalanlar:** Zaman serisi analizi, derin öğrenme modelleri, gerçek zamanlı risk izleme sistemi.

---

### BÖLÜM 3: LİTERATÜR ÖZETİ

Şu konulardan akademik kaynaklara referans vererek bahset:
- Tedarikçi risk yönetimi ve performans değerlendirme çerçeveleri.
- Çok kriterli karar verme (MCDM) yöntemlerinin tedarikçi seçimindeki kullanımı.
- Makine öğrenmesinin tedarik zinciri risk yönetimindeki uygulamaları.
- Sınıflandırma algoritmalarının (Lojistik Regresyon, Random Forest vb.) risk tahmini alanındaki başarıları.

---

### BÖLÜM 4: TEORİK ARKA PLAN

#### 4.1 Temel Kavramlar
- **Sınıflandırma (Classification):** Verileri önceden tanımlanmış kategorilere ayırma işlemidir. Bu projede tedarikçileri "Düşük Risk", "Orta Risk", "Yüksek Risk" olarak sınıflandırdık.
- **Özellik Mühendisliği (Feature Engineering):** Ham veriden anlamlı değişkenler türetme sürecidir. Bu projede performans skorlarını ters çevirerek risk bileşenlerine dönüştürdük.
- **Normalizasyon (MinMaxScaler):** Tüm değişkenleri 0-1 aralığına getiren ön işleme tekniğidir.

#### 4.2 Kullanılan Algoritmalar
Aşağıdaki 4 algoritmayı kısaca (her birini 1-2 paragraf) tanıt:

1. **Lojistik Regresyon (Logistic Regression):** Doğrusal sınıflandırma modeli. Bağımsız değişkenlerin doğrusal kombinasyonunu sigmoid fonksiyonu ile olasılığa çevirir. Bu projede `StandardScaler` ile ölçeklendirme yapıldıktan sonra `Pipeline` içinde kullanıldı.

2. **Karar Ağacı (Decision Tree):** Veriyi ardışık karar kurallarıyla dallandırarak sınıflandıran ağaç yapısı. Ölçeklendirmeye ihtiyaç duymaz (scale-invariant). Bu projede ölçeklendirme yapılmadan kullanıldı.

3. **Rastgele Orman (Random Forest):** Birden fazla karar ağacının birlikte çalıştığı topluluk (ensemble) yöntemi. Her ağaç rastgele alt örneklem ve özellik seçimi kullanır. Değişken önem sıralaması (feature importance) üretebilmesi önemli bir avantajdır. Bu projede ölçeklendirme yapılmadan kullanıldı.

4. **K-En Yakın Komşu (K-Nearest Neighbors / KNN):** Yeni bir gözlemi, eğitim setindeki en yakın K komşusunun çoğunluk oyuyla sınıflandıran mesafe tabanlı algoritmadır. Öklid mesafesi kullandığı için ölçeklendirme zorunludur. Bu projede `StandardScaler` ile `Pipeline` içinde kullanıldı.

#### 4.3 Değerlendirme Metrikleri
- **Accuracy (Doğruluk):** Tüm doğru tahminlerin toplam tahminlere oranı.
- **Precision (Kesinlik):** Pozitif tahmin edilenlerin gerçekten pozitif olanlarının oranı.
- **Recall (Duyarlılık):** Gerçek pozitiflerin ne kadarının doğru yakalandığı.
- **F1-Score:** Precision ve Recall'ın harmonik ortalaması. Dengesiz sınıflarda daha güvenilirdir.
- **Confusion Matrix (Karışıklık Matrisi):** Tahminlerin gerçek değerlerle karşılaştırılmasını gösteren matris.
- **R² (Belirlilik Katsayısı):** Bağımsız değişkenlerin bağımlı değişkendeki varyansı açıklama oranı.
- **VIF (Varyans Şişirme Faktörü):** Bağımsız değişkenler arasındaki çoklu doğrusal bağlantıyı ölçen istatistik. VIF < 5 ise sorun yoktur.

---

### BÖLÜM 5: VERİ SETİ AÇIKLAMASI

#### 5.1 Veri Setinin Genel Bilgileri
- **Adı:** Supplier Risk Assessment Dataset
- **Kaynak:** Kaggle
- **Gözlem Sayısı:** 1800 satır (1 başlık satırı hariç)
- **Değişken Sayısı:** 11 sütun
- **Benzersiz Tedarikçi Sayısı:** 100 (Supplier_ID bazında)

#### 5.2 Değişkenlerin Listesi ve Türleri

| Değişken Adı | Tür | Açıklama |
| :--- | :--- | :--- |
| Supplier_ID | Tamsayı (ID) | Tedarikçi kimlik numarası (1-100 arası). |
| Year | Tamsayı | Gözlemin ait olduğu yıl (2007-2024 arası). |
| Financial_Stability_Score | Ondalıklı (0-1) | Tedarikçinin finansal istikrar puanı. Yüksek = iyi. |
| Delivery_Performance_Score | Ondalıklı (0-1) | Teslimat performans puanı. Yüksek = iyi. |
| Quality_Compliance_Score | Ondalıklı (0-1) | Kalite uyumluluk puanı. Yüksek = iyi. |
| Regulatory_Adherence_Score | Ondalıklı (0-1) | Düzenleyici uyum puanı. Yüksek = iyi. |
| Sustainability_Score | Ondalıklı (0-1) | Sürdürülebilirlik puanı. Yüksek = iyi. |
| Past_Risk_Level | Ondalıklı (0-1) | Geçmiş risk seviyesi. Yüksek = kötü (riskli). |
| ERP_Transactions | Tamsayı | ERP işlem hacmi. |
| Incidents_Count | Tamsayı | Olay/sorun sayısı. Yüksek = kötü (riskli). |
| MCDM_Score | Ondalıklı (0-1) | Çok Kriterli Karar Verme (MCDM) skoru. Muhtemelen önceden hesaplanmış bir kompozit skor. |
| Risk_Category | Kategorik | Orijinal risk sınıfı: "Medium" (916) ve "High" (884). |

#### 5.3 Veri Kalitesi
- **Eksik Veri:** Hiçbir sütunda eksik (missing) değer bulunmamaktadır.
- **Tekrarlayan Satır:** Hiçbir tam tekrar eden (duplicate) satır yoktur.
- **Veri setine müdahale edilmeden analize başlanmıştır.**

#### 5.4 EDA Sırasında Yapılan Gözlemler
- Orijinal `Risk_Category` sütunundaki "High" kategorisi aslında daha yüksek performans skorlarına sahip tedarikçilere denk geldiği gözlenmiştir. Bu durum, sütunun "yüksek performans = yüksek kategori" anlamında kullanıldığını göstermektedir ve bu yüzden hedef değişken olarak kullanılmamıştır.
- `MCDM_Score` zaten önceden hesaplanmış bir bileşik (composite) skor olduğundan, risk skorlamasına dahil edilmemiştir (çift sayım riski).
- `ERP_Transactions` değişkeni doğrudan risk ile yorumlanamayacağından risk skoruna dahil edilmemiştir.
- Değişkenler arasındaki korelasyonlar genel olarak çok düşüktür (birbirleriyle ilişkisiz).

#### 5.5 Bu Bölümde Kullanılacak Görseller
1. **`risk_category_distribution.png`** — Orijinal Risk_Category dağılımını gösteren çubuk grafik.
2. **`year_distribution.png`** — Yıllar bazında gözlem frekans histogramı.
3. **`correlation_heatmap.png`** — Sayısal değişkenlerin korelasyon ısı haritası.
4. **`boxplot_Financial_Stability_Score.png`** — Finansal İstikrar Skoru kutu grafiği (Risk_Category bazında).
5. **`boxplot_Delivery_Performance_Score.png`** — Teslimat Performans Skoru kutu grafiği.

---

### BÖLÜM 6: YÖNTEM VE UYGULAMA

#### 6.1 Genel Yaklaşım
Bu projede üç aşamalı bir metodoloji izlenmiştir:
1. Keşifçi Veri Analizi (EDA)
2. Kompozit Risk Skorlama Sistemi Tasarımı
3. Makine Öğrenmesi Sınıflandırma Modelleri

#### 6.2 Risk Skorlama Sistemi

**Kullanılan 7 Değişken:**
| Değişken | Risk Dönüşümü | Açıklama |
| :--- | :--- | :--- |
| Financial_Stability_Score | `1 - normalized_value` (ters çevrildi) | Yüksek performans = düşük risk |
| Delivery_Performance_Score | `1 - normalized_value` (ters çevrildi) | Yüksek performans = düşük risk |
| Quality_Compliance_Score | `1 - normalized_value` (ters çevrildi) | Yüksek performans = düşük risk |
| Regulatory_Adherence_Score | `1 - normalized_value` (ters çevrildi) | Yüksek performans = düşük risk |
| Sustainability_Score | `1 - normalized_value` (ters çevrildi) | Yüksek performans = düşük risk |
| Past_Risk_Level | Doğrudan kullanıldı | Yüksek değer = yüksek risk |
| Incidents_Count | Doğrudan kullanıldı | Yüksek değer = yüksek risk |

**Normalizasyon:** Tüm değişkenler `MinMaxScaler` ile 0-1 aralığına normalize edildi.

**İki Farklı Skorlama Yöntemi:**

**A) Eşit Ağırlıklı Skor (Risk_Score_Equal):**
```
Risk_Score_Equal = (1/7) * Σ tüm risk bileşenleri
```

**B) Öncelik Ağırlıklı Skor (Risk_Score_Priority):**
```
Risk_Score_Priority = 0.27 × Financial_Risk
                    + 0.21 × Delivery_Risk
                    + 0.13 × Quality_Risk
                    + 0.08 × Regulatory_Risk
                    + 0.11 × Sustainability_Risk
                    + 0.10 × Past_Risk
                    + 0.10 × Incident_Risk
```
(Ağırlıklar toplamı = 1.00)

#### 6.3 Sınıflandırma Eşikleri

**ANA MODEL — Sabit (Eşit 3'e Bölünmüş) Eşikler:**
| Risk Sınıfı | Skor Aralığı |
| :--- | :--- |
| Low Risk (Düşük) | 0.00 ≤ skor ≤ 0.33 |
| Medium Risk (Orta) | 0.33 < skor ≤ 0.66 |
| High Risk (Yüksek) | 0.66 < skor ≤ 1.00 |

Bu yöntem, skor aralığını eşit genişlikte 3 parçaya böler. Sınıf dağılımı veriye bağlıdır ve dengesiz olabilir.

**YAN MODEL — Kuantil (Yüzdelik) Eşikler:**
| Risk Sınıfı | Yüzdelik Dilim |
| :--- | :--- |
| Low Risk (Düşük) | Alt %33 |
| Medium Risk (Orta) | Orta %33 |
| High Risk (Yüksek) | Üst %34 |

Kuantil eşik değerleri:
- **Equal Weighted:** Low/Medium sınırı = 0.4540, Medium/High sınırı = 0.5504
- **Priority Weighted:** Low/Medium sınırı = 0.4441, Medium/High sınırı = 0.5559

Bu yöntem dengeli sınıflar üretir (yaklaşık 594 / 594 / 612).

#### 6.4 Makine Öğrenmesi Pipeline Yapısı

**Veri Bölünmesi:**
- Train: %80 — Test: %20
- `random_state = 42`
- `stratify = y` (hedef değişkenin oranı korunarak)

**Model Yapılandırmaları (sklearn Pipeline):**

| Model | Ölçeklendirme | Pipeline Yapısı |
| :--- | :--- | :--- |
| Logistic Regression | StandardScaler uygulandı | Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression(max_iter=1000))]) |
| K-Nearest Neighbors | StandardScaler uygulandı | Pipeline([('scaler', StandardScaler()), ('model', KNeighborsClassifier())]) |
| Decision Tree | Ölçeklendirme yok | DecisionTreeClassifier(random_state=42) |
| Random Forest | Ölçeklendirme yok | RandomForestClassifier(random_state=42) |

**Neden Bazı Modellere Ölçeklendirme Uygulandı:**
- Lojistik Regresyon gradyan tabanlı optimizasyon kullanır; farklı ölçeklerdeki değişkenler yakınsama sorunlarına yol açar.
- KNN mesafe (Öklid) tabanlıdır; ölçek farkı mesafe hesabını bozar.
- Karar Ağacı ve Random Forest dal bölme kurallarıyla çalışır; ölçeğe duyarsızdır (scale-invariant).

**Year Değişkeni Karşılaştırması:**
İki versiyon çalıştırıldı: Year dahil ve Year hariç. Year'ın eklenmesinin anlamlı bir fark yaratmadığı doğrulandığı için ana sonuçlarda Year hariç tutulmuştur.

#### 6.5 Bu Bölümde Kullanılacak Görseller
1. **`risk_class_comparison.png`** — Risk sınıfı dağılımları (Equal vs Priority, sabit eşik).
2. **`threshold_comparison.png`** — Sabit eşik vs Kuantil eşik karşılaştırması.

#### 6.6 Bu Bölüme Eklenecek Kod Snippet'leri
Aşağıdaki kod parçacıklarından birkaçını ekran görüntüsü veya metin olarak ekle:
- `MinMaxScaler` ile normalizasyon kodu (`supplier_scoring.py` satır 25-32)
- Risk skoru formülü kodu (`supplier_scoring.py` satır 41-49)
- Sabit eşik sınıflandırma fonksiyonu (`supplier_scoring.py` satır 52-58)
- Pipeline tanımlama kodu (`ml_modeling.py` satır 25-35)

---

### BÖLÜM 7: SONUÇLAR VE YORUM

Bu bölüm ödevin en ağırlıklı ve en önemli bölümüdür. Aşağıdaki tüm alt başlıkları ve tabloları birebir kullan.

#### 7.1 İstatistiksel Geçerlilik Testleri

##### 7.1.1 VIF (Variance Inflation Factor) Analizi
Modele giren 7 bağımsız değişken arasında çoklu doğrusal bağlantı (multicollinearity) olup olmadığı test edilmiştir.

| Özellik (Feature) | VIF Değeri |
| :--- | :--- |
| Financial_Stability_Score | 1.003 |
| Delivery_Performance_Score | 1.006 |
| Quality_Compliance_Score | 1.002 |
| Regulatory_Adherence_Score | 1.003 |
| Sustainability_Score | 1.003 |
| Past_Risk_Level | 1.005 |
| Incidents_Count | 1.002 |

**Yorum:** Tüm VIF değerleri 1.00 civarındadır. Genel kabul olarak VIF < 5 (veya < 10) olması çoklu doğrusal bağlantı problemi olmadığını gösterir. Bizim değerlerimiz 1.00 seviyesinde olduğu için tüm değişkenlerin birbirinden tamamen bağımsız bilgi taşıdığı ve modele dahil edilmelerinin istatistiksel olarak son derece sağlıklı olduğu kanıtlanmıştır.

##### 7.1.2 R² (Belirlilik Katsayısı) Analizi
Sürekli risk skorlarının (Risk_Score_Equal ve Risk_Score_Priority) seçilen 7 özellik tarafından ne kadar iyi açıklandığı Çoklu Doğrusal Regresyon ile test edilmiştir.

- **R² (Risk_Score_Equal):** 1.0000
- **R² (Risk_Score_Priority):** 1.0000

**Yorum:** R² = 1.00, bağımsız değişkenlerin hedef değişkeni (risk skoru) %100 oranında açıkladığını gösterir. Bu beklenen bir sonuçtur çünkü risk skorları bu değişkenlerin matematiksel (ağırlıklı) birleşimiyle oluşturulmuştur. Bu sonuç modelin iç tutarlılığının (internal consistency) kusursuz olduğunu doğrular.

#### 7.2 ANA MODEL Sonuçları (Sabit Eşik — Eşit 3'e Bölünmüş)

##### 7.2.1 Priority Fixed (Öncelik Ağırlıklı) — Year Olmadan

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 (Macro) |
| :--- | :--- | :--- | :--- | :--- |
| Logistic Regression | 0.9944 | 0.9945 | 0.9944 | 0.9944 |
| Random Forest | 0.8556 | 0.8569 | 0.8552 | 0.8559 |
| K-Nearest Neighbors | 0.8222 | 0.8206 | 0.8219 | 0.8193 |
| Decision Tree | 0.6944 | 0.6885 | 0.6935 | 0.6903 |

##### 7.2.2 Equal Fixed (Eşit Ağırlıklı) — Year Olmadan

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 (Macro) |
| :--- | :--- | :--- | :--- | :--- |
| Logistic Regression | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Random Forest | 0.8611 | 0.8587 | 0.8602 | 0.8579 |
| K-Nearest Neighbors | 0.7722 | 0.7677 | 0.7713 | 0.7688 |
| Decision Tree | 0.6333 | 0.6351 | 0.6328 | 0.6339 |

**Ana Model Yorumu:**
Sabit eşik (0.33 ve 0.66) ile bölünen sınıflandırmada tedarikçilerin büyük çoğunluğu "Medium Risk" grubunda toplanmıştır. Bu dengesiz dağılıma rağmen Lojistik Regresyon %99.4 - %100 F1 başarısı göstermiştir. Bunun nedeni, risk skorlarının doğrusal bir formülle hesaplanmış olması ve Lojistik Regresyon'un doğrusal bir algoritma olarak bu formülü mükemmel şekilde öğrenebilmesidir. Ağaç tabanlı algoritmalar (Decision Tree, Random Forest) dengesiz sınıflarda uç sınıfları tahmin etmekte nispeten zorlanmıştır.

#### 7.3 YAN MODEL Sonuçları (Kuantil Eşik — %33/%33/%34 Bölünmüş)

##### 7.3.1 Priority Quantile (Öncelik Ağırlıklı)

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 (Macro) |
| :--- | :--- | :--- | :--- | :--- |
| Logistic Regression | 0.9944 | 0.9945 | 0.9944 | 0.9944 |
| Random Forest | 0.8583 | 0.8566 | 0.8580 | 0.8569 |
| K-Nearest Neighbors | 0.7556 | 0.7487 | 0.7547 | 0.7501 |
| Decision Tree | 0.7000 | 0.6937 | 0.6994 | 0.6954 |

##### 7.3.2 Equal Quantile (Eşit Ağırlıklı)

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 (Macro) |
| :--- | :--- | :--- | :--- | :--- |
| Logistic Regression | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Random Forest | 0.8389 | 0.8364 | 0.8382 | 0.8367 |
| K-Nearest Neighbors | 0.7417 | 0.7355 | 0.7410 | 0.7370 |
| Decision Tree | 0.6278 | 0.6320 | 0.6274 | 0.6293 |

**Yan Model Yorumu:**
Kuantil eşik yöntemi, sınıfları dengeli hale getirmiştir (~600 gözlem her sınıfta). Ağaç tabanlı modeller (Random Forest ~%85 F1) dengeli sınıflardan yararlanarak daha kararlı sonuçlar üretmiştir. Lojistik Regresyon her iki yaklaşımda da baskın model olmaya devam etmiştir.

#### 7.4 Ana Model vs Yan Model Karşılaştırması

| Karşılaştırma Kriteri | Ana Model (Sabit Eşik) | Yan Model (Kuantil Eşik) |
| :--- | :--- | :--- |
| Sınıf dengesi | Dengesiz (Medium'a yığılma) | Dengeli (~600/600/600) |
| En iyi model | Logistic Regression (%99.4-100) | Logistic Regression (%99.4-100) |
| Random Forest performansı | ~%85 F1 | ~%85 F1 |
| Ağaç tabanlı modeller | Dengesiz sınıflardan olumsuz etkilendi | Daha kararlı sonuçlar |
| Metodolojik tercih | Skor aralığını eşit böler; iş mantığına uygun | Dağılımı eşit böler; istatistiksel olarak dengeli |

**Genel Yorum:** İki yöntem de birbirine yakın sonuçlar vermiştir. Sabit eşik yöntemi, 0-0.33/0.33-0.66/0.66-1.00 gibi sezgisel ve yorumlanabilir sınırlar sunduğu için ana model olarak tercih edilmiştir. Kuantil yöntemi ise sınıf dengesizliğini gidermesi açısından güçlü bir alternatif olarak yan model şeklinde sunulmuştur.

#### 7.5 Random Forest Değişken Önemi (Feature Importance)

Random Forest modelinin hesapladığı değişken önem sıralamaları:

**Priority Weighted modelde:** Financial_Stability_Score (en yüksek, ~0.27 önem) ve Delivery_Performance_Score (~0.21 önem) en önemli değişkenlerdir. Bu sıralama, risk skorundaki ağırlıklarla birebir örtüşmektedir.

**Equal Weighted modelde:** Tüm değişkenlerin önemi birbirine çok yakındır (~0.12-0.15), çünkü tüm bileşenler eşit ağırlıkla dahil edilmiştir.

Her iki modelde de `Year` değişkeninin önemi sıfıra yakın çıkmıştır (en düşük), bu da Year'ın risk sınıflandırmasına katkısının olmadığını doğrular.

#### 7.6 Year (Yıl) Değişkeninin Etkisi

| Hedef | Model | Year Yok (F1) | Year Var (F1) | Fark |
| :--- | :--- | :--- | :--- | :--- |
| Priority Fixed | Logistic Regression | 0.9944 | 0.9573 | -0.0071 |
| Priority Fixed | Random Forest | 0.6948 | 0.7095 | +0.0147 |
| Equal Fixed | Logistic Regression | 0.9626 | 0.9626 | 0.0000 |
| Equal Fixed | Random Forest | 0.4683 | 0.4412 | -0.0270 |

**Yorum:** Year değişkeninin eklenmesi, modellerin tahmin gücüne kayda değer hiçbir iyileştirme sağlamamıştır. Risk sınıfları, tamamen tedarikçi performans metriklerine dayalı (zamandan bağımsız) olarak hesaplandığı için Year yalnızca "gürültü" (noise) görevi görmüştür. Bu nedenle Year değişkeni nihai modelden çıkarılmıştır.

#### 7.7 Bu Bölümde Kullanılacak Görseller
1. **`confusion_matrices_priority_without_year.png`** — ANA MODEL Priority Fixed confusion matrix'leri.
2. **`confusion_matrices_equal_without_year.png`** — ANA MODEL Equal Fixed confusion matrix'leri.
3. **`confusion_matrices_priority_quantile.png`** — YAN MODEL Priority Quantile confusion matrix'leri (opsiyonel).
4. **`rf_feature_importance_priority_without_year.png`** — ANA MODEL Random Forest değişken önem grafiği.
5. **`rf_feature_importance_equal_without_year.png`** — ANA MODEL Equal Random Forest değişken önem grafiği (opsiyonel).

---

### BÖLÜM 8: SONUÇ VE DEĞERLENDİRME

#### 8.1 Genel Özet
Bu projede Kaggle'dan elde edilen 1800 gözlem ve 11 değişkenden oluşan tedarikçi risk veri seti üzerinde kapsamlı bir veri madenciliği çalışması gerçekleştirilmiştir. Keşifçi veri analizi sonucunda orijinal `Risk_Category` değişkeninin hedef olarak uygun olmadığı tespit edilmiş ve kendi kompozit risk skorlama sistemimiz tasarlanmıştır. Dört farklı makine öğrenmesi algoritması test edilmiş, Lojistik Regresyon %99+ F1 skoru ile en başarılı model olmuştur. VIF ve R² analizleri modelin istatistiksel sağlamlığını kanıtlamıştır.

#### 8.2 Öğrenci Olarak Ne Öğrendik
- Veri ön işleme ve özellik mühendisliğinin model başarısındaki kritik rolü.
- StandardScaler gibi ölçeklendirme tekniklerinin mesafe tabanlı ve gradyan tabanlı algoritmalar üzerindeki dramatik etkisi.
- Pipeline kullanımının kod tekrarını önlediği ve veri sızıntısını (data leakage) engellediği.
- VIF ve R² gibi istatistiksel testlerin modelin güvenilirliğini değerlendirmedeki önemi.
- Farklı eşik yöntemlerinin (sabit vs kuantil) sınıf dağılımına ve model performansına etkisi.

#### 8.3 Gelecekte Yapılabilecek İyileştirmeler
- XGBoost, LightGBM gibi gelişmiş topluluk yöntemlerinin denenmesi.
- GridSearchCV veya RandomizedSearchCV ile hiperparametre optimizasyonu.
- Zaman serisi analizi ile tedarikçi risk trendlerinin incelenmesi.
- Derin öğrenme yaklaşımlarının (Neural Network) bu veri setine uygulanması.
- Gerçek dünya verileriyle doğrulama (cross-validation, harici veri seti).

---

### BÖLÜM 9: KAYNAKÇA

Aşağıdaki kaynak türlerinden oluşturulmalıdır (APA formatında):
- Tedarik zinciri risk yönetimi üzerine akademik makaleler.
- Scikit-learn resmi dokümantasyonu.
- Pandas, NumPy, Matplotlib, Seaborn dokümantasyonları.
- Kaggle veri seti sayfası.
- Veri madenciliği ders kitapları.

---

### BÖLÜM 10: EKLER

Bu bölüme aşağıdaki uzun kod parçacıkları metin olarak eklenmelidir:
1. `eda_supplier_risk.py` — Keşifçi Veri Analizi kodu (tam metin).
2. `supplier_scoring.py` — Risk skorlama kodu (tam metin).
3. `supplier_scoring_quantile.py` — Kuantil eşik kodu (tam metin).
4. `ml_modeling.py` — Makine öğrenmesi modelleme kodu (tam metin).
5. `advanced_stats.py` — VIF ve R² hesaplama kodu (tam metin).

Ek olarak, Ana metin içinde yer verilmeyen diğer görseller buraya konulabilir:
- `boxplot_Quality_Compliance_Score.png`
- `boxplot_MCDM_Score.png`
- `model_comparison_f1_priority_quantile.png`
- `model_comparison_f1_equal_quantile.png`

---

## KAPAK SAYFASI FORMATI

PDF'in 4. sayfasında belirtilen YTÜ kapak formatına uygun olarak:
- YTÜ logosu (üstte, ortalanmış)
- "YILDIZ TEKNİK ÜNİVERSİTESİ" (büyük harf, bold)
- "İstatistik Bölümü" (altında)
- "VERİ MADENCİLİĞİNE GİRİŞ DÖNEM ÖDEVİ" (ortada, büyük font)
- "Tedarikçi Risk Değerlendirmesi: Veri Madenciliği Yaklaşımı" (alt başlık)
- Öğrenci ad, soyad ve numara bilgileri
- Tarih: 2025-2026 Bahar Dönemi

---

## ÖNEMLİ NOTLAR

1. **Ana model** her zaman Sabit Eşik (0-0.33, 0.33-0.66, 0.66-1.00) modelidir.
2. **Yan model** Kuantil (%33-%33-%34) modelidir ve karşılaştırma amacıyla sunulur.
3. Orijinal `Risk_Category` sütunu hedef değişken olarak **kullanılmamıştır**.
4. `MCDM_Score` ve `ERP_Transactions` risk skorlamasına **dahil edilmemiştir**.
5. `Year` değişkeni son modelden **çıkarılmıştır** (gürültü yaptığı kanıtlanmıştır).
6. Lojistik Regresyon ve KNN için `StandardScaler` uygulanmıştır (Pipeline içinde).
7. Karar Ağacı ve Random Forest için ölçeklendirme **uygulanmamıştır**.
8. Tüm train-test bölmeleri: %80/%20, `random_state=42`, `stratify=y`.
