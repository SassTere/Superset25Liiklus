# Superset25Liiklus

Superseti ülevaade liiklusjuhtumitest.

# Sissejuhatus

Selles repositooriumis asuvad vajalikud failid ja juhend Superseti jooksutamiseks enda arvutis Docker image-ina.

Lisaks on kirjeledus liiklusjuhtumite algandmetest, nende töötlemise viisist ja laadimisest andmebaasi selleks, et neid laadida Superseti.

Kaasas on ka failid, mis võimaldavad andmebaasi laetud andmete põhjal kuvada Superseti autori poolt koostatud graafikud ja dashboardi.

# Kuidas alustada?

Esmalt veendu, et sul on installitud VS Code
https://code.visualstudio.com/

Selle projekti raames olid VS Code-i paigadatud järgmised laiendused:

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
