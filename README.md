Home first aid kit control
=============
Application to control the expiration date of medicines in the first aid kit


docs
-------
https://честныйзнак.рф/upload/iblock/a40/PP-RF-ot-14.12.2018-_-1556-s-uchyetom-izmeneniy-1118_1.pdf

https://forum.mista.ru/topic.php?id=847308#22


    Стандарт данных маркировки (для вторичной упаковки) теперь такой:

    00<GTIN>21<SERIAL><FNC1>91<KeyID><FNC1>99<SIGN>


    где <GTIN> - 14-разрядный код GTIN

    <SERIAL> - серийный номер вторичной упаковки, 13 символов (это в документации, но производители могут это трактовать как от 1 до 13 символов, т.к. эта группа данных должна заканчиваться разделителем групп <FNC1> кодом символа 29)

    <KeyID> - 4-разрядный идентификатор ключа

    <SIGN> - 44-разрядная подпись (ранее была 88 разрядная)"


    Во, вроде разобрался как на одной из упаковок закодирован КиЗ!
    Другое дело все равно пока не ясно, правильная ли это кодировка для целей МДЛП.

    Исходный код:
    01189011480060481721120010B90020621B2ALQQWWCJF3

    Расшифровка:

    (01)18901148006048(17)211200(10)B900206(21)B2ALQQWWCJF3

    18901148006048 - это джитин (притом контрольный разряд здесь верный)

    211200 - срок годности 12.21
    B900206 - номер серии (партии)
    B2ALQQWWCJF3 - серийный номер упаковки

    Криптохвоста правда здесь нет..

API
--------------
Документация по API: https://апи.национальный-каталог.рф/

* для получения продукта https://апи.национальный-каталог.рф/v3/product?apikey=l10k3203w65mbngr&gtin=<gtin>

Mobile check
-------

Req:

    POST /mobile/check? HTTP/1.1
    Host: mobile.api.crpt.ru
    Content-Type: application/json
    client: iOS 14.4; AppVersion: 4.6.1; Device: iPhone X
    Connection: keep-alive
    Accept: application/json
    User-Agent: User-Agent: Platform: iOS 14.4; Device: iPhone X
    Accept-Language: ru-RU;q=1.0, en-RU;q=0.9
    Accept-Encoding: gzip;q=1.0, compress;q=0.5
    Content-Length: 162

    {"cis":"0108000036012000215884486546653\u001d91EE06\u001d92QKT9vdPhgmoRg6GAKmYgpMiP6X8HYolEeukFLhrQBfo=","sid":"","codeType":"datamatrix","isGs1DataCarrier":true}

Res:

    {"id":59227842,"codeFounded":true,"checkResult":true,"cis":"0108000036012000215884486546653\u001D91EE06\u001D92QKT9vdPhgmoRg6GAKmYgpMiP6X8HYolEeukFLhrQBfo=","code":"0108000036012000215884486546653\u001D91EE06\u001D92QKT9vdPhgmoRg6GAKmYgpMiP6X8HYolEeukFLhrQBfo=","checkDate":1614544748647,"category":"drugs","productName":"Тантум верде форте","producerName":"Азиенде Кимике Риуните Анжелини Франческо А.К.Р.А.Ф. С.п.А., Италия","ownerName":"Закрытое акционерное общество фирма \"Центр внедрения \"ПРОТЕК\"","status":"goods_in_sale","expDate":"2024-09-30T00:00:00.000Z","operationDate":1607703269000,"batch":"0384","inn":"7724053916","statusNumber":"11","warningFlag":true,"warning":"ok","drugsData":{"prodDescLabel":"Тантум верде форте","packingName":"Азиенде Кимике Риуните Анжелини Франческо А.К.Р.А.Ф. С.п.А., Италия","batch":"0384","expirationDate":"2024-09-30T00:00:00.000Z","status":"in_circulation","lastOperationDate":1607703269000,"ownerInn":"7724053916","ownerName":"Закрытое акционерное общество фирма \"Центр внедрения \"ПРОТЕК\"","ownerAddress":"с Тарасовка, ул Большая Тарасовская, Владение 1, Сооружение 1","sourceType":1,"utilizationOpDate":1603998567000,"emissionOperationDate":1601297007000,"containsVzn":false,"gtin":"08000036012000","sgtin":"080000360120005884486546653","productProperty":{"byOfd":false,"hasOfdPrice":false},"signVetal":"0","releaseDate":1606385113000,"foiv":{"prodFormNormName":"СПРЕЙ ДЛЯ МЕСТНОГО ПРИМЕНЕНИЯ ДОЗИРОВАННЫЙ","prodDNormName":"0.51 мг/доза","prodPack1Name":"ФЛАКОН","prodPack12":"1","prodPack1Size":"1","completeness":"~","glfName":"АЗИЕНДЕ КИМИКЕ РИУНИТЕ АНЖЕЛИНИ ФРАНЧЕСКО А.К.Р.А.Ф. С.П.А.","glfCountry":"ИТАЛИЯ","regHolder":"АЗИЕНДЕ КИМИКЕ РИУНИТЕ АНЖЕЛИНИ ФРАНЧЕСКО А.К.Р.А.Ф. С.П.А.","regNumber":"ЛСР-002911/10","regDate":1270598400000,"prodNormName":"БЕНЗИДАМИН"}}}

CURL:

    curl 'https://mobile.api.crpt.ru/mobile/check?' \
    -X POST \
    -H 'Content-Type: application/json' \
    -H 'Accept-Language: ru-RU;q=1.0, en-RU;q=0.9' \
    -H 'client: iOS 14.4; AppVersion: 4.6.1; Device: iPhone X' \
    -H 'Accept: application/json' \
    -H 'Content-Length: 162' \
    -H 'User-Agent: User-Agent: Platform: iOS 14.4; Device: iPhone X' \
    -H 'Connection: keep-alive' \
    -H 'Host: mobile.api.crpt.ru' \
    --proxy http://localhost:9090 \
    -d '{"cis":"0108000036012000215884486546653\u001d91EE06\u001d92QKT9vdPhgmoRg6GAKmYgpMiP6X8HYolEeukFLhrQBfo=","sid":"","codeType":"datamatrix","isGs1DataCarrier":true}'