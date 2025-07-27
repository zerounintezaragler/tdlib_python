# Tdlib python

** Tdlib python ** 'n Biblioteek om BOT / USERBOT / enigiets wat verband hou met Telegram te maak

- 🇮🇩 [Indonesië] (./ readme.md)
- 🇺🇸 [Engels] (./ readme_en.md)
- 🇰🇷 [Korea, Republiek van Suid -Korea] (./ readme_ko.md)
- 🇨🇳 [China] (./ readme_zh-cn.md)
- 🇿🇦 [Suid -Afrika] (./ readme_af.md)
- 🇮🇳 [Indië] (./ readme_hi.md)
- 🇯🇵 [Japan] (./ readme_ja.md)
- 🇷🇺 [Rusland] (./ readme_ru.md)
- 🇹🇭 [Thailand] (./ readme_th.md)
- 🇦🇪 [Verenigde Arabiese Emirate] (./readme_ar.md)


## feit

- Hierdie biblioteek is nie gebind deur baie afhanklikhede nie 3

## funksie

- [x] ** baie vinnig ** ashnc -biblioteek
- [x] ** maklik om te gebruik **

## Voorbeeld

- [Eenvoudige voorbeeld] (https://github.com/zerounintezaragler/tdlib_python/tree/main/quickstart)



## Installeer

Voordat u installeer, moet u seker maak dat u die basiese python ten minste ken, u Ptyhon op u rekenaar / toestel geïnstalleer het. [Python webwerf] (https://www.python.org)

- ** Python **

  `` Bash
  PIP Installeer Tdlib-Python
  `` `

## dokumentasie

### Versekeryninaliseer

Die metode moet vrylik genoem word om na ** op ** / voor die metode ** op ** te wees, maar ek stel voor ** op **

** Voorbeeld: **

`` `Python
  Tdlibpythonzerounintezaragler.ensureInitialized (LibraryPath = "vurk/afhanklikhede/lib/libbtdlib_python.so")
`` `

### Initialiseer

Hierdie metode moet na die ** op ** -metode geroep word, want om opdaterings te verwerk

** Voorbeeld: **

`` `Python
  Wag op tdlibpythonzerounintezaragler.initialized ()
`` `

### aan

Hierdie metode is nuttig om data -opdaterings van oproepe / opdaterings te kry

** Voorbeeld: **

`` `Python

  def on_callback (opdatering: dict):
    Druk (opdatering)

  Tdlibpythonzerounintezaragler.on (event_name = "update", on_callback = on_callback)
  
`` `


### createclient

Om 'n nuwe kliënt te skep, maak seker dat u die metode noem.

** Voorbeeld: **

`` `Python
NewClientId = tdlibpythonzerounintezaragler.createclient ()
Druk (newClientId)
`` `


### Invok

Om die API te skakel, moet u die dokumentasie direk lees

- [URL Docs] (ander_url_docs) is maklik om vir die publiek te lees 

Hier bied ek slegs parameters datakaart, kaart / json Daar is verskeie belangrike sleutels


| Sleutel | Beskrywing | Waarde | Moet gevul word |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| **@tipe ** | Dit is gevul met die metode van | ** String ** | ** Ja ** |
| **@client_id ** | Dit bevat kliënt -ID vanaf die ** createClient ** -metode ** | ** int ** | ** As daar vir die sinkroniseringsmetode iets moet wees wat nie ** |
| **@ekstra ** | Vul die unieke ID in omdat die async -metode nie direk data teruggee nie, sodat dit ekstra nodig is as 'n sleutelopgawe -data | ** String ** | ** nee ** |


As ons die verpligte parameters gevul het, gaan ons voort hoe om die brand aan te roep

- ** setLogveribilityLevel **
  Omdat dit die log -metode is, gebruik u die sinkroniseringsmetode 
  en nie hoef te vul om die sleutel in te vul nie **@client_id **

  Voorbeeld: 


`` `Python
  Tdlibpythonzerounintezaragler.invokesync (parameters = {
    "@Type": "setLogverability",
    "New_veverbosity_level": 0,
  });
`` `

- ** sendMessage **
  Maak seker dat die kliënt aangemeld is om boodskappe met hierdie biblioteek te stuur
  [Verwysingsdokumentasie van SendMessage] (URL -dokumente)

`` `Python

        /// Neem vanaf CreateClient of Update
        client_id = 1;
        getMe = wag op tdlibpythonzerounintezaragler.invoke (parameters = {
          "@Type": "getMe",
          "@client_id": client_id,
        });
        druk (getMe);
        Wag op tdlibpythonzerounintezaragler.invoke (parameters = {{
          "@Type": "sendMessage",
          "@client_id": cliEnt_id,
          "chat_id": getMe ["id"],
          "Tipe": "teks",
          "Teks": "Hallo",
        });
`` `

Boonop is dit net 'n voorbeeld, om 'n ander metode te gebruik, moet u net die parametersdata invul, seker maak dat die sleutelparameters volgens die tabel gevul moet word, ek bedoel daar is 'n sleutel wat ingevul moet word, anders sal dit datasfoute stuur



## Help

** Moeilik **? Ek het ** biblioteek ** hierdie ** so goed as moontlik ** gebou en ** probeer maklik ** om te lees en ** so goed as moontlik gebruik **. 

As ** jy ** nog steeds ** voel ** ** Moeilikheid ** en ** Verwarring ** ** Probeer om aan te sluit ** tot ** Groep ** Ons in ** gratis sonder enige koste **

- [Telegram] (https://t.me/developer_global_public)

** Voordat u aansluit ** maak seker ** Gebruik profiel ** dat ** duidelik ** Ons gee nie om wie u is nie, en enige rang, maar ** Maak seker dat daar 'n gebruikersnaam en fotoprofiel is **, en probeer om ** in die groep te gesels ** ** Geen persoonlike klets ** want dit ** General Group en miskien is ander mense verward **. As ** nie volg nie **, is dit die moontlikheid ** kan nie toegang hê tot die klets in die groep nie en sal dit verbied word **, die oplossing om die tweede rekening te gebruik, want nadat ons verbied is, kan ons nie vinnig reageer nie


## Ondersteun my

As u voel dat hierdie program nuttig is, kan u my ondersteun [GitHub Zerounintezaragler] (https://github.com/zerounintezaragler) op die skakel is beskikbaar op sosiale media en my borge. Ek gee nie om as u net 'n bietjie geld volg / skenk nie

[] (https://github.com/zerounintezaragler/zerounintezaragler/blob/main/asses/gopay.png)

- https://github.com/sponsors/zerounintezaragler

Dankie


Zerounintezaragler-18-07-2025


## Tags

- Tdlib_python Python