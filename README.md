# Superset25Liiklus

Superseti ülevaade Liiklusjärelvalve käigus avastatud süütegudest.


![Image](https://github.com/user-attachments/assets/ed9109a6-861d-400b-8b4a-e84bd98eb608)


# Sissejuhatus

Selles repositooriumis asuvad vajalikud failid ja juhend Superseti jooksutamiseks enda arvutis Docker image-ina.

Lisaks on kirjeledus liiklusjuhtumite algandmetest, nende töötlemise viisist ja laadimisest andmebaasi selleks, et neid laadida Superseti.

Kaasas on ka failid, mis võimaldavad andmebaasi laetud andmete põhjal kuvada Superseti autori poolt koostatud graafikud ja dashboardi.

# Andmestik

Meie analüüs põhineb **Liiklusjärelevalve käigus avastatud süütegude** andmestikul.

Avaldatud süütegude andmete allikas on politsei menetlusinfosüsteem POLIS. Andmeid kasutades tuleb arvestada, et avaldatavad andmed lähtuvad operatiivtasandi andmebaasist, kuhu sisestatakse esmane registreerimist vajav informatsioon, mis võib edasise menetluse käigus täieneda ja muutuda.

- **Allikas:**  
  [Liiklusjärelevalve käigus avastatud süüteod - Politseitööga seotud avaandmed)](https://www.politsei.ee/et/juhend/politseitoeoega-seotud-avaandmed/liiklusjarelevalve-kaigus-avastatud-suuteod)  
  [Liiklusjärelevalve käigus avastatud süüteod CSV)](https://opendata.smit.ee/ppa/csv/liiklusjarelevalve_1.csv)   
- **Andmete kasutuslitsents:** Creative Commons 3.0  
- **Avaldatud:** vajab täpsustamist
- **Viimati uuendatud:** vajab täpsustamist
- **Kohalik koopia:** [`data/Liiklus.csv`](data/Liiklus.csv)  

## Andmeelemendid

| Avaldatava andmeelemendi nimetus         | Kirjeldus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JuhtumId**                             | Juhtumi unikaalne identifikaator. Väljastatavates andmetes võib ühe juhtumi kohta olla mitu kirjet, kui korraga on toime pandud mitu süütegu; sama JuhtumId väärtuse esinemine mitmes kirjes näitab, et need kirjed kuuluvad ühte juhtumisse (nt kiiruse ületamine + tehnonõuetele mittevastava sõiduki juhtimine).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **ToimKpv**                              | Süüteo toimepaneku kuupäev.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **ToimKell**                             | Süüteo toimepaneku kellaaeg.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **ToimNadalaPaev**                       | Süüteo toimepaneku nädalapäev.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **ToimLoppKpv**                          | Süüteo toimepaneku ajavahemiku lõpu kuupäev (kasutatakse varavastaste süütegude puhul, kui täpne kellaaeg on teadmata).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **ToimLoppKell**                         | Süüteo toimepaneku ajavahemiku lõpu kellaaeg (kasutatakse varavastaste süütegude puhul, kui täpne kellaaeg on teadmata).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **SyndmusLiik**                          | Toimunud sündmuse liik (avaldatavad koodide väärtused on dokumendi lõpus).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **SyndmusTaiendavStatLiik**              | Toimunud sündmuse täiendav statistiline liik (avaldatavad koodide väärtused on dokumendi lõpus); ei ole kohustuslik väärtegude puhul.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **SissetungimiseLiik**                    | Sissetungimise meetodi liik (avaldatavad koodide väärtused on dokumendi lõpus); ei ole kohustuslik väärtegude puhul.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Valve**                                | Toimepanemise koha/varastatud sõiduki valve liik (avaldatavad koodide väärtused on dokumendi lõpus); ei ole kohustuslik väärtegude puhul.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Seadus**                               | Seaduse nimetus, mille alusel on süütegu kvalifitseeritud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Paragrahv**                            | Paragrahvi number, mille alusel on süütegu kvalifitseeritud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **ParagrahvTais**                        | Paragrahvi tekst, mille alusel on süütegu kvalifitseeritud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Loige**                                | Lõike number, mille alusel on süütegu kvalifitseeritud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Punkt**                                | Punkti number, mille alusel on süütegu kvalifitseeritud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **RikutudOigusnorm**                     | Rikutud õigusnorm, mis täpsustab rikkumise sisu (kasutatakse väärtegude korral).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Kahjusumma**                           | Süüteoga põhjustatud kahju suurus eurodes; esitatakse vahemikena 0–499, 500–4 999, 5 000–49 999 ja 50 000+.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **KohtLiik**                             | Toimepaneku koha liik (avaldatavad koodide väärtused on dokumendi lõpus).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **MaakondNimetus**                       | Toimepaneku koha maakonna nimetus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **ValdLinnNimetus**                      | Toimepaneku koha kohaliku omavalitsusüksuse (valla või linna) nimetus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **KohtNimetus**                          | Toimepaneku koha asustusüksuse (küla, alevik, alev, linnaosa) nimetus; avaldatakse nimetused olukorras, mis kehtis süüteo toimepaneku ajal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **MntVoiTanav**                          | Näitab, kas koht on määratud maantee nimetusega ja kilomeetriga (MNT) või tänava nimetusega (TNV).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **MntTanavNimetus**                      | Toimepaneku koha maantee või tänava nimetus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **KM**                                   | Toimepaneku koha maantee kilomeeter (KM).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Lest_X**                               | Toimepaneku koha X-koordinaat L-EST koordinaatsüsteemis; esitatakse üldistatult vahemikena (500 m või 1 000 m ruutudena sõltuvalt andmehulgast ja asustusüksusest).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Lest_Y**                               | Toimepaneku koha Y-koordinaat L-EST koordinaatsüsteemis; esitatakse üldistatult vahemikena (500 m või 1 000 m ruutudena sõltuvalt andmehulgast ja asustusüksusest).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **SoidukLiik**                           | Sõiduki liik liiklusjärelevalve rikkumise korral või varastatud mootorsõiduki liik varavastase süüteo korral (avaldatavad koodide väärtused on dokumendi lõpus); varguse puhul iga sõiduki kohta eraldi kirje, kahjusumma esitatakse ühes kirjes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **SoidukRegRiik**                        | Sõiduki registreerimise riik liiklusjärelevalve rikkumise või varavastase süüteo korral (EST või MUU).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **SoidukMark**                           | Sõiduki mark liiklusjärelevalve rikkumise või varavastase süüteo korral; esitatakse, kui liiklusregistris on vähemalt 100 sama marki sõidukit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **SoidukVlAasta**                        | Sõiduki väljalaske aasta liiklusjärelevalve rikkumise või varavastase süüteo korral; esitatakse, kui registris ≥ 100 sama marki sõidukit või kui vanus ≥ 40 aastat (siis näidatakse “VANA”).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **RikkujaSugu**                          | Süüteo toimepanija sugu (M või N).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **RikkujaVanus**                         | Süüteo toimepanija vanus toimepaneku ajal; esitatakse vahemikena 0–12, 13–15, 16–17, 18–25, 26–34, 35–44, 45–54, 55–64 ja 65+.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **RikkujaElukoht**                       | Süüteo toimepanija elukoha riik (EST või MUU).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **SyyteoLiik**                           | Näitab, kas süütegu on väärtegu (VT) või kuritegu (KT).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |




# Andmete puhastamine

## Tööriist: [OpenRefine](https://openrefine.org/)  

## “SoidukMark” välja klasterdamine OpenRefine’iga

![Image](https://github.com/user-attachments/assets/7aa3e16c-5896-42de-b058-2655fbd987ee)

Selleks, et välja **SoidukMark** väärtused (nt “Ford”, “Mercedes-Benz” jmt) muuta ühtlaseks ja kõrvaldada kirjavead (näiteks `Fprd`, `Mersedes Bens` jms), kasutasime OpenRefine’i **Cluster & Edit** funktsionaalsust:

1. Imporditud andmestikus valida veerg **SoidukMark**.
2. Menüüs **Edit cells → Cluster and edit…** valida esmalt meetod **Key collision** (Fingerprint), millega leitakse peamised kirjaviisierinevused.
3. Läbi automaatselt grupitud klastrid: ühenda näiteks `Fprd`, `Ford` ja `Ford’ina` kõik ühise stiili **Ford** alla.
4. Vajadusel vaheta meetodit **Nearest neighbor** (Levenshtein) klastrite leidmiseks detailsemate variatsioonide puhul.
5. Pärast klasterdamist ja valideerimist salvesta muudetud andmed, kus iga sõidukimarki esineb nüüd korrektselt ja ühe kordusena.

--

## Maakondade eraldamine ja kuvamine Superset’is

Supersetis on võimalik visualiseerimisel eraldada ja kuvada Eesti maakondi, mille puhul on vaja leida nimi → kood vaste. Selleks kasuta **Data → Reconcile** funktsionaalsust, mis sidus maakondade nimed vastavate ISO 3166-2 koodidega.

| Maakond      | ISO 3166-2 kood |
|--------------|-----------------|
| Harjumaa     | EE-37           |
| Hiiumaa      | EE-39           |
| Ida-Virumaa  | EE-45           |
| Jõgevamaa    | EE-50           |
| Järvamaa     | EE-52           |
| Läänemaa     | EE-56           |
| Lääne-Virumaa| EE-60           |
| Põlvamaa     | EE-64           |
| Pärnumaa     | EE-68           |
| Raplamaa     | EE-71           |
| Saaremaa     | EE-74           |
| Tartumaa     | EE-79           |
| Valgamaa     | EE-81           |
| Viljandimaa  | EE-84           |
| Võrumaa      | EE-87           | 

--

## Export

Korrastatud andmed expordi xlsx failiks ja seejärl tee esimased katsetused andmete visualiseerimisega Excelis.

Superset ei toeta otse XLSX-faile kui andmeallikat, seega tuleb Excel-tabel esmalt teisendada sobivasse, veerupõhisesse andmeformaati. Selleks on hea kasutada Parquet-vormingut, sest:

- **Veerupõhine (columnar) salvestus**  
  Parquet salvestab andmed veergude kaupa, mis tähendab, et Superset saab päringuid teha ainult vajalike veergude peal, ilma kogu faili lugemata. See vähendab oluliselt I/O-koormust ja kiirendab visualiseerimisi.

- **Tõhus andmekompressioon ja väiksem kettakasutus**  
  Parquet kasutab efektiivseid kompressiooniskeeme (nt Snappy), mis tähendab, et sama andmemahu puhul kulub ketta- ja mäluruumi märgatavalt vähem kui XLSX- või CSV-faili puhul.

- **Täpne skeemi ja tüüpide informatsioon**  
  Parquet formaat salvestab veergude andmetüübid (nt integer, float, timestamp) koos metaandmetega. Superset saab selle abil õieti tuvastada mõõdikud ja dimensioonid ning rakendada filtreid ja agregatsioone veatult.

- **Suuremahuliste andmete käsitlemine**  
  Kui Excel-failid kasvavad kümne- või sadatuhandetes ridadesse, muutub nende laadimine ja päringute tegemine aeglaseks. Parquet võimaldab tööd teha ka miljonite ridadega, säilitades samal ajal jõudluse.

- **Lihtne integreerimine Hadoop/Spark ökosüsteemiga**  
  Kui tulevikus on plaanis kasutada suuremat andmeplatvormi (nt Apache Spark), on Parquet-vorming standardne ja laialt toetatud, lihtsustades andmete edasist töötlemist ja laadimist Superseti taha.

**Näide konverteerimisest Pythonis**  
```python
import pandas as pd

# 1) Lae Excel andmed
df = pd.read_excel('andmed.xlsx')

# 2) Salvesta Parquet'na
df.to_parquet('andmed.parquet', compression='snappy')
```
--

# Kuidas alustada?

Esmalt veendu, et sul on installitud VS Code
https://code.visualstudio.com/

Selle projekti raames on VS Code-i paigadatud järgmised laiendused:

Võimaldab sirvida ja hallata SSH-, WSL- ja Dev Container-sihtkohti otse VS Code’i külgribal.  
```bash
- `ms-vscode.remote-explorer-0.5.0@0.5.0`
```
 Lubab vaadata ja redigeerida Git-hoidlaid ilma neid lokaalselt kloonimata.
```bash
- `ms-vscode.remote-repositories-0.42.0@0.42.0`
```
 Võimaldab arendada ja käivitada projektikoodi Docker-põhistes Dev Containerites.
 ```bash
- `ms-vscode-remote.remote-containers-0.413.0@0.413.0`
```
 Pakub VS Code’is integreeritud tööriistu Docker-image'ite, konteinerite ja registrite haldamiseks. 
 ```bash
- `docker.docker-0.7.0-darwin-arm64@0.7.0`
```


## Projekti kloonimine ja avamine VS Code’is

1. Ava **VS Code**.  
2. Klõpsa vasakul küljeribal **Source Control** (Git-ikoon).  
3. Vajuta üleval **Clone Repository** (või **Clone Git Repository**) nuppu.  
4. Kleebi URL: https://github.com/SassTere/Superset25Liiklus.git
ja vajuta **Enter**.  
5. Vali dialoogis kaust, kuhu soovid salvestada, ja klõpsa **Select Repository Location**.  
6. Kui kloonimine on lõppenud, vali **Open** või **Open in Current Window**, et projekt VS Code’i aknas avada.

## Apache Superseti paigaldamine
Apache Superset on mugav vabavaraline tööriist andmete analüüsiks visualiseermiseks.  
[Täpsem juhend Superseti'i seadistamiseks)](https://github.com/SassTere/Superset25Liiklus/blob/main/superset_build/README.md)  

### Apache Superseti image’i tõmbimine Docker Hub’ist

1. Veendu, et Docker on sinu süsteemis installitud ja käivitunud.  
2. Ava terminal või käsurida.  
3. Tõmba ametlik Superseti image:
   ```bash
   docker pull apache/superset:latest
   ```

### Docker Desktop GUI abil Superseti image’i tõmbimine

1. Ava **Docker Desktop** rakendus.  
2. Vali vasakul menüüst **Docker Hub**.  
3. sisesta otsingusse **Apache Superset**.  
4. Vali esimene valik nimega apache/superset.  
5. Klõpsa paremas ülanurgas **Pull** nupule.

## Kahe uue Docker-konteineri loomine

Seame üles:
1. Superset’i konteiner, kus on mount’itud meie projekt (`Superset25Liiklus`).
2. Python’i arendus­konteiner, kus on samuti mount’itud meie projekt.




### Arenduskeskkonna käivitamine

cmd+shift+p
Dev Containers:
Rebuild and Reopen in Container

Dockeris on nähtav uus Container 

Alternatiivina kasuta:
### Arenduskeskkonna loomine
Kasuta klahvikombinatsiooni cmd+shift+p
kirjuta dev containers 
Vali add configuration to workspace
debian
bullseye
python devcontainers > OK
keep defaults

Open in container

Dockeris on nähtav uus Container 


### Superset’i konteineri seadistamine

Täpsed juhised Superseti jooksutamiseks asuvad superset_build README failis.










