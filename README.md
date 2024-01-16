# KSY_semestralka

## Natrénujte si neuronovou síť, která rozpozná vaše vlastní písmo od cizího

Grafognózie (písmoznalectví) je vědní obor zabývající se identifikací pisatele na základě písma. Natrénujte neuronovou síť (nebo dotrénujte již předtrénovanou), která dokáže rozlišit vaše vlastní písmo od cizího (tedy binární klasifikátor: vaše/cizí). Přesnost sítě ověřte na testovacích datech (která neviděla během trénovaní).  Kolik trénovacích dat nejméně vaše síť potřebuje? Jak se podle vás liší mechanismus, který síť používá, od metod obecně používaných v písmoznalectví?

## Potřebné Python knihovny

```python
jupyter notebook
numpy
torch
torchvision
matplotlib 
```

## Spuštění trénovaní písmen

V souboru handwritting_recog_letters.ipynb postupně evaluuovat jednotlivé buňky. Je nutné mít uložený dataset ve složce dataset_letters, která má 2 podložky train a test. Train obsahuje složky 0 a 1, které obsahují obrázky písmen velikosti **28x28 pixelů**. Složka 0 je pro cizí písmena a složka 1 pro vlastní písmena. Test složka je pro testování sítě a má stejnou strukturu jako složka train.
Výsledek učení je vykreslen v poslední buňce.
Výstupem je slovník pro Neuronoou síť, který je uložen do souboru binary_classifier_cnn_letters.pth

## Spuštění trénovaní slov

V souboru handwritting_recog_words.ipynb postupně evaluuovat jednotlivé buňky. Je nutné mít uložený dataset ve složce dataset_letters, která má 2 podložky train a test. Train obsahuje složky 0 a 1, které obsahují obrázky písmen velikosti **475x100 pixelů**. Složka 0 je pro cizí písmena a složka 1 pro vlastní písmena. Test složka je pro testování sítě a má stejnou strukturu jako složka train.
Výsledek učení je vykreslen v poslední buňce.
Výstupem je slovník pro Neuronoou síť, který je uložen do souboru binary_classifier_cnn_words.pth

## Demo

Ve složce demo jsou 2 Jupiter notebooky pro rozpoznávání písmen a slov.
Pro spuštění dema je nutné mít soubor s natrénovanou sítí. Pro rozpoznávání písmet to je binary_classifier_cnn_letters.pth a pro rozpoznávání slov to je binary_classifier_cnn_words.pth. Soubory musí být ve stejné složce jako obrázky na rozpoznání, musí být ve formátu .png a musí mít velikost **28x28 pixelů** pro písmena a **475x100 pixelů** pro slova. V poslední buňce je možné změnit obrázek, který se má rozpoznat nebo slovník Neuronové sítě, který se má použít. Výstupem je text, který říká, jestli je obrázek vlastní nebo cizí.
