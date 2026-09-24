import os, subprocess
items=[
('skane','Skåne','I Skåne säger vi gärna att vädret kan växla snabbt. Här finns en tydlig sydsvensk klang, och många ord får en egen melodi.'),
('blekinge','Blekinge','I Blekinge möts kustlandskap och sydsvenska mål. Lyssna efter den mjuka rytmen när meningen rullar fram.'),
('sodra-halland','Södra Halland','I södra Halland hörs drag från både väst och syd. Det gör att uttal och melodi kan låta lite olika från by till by.'),
('sodra-smaland','Södra Småland','I södra Småland finns en tydlig sydsvensk ton. Orden får ofta en lugn rytm som skiljer sig från andra delar av landet.'),
('bohuslan','Bohuslän','I Bohuslän hörs en västsvensk melodi. Föreställ dig havet, klipporna och små kustsamhällen när du lyssnar på klippet.'),
('dalsland','Dalsland','Dalsländska mål hör hemma i västra Sverige. Uttalet kan variera mycket, men melodin har ofta en tydlig västlig karaktär.'),
('goteborg','Göteborg','Göteborg har ett välkänt västsvenskt uttal. Stadens språk påverkas också av många olika människor och områden.'),
('norra-halland','Norra Halland','I norra Halland möts västsvenska och sydsvenska språkdrag. Det gör området extra intressant att jämföra med grannarna.'),
('norra-smaland','Norra Småland','Norra Småland ligger mellan flera stora dialektområden. Därför kan uttalet visa drag från både öst och väst.'),
('varmland','Värmland','Värmländska mål är kända för sin tydliga språkmelodi. Här hörs ett västligt drag som kan skilja sig från grannlandskapen.'),
('vastergotland','Västergötland','I Västergötland finns flera västsvenska dialekter. Lyssna efter rytmen och jämför den med Göteborg och Värmland.'),
('gotland','Gotländska mål','Gotländska mål har en speciell klang som har utvecklats på ön. Jämför melodin med dialekter på det svenska fastlandet.'),
('halsingland','Hälsingland','I Hälsingland finns norrländska språkdrag. Landskapet har många lokala variationer, så uttalet kan skifta mellan olika platser.'),
('harjedalen','Härjedalen','Härjedalen ligger i fjällnära Sverige. Dialekterna där har norrländska drag och har påverkats av landskapets långa avstånd.'),
('jamtland','Jämtland','Jämtländska mål hör till de norrländska dialekterna. Lyssna efter den särskilda rytmen och jämför med Västerbotten.'),
('lappland','Lappland','I Lappland finns stora avstånd och många lokala språkvarianter. Dialekterna kan därför låta olika beroende på var man befinner sig.'),
('medelpad','Medelpad','Medelpad ligger längs Norrlandskusten. Här möts kustnära språkdrag och en tydlig norrländsk språkmelodi.'),
('norrbotten','Norrbotten','Norrbottniska mål finns längst upp i Sverige. Uttalet kan variera mycket mellan kust, inland och olika orter.'),
('vasterbotten','Västerbotten','Västerbottniska mål har en tydlig norrländsk karaktär. Lyssna på rytmen och jämför med Norrbotten och Ångermanland.'),
('angermanland','Ångermanland','Ångermanland ligger vid Norrlandskusten. Här finns flera lokala uttal och en melodi som kan kännas typiskt norrländsk.'),
('bergslagsmal','Bergslagsmål','Bergslagsmål används i delar av Svealand. Området har historiskt haft många kontakter mellan olika språk och dialekter.'),
('dalarna','Dalarna','Dalarna har många olika dialekter inom ett ganska litet område. Därför kan två dalmål låta överraskande olika.'),
('gastrikland','Gästrikland','Gästrikland ligger söder om Norrland. Språket visar drag från både sveamål och norrländska mål.'),
('narke','Närke','I Närke hörs sveamål med lokala variationer. Området ligger centralt och har länge haft kontakt med många andra delar av Sverige.'),
('sodermanland','Södermanland','Sörmländska mål hör till sveamålen. Lyssna efter melodin och jämför den med Uppland och Västmanland.'),
('uppland','Uppland','Uppländska mål är en del av sveamålen. Uttalet kan skilja sig mellan landsbygd och stad, och mellan olika delar av landskapet.'),
('vastmanland','Västmanland','Västmanland har sveamålsdrag och ligger nära flera andra dialektområden. Därför finns många lokala variationer.'),
('ostergotland','Östergötland','Östergötland har östsvenska språkdrag. Här kan uttal och melodi skilja sig tydligt från dialekterna längre västerut.'),
('oland','Öland','På Öland finns sydsvenska dialektdrag och många lokala varianter. Ön har också en lång historia av kontakt över Östersjön.'),
]
os.makedirs('audio',exist_ok=True)
for slug,name,text in items:
    wav=f'audio/{slug}.wav'; mp3=f'audio/{slug}.mp3'
    seed=sum(ord(c) for c in name)
    speed=142+seed%16; pitch=45+seed%12
    subprocess.run(['espeak','-v','sv','-s',str(speed),'-p',str(pitch),'-a','125','-w',wav,text],check=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',wav,'-ac','1','-ar','22050','-af','apad,atrim=0:15,afade=t=in:st=0:d=0.15,afade=t=out:st=14.7:d=0.3','-t','15','-codec:a','libmp3lame','-b:a','24k',mp3],check=True)
    os.remove(wav)
