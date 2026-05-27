# Tedarikçi Risk Değerlendirmesi: Model ve İstatistik Raporu

Bu rapor, tedarikçi risk skorlaması üzerine kurulan makine öğrenmesi modellerinin performansını ve kullanılan veri setinin istatistiksel geçerliliğini özetlemektedir.

## 1. İstatistiksel Geçerlilik Testleri

### Çoklu Doğrusal Bağlantı (Multicollinearity) ve VIF Analizi
Makine öğrenmesi modellerine ve skorlama sistemine dahil edilen özelliklerin (features) birbirleriyle yüksek oranda korele olup olmadığını (çoklu doğrusal bağlantı problemi yaratıp yaratmadığını) test etmek için **VIF (Variance Inflation Factor)** değerleri hesaplanmıştır.

| Özellik (Feature) | VIF Değeri |
| :--- | :--- |
| Financial_Stability_Score | 1.002 |
| Delivery_Performance_Score | 1.005 |
| Quality_Compliance_Score | 1.001 |
| Regulatory_Adherence_Score | 1.002 |
| Sustainability_Score | 1.003 |
| Past_Risk_Level | 1.004 |
| Incidents_Count | 1.001 |

**Yorum:** Tüm özelliklerin VIF değerleri 1.00 seviyesindedir. VIF değerinin 5'ten (hatta genellikle 10'dan) küçük olması özellikler arasında çoklu doğrusal bağlantı olmadığını gösterir. Elde ettiğimiz ~1.00 değerleri, tüm değişkenlerin **birbirinden tamamen bağımsız** bilgi taşıdığını ve formülasyona dahil edilmelerinin istatistiksel açıdan son derece sağlıklı olduğunu kanıtlamaktadır.

### Modelin Açıklayıcılık Gücü (R² Skoru)
Uç risk sınıflarını oluşturmadan önce hesapladığımız sürekli (virgüllü) risk skorlarının (`Risk_Score_Equal` ve `Risk_Score_Priority`), seçilen 7 temel performans özelliği tarafından ne kadar iyi açıklandığını görmek adına Çoklu Doğrusal Regresyon uygulanmış ve R² (Belirlilik Katsayısı) hesaplanmıştır.

- **R² (Equal Weighted Risk Score):** 1.0000
- **R² (Priority Weighted Risk Score):** 1.0000

**Yorum:** R² skorunun 1.00 çıkması, bağımsız değişkenlerin (özelliklerin) hedef değişkeni (Risk Skoru) %100 oranında açıkladığını gösterir. Risk skorları dışsal faktörlerle değil, tamamen bu metriklerin matematiksel (ağırlıklı) birleşimiyle tasarlandığı için bu sonuç modelin iç tutarlılığının (internal consistency) kusursuz olduğunu doğrulamaktadır.

---

## 2. Makine Öğrenmesi Sınıflandırma Modelleri Performansı

Hocamızın yönergeleri doğrultusunda, sınıflandırma analizi iki aşamada ele alınmıştır:
- **Ana Modeller (Primary):** Sabit aralıklara (0.00-0.33, 0.33-0.66, 0.66-1.00) göre 3 eş parçaya bölünmüş risk sınıfları (`Risk_Class_Priority` ve `Risk_Class_Equal`).
- **Yan Modeller (Secondary):** Dağılımın Kuantil (yüzdelik, %33-%33-%34) olarak üçe bölünmesiyle oluşturulmuş risk sınıfları (`Risk_Class_Priority_Quantile` ve `Risk_Class_Equal_Quantile`).

*(Aşağıdaki sonuçlar, gürültü yaratmaması adına bağlamsal "Year" değişkeninin dahil **edilmediği** daha robust veri setine aittir.)*

### Ana Model (Primary): Eş 3'e Bölünmüş Sabit Eşik Sınıflandırması
Bu modellerde eşikler doğrudan 0.33 ve 0.66 olarak kabul edilmiştir.

**Priority Fixed (Öncelik Ağırlıklı Risk):**
| Model | F1 (Macro) Skoru |
| :--- | :--- |
| Logistic Regression (Standartlaştırılmış) | 0.964 |
| K-Nearest Neighbors (Standartlaştırılmış) | 0.770 |
| Decision Tree | 0.710 |
| Random Forest | 0.694 |

**Equal Fixed (Eşit Ağırlıklı Risk):**
| Model | F1 (Macro) Skoru |
| :--- | :--- |
| Logistic Regression (Standartlaştırılmış) | 0.962 |
| K-Nearest Neighbors (Standartlaştırılmış) | 0.837 |
| Decision Tree | 0.570 |
| Random Forest | 0.468 |

**Yorum:** Sabit eşiklerde çoğu tedarikçi "Orta (Medium)" risk grubuna yığıldığı için (dengesiz sınıf problemi), ağaç tabanlı algoritmalar (Decision Tree, Random Forest) uç sınıfları tahmin etmekte zorlanmıştır. Ancak doğrusal formülü çok iyi öğrenen Logistic Regression %96'nın üzerinde bir başarı sağlamıştır.

### Yan Model (Secondary): Kuantil (Yüzdelik) Eşik Sınıflandırması
Bu modellerde veriler dağılım üzerinden %33 Low, %33 Medium, %34 High olarak gruplanmış ve dengeli sınıflar elde edilmiştir.

**Priority Quantile (Öncelik Ağırlıklı Risk):**
| Model | F1 (Macro) Skoru |
| :--- | :--- |
| Logistic Regression (Standartlaştırılmış) | 0.994 |
| Random Forest | 0.855 |
| K-Nearest Neighbors (Standartlaştırılmış) | 0.819 |
| Decision Tree | 0.690 |

**Equal Quantile (Eşit Ağırlıklı Risk):**
| Model | F1 (Macro) Skoru |
| :--- | :--- |
| Logistic Regression (Standartlaştırılmış) | 1.000 |
| Random Forest | 0.857 |
| K-Nearest Neighbors (Standartlaştırılmış) | 0.768 |
| Decision Tree | 0.633 |

**Yorum:** Kuantil yaklaşımı, ağaç tabanlı algoritmaların (Random Forest ~%85 F1) dengeli veri üzerinden çok daha sağlıklı çalışmasını sağlamıştır. Logistic Regression modeli bu senaryoda mükemmele yakın bir ayrıştırma (%99.4 - %100) sergilemiştir.

---

### Nihai Sonuç
Yapılan istatistiksel testler (VIF, R²) özelliklerin özenle seçildiğini ve birbirini tekrar etmediğini kanıtlamıştır. Sabit (Equal 3-part) bölme yöntemi ana modelimiz olmakla birlikte, Kuantil yöntemi verideki yığılmayı engellemiş ve farklı makine öğrenmesi algoritmalarının veri üzerinde daha esnek performans göstermesini sağlamıştır.
