1.
Vad gör FastAPI? FastAPI är ett ramverk som används för att skapa APIer, i analogi med en bro mellan två system som används för att överföra data.
Vad gör Pydantic? Pydantic är en komponent av FastAPI och dess främsta syfte är typvalidering, en bekräftelse att en variabels värde är av rätt datatyp i den kontexten.
Vad gör psycopg3? Psycopg3 är en populär modul som fungerar som en adapter mellan python-skript och postgreSQL.
Var 'försvinner' datan mellan request och databas? Som frågan antyder försvinner datan inte riktigt, utan den blir exempelvis omvandlad alternativt dold internt.

2.
Vad betyder “Allt eller inget”, vad tror du? I denna kontext kan det syfta på att en exekvering antingen genomförs helt korrekt eller har ingen effekt överhuvudtaget.
transaction() eller commit()? transaction() kan anses viktigare för att det är en avskärmd och skyddad 'arbetsyta', medan commit() kunggör förändringarna.

3.
Vad är ett Python-objekt? Det är en instans som skapats från en pythonklass, vilket är ett slags ramverk.
Vad förstår PostgreSQL? PostgreSQL kan likna SQL på vissa sätt, medan PostgreSQL även förstår data i JSON-format.
Varför måste vi “översätta” data? Data översätts för att den förekommer i olika format, vilket gör det nödvändigt att ändra den så att den kan förstås på många olika platser innuti ens lokala maskin, eller på webben.

4.
När är JSONB bra? Eftersom JSONB lagras i binärt format ger det mer flexibilitet, vilket kan vara fördelaktigt i vissa fall
När är kolumner bättre? Kolumner, i kontexten av relationsdatabaser, kan vara bättre när man vill ha datan strukturerad på ett visst sätt, om man exempelvis vill göra JOINS, et cetera.
Varför har vi “raw tables”? Ibland kan det finnas ett värde i att tabeller mottar data utan att förändra den på något sätt.

