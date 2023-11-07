import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from io import StringIO

# Replace the following string with your CSV data
data = """

ORDERNUMBER,QUANTITYORDERED,PRICEEACH,ORDERLINENUMBER,SALES,ORDERDATE,STATUS,QTR_ID,MONTH_ID,YEAR_ID,PRODUCTLINE,MSRP,PRODUCTCODE,CUSTOMERNAME,PHONE,ADDRESSLINE1,ADDRESSLINE2,CITY,STATE,POSTALCODE,COUNTRY,TERRITORY,CONTACTLASTNAME,CONTACTFIRSTNAME,DEALSIZE
10107,30,95.7,2,2871,2/24/2003 0:00,Shipped,1,2,2003,Motorcycles,95,S10_1678,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10121,34,81.35,5,2765.9,5/7/2003 0:00,Shipped,2,5,2003,Motorcycles,95,S10_1678,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10134,41,94.74,2,3884.34,7/1/2003 0:00,Shipped,3,7,2003,Motorcycles,95,S10_1678,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10145,45,83.26,6,3746.7,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,95,S10_1678,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10159,49,100,14,5205.27,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,95,S10_1678,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10168,36,96.66,1,3479.76,10/28/2003 0:00,Shipped,4,10,2003,Motorcycles,95,S10_1678,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10180,29,86.13,9,2497.77,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,95,S10_1678,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10188,48,100,1,5512.32,11/18/2003 0:00,Shipped,4,11,2003,Motorcycles,95,S10_1678,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10201,22,98.57,2,2168.54,12/1/2003 0:00,Shipped,4,12,2003,Motorcycles,95,S10_1678,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10211,41,100,14,4708.44,1/15/2004 0:00,Shipped,1,1,2004,Motorcycles,95,S10_1678,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10223,37,100,1,3965.66,2/20/2004 0:00,Shipped,1,2,2004,Motorcycles,95,S10_1678,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10237,23,100,7,2333.12,4/5/2004 0:00,Shipped,2,4,2004,Motorcycles,95,S10_1678,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10251,28,100,2,3188.64,5/18/2004 0:00,Shipped,2,5,2004,Motorcycles,95,S10_1678,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Medium
10263,34,100,2,3676.76,6/28/2004 0:00,Shipped,2,6,2004,Motorcycles,95,S10_1678,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10275,45,92.83,1,4177.35,7/23/2004 0:00,Shipped,3,7,2004,Motorcycles,95,S10_1678,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10285,36,100,6,4099.68,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,95,S10_1678,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10299,23,100,9,2597.39,9/30/2004 0:00,Shipped,3,9,2004,Motorcycles,95,S10_1678,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10309,41,100,5,4394.38,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,95,S10_1678,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10318,46,94.74,1,4358.04,11/2/2004 0:00,Shipped,4,11,2004,Motorcycles,95,S10_1678,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10329,42,100,1,4396.14,11/15/2004 0:00,Shipped,4,11,2004,Motorcycles,95,S10_1678,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10341,41,100,9,7737.93,11/24/2004 0:00,Shipped,4,11,2004,Motorcycles,95,S10_1678,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Large
10361,20,72.55,13,1451,12/17/2004 0:00,Shipped,4,12,2004,Motorcycles,95,S10_1678,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10375,21,34.91,12,733.11,2/3/2005 0:00,Shipped,1,2,2005,Motorcycles,95,S10_1678,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10388,42,76.36,4,3207.12,3/3/2005 0:00,Shipped,1,3,2005,Motorcycles,95,S10_1678,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10403,24,100,7,2434.56,4/8/2005 0:00,Shipped,2,4,2005,Motorcycles,95,S10_1678,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10417,66,100,2,7516.08,5/13/2005 0:00,Disputed,2,5,2005,Motorcycles,95,S10_1678,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10103,26,100,11,5404.62,1/29/2003 0:00,Shipped,1,1,2003,Classic Cars,214,S10_1949,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10112,29,100,1,7209.11,3/24/2003 0:00,Shipped,1,3,2003,Classic Cars,214,S10_1949,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Large
10126,38,100,11,7329.06,5/28/2003 0:00,Shipped,2,5,2003,Classic Cars,214,S10_1949,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Large
10140,37,100,11,7374.1,7/24/2003 0:00,Shipped,3,7,2003,Classic Cars,214,S10_1949,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Large
10150,45,100,8,10993.5,9/19/2003 0:00,Shipped,3,9,2003,Classic Cars,214,S10_1949,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Large
10163,21,100,1,4860.24,10/20/2003 0:00,Shipped,4,10,2003,Classic Cars,214,S10_1949,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10174,34,100,4,8014.82,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,214,S10_1949,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Large
10183,23,100,8,5372.57,11/13/2003 0:00,Shipped,4,11,2003,Classic Cars,214,S10_1949,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Medium
10194,42,100,11,7290.36,11/25/2003 0:00,Shipped,4,11,2003,Classic Cars,214,S10_1949,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Large
10206,47,100,6,9064.89,12/5/2003 0:00,Shipped,4,12,2003,Classic Cars,214,S10_1949,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Large
10215,35,100,3,6075.3,1/29/2004 0:00,Shipped,1,1,2004,Classic Cars,214,S10_1949,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Medium
10228,29,100,2,6463.23,3/10/2004 0:00,Shipped,1,3,2004,Classic Cars,214,S10_1949,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Medium
10245,34,100,9,6120.34,5/4/2004 0:00,Shipped,2,5,2004,Classic Cars,214,S10_1949,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10258,32,100,6,7680.64,6/15/2004 0:00,Shipped,2,6,2004,Classic Cars,214,S10_1949,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Large
10270,21,100,9,4905.39,7/19/2004 0:00,Shipped,3,7,2004,Classic Cars,214,S10_1949,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10280,34,100,2,8014.82,8/17/2004 0:00,Shipped,3,8,2004,Classic Cars,214,S10_1949,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Large
10291,37,100,11,7136.19,9/8/2004 0:00,Shipped,3,9,2004,Classic Cars,214,S10_1949,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Large
10304,47,100,6,10172.7,10/11/2004 0:00,Shipped,4,10,2004,Classic Cars,214,S10_1949,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Large
10312,48,100,3,11623.7,10/21/2004 0:00,Shipped,4,10,2004,Classic Cars,214,S10_1949,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10322,40,100,1,6000.4,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,214,S10_1949,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10333,26,100,3,3003,11/18/2004 0:00,Shipped,4,11,2004,Classic Cars,214,S10_1949,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Medium
10347,30,100,1,3944.7,11/29/2004 0:00,Shipped,4,11,2004,Classic Cars,214,S10_1949,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10357,32,100,10,5691.84,12/10/2004 0:00,Shipped,4,12,2004,Classic Cars,214,S10_1949,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10369,41,100,2,4514.92,1/20/2005 0:00,Shipped,1,1,2005,Classic Cars,214,S10_1949,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10381,36,100,3,8254.8,2/17/2005 0:00,Shipped,1,2,2005,Classic Cars,214,S10_1949,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Large
10391,24,100,4,2416.56,3/9/2005 0:00,Shipped,1,3,2005,Classic Cars,214,S10_1949,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10411,23,100,9,4140.23,5/1/2005 0:00,Shipped,2,5,2005,Classic Cars,214,S10_1949,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10424,50,100,6,12001,5/31/2005 0:00,In Process,2,5,2005,Classic Cars,214,S10_1949,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10107,39,99.91,5,3896.49,2/24/2003 0:00,Shipped,1,2,2003,Motorcycles,118,S10_2016,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10120,29,96.34,3,2793.86,4/29/2003 0:00,Shipped,2,4,2003,Motorcycles,118,S10_2016,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10134,27,100,5,3307.77,7/1/2003 0:00,Shipped,3,7,2003,Motorcycles,118,S10_2016,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10145,37,100,9,5192.95,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,118,S10_2016,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10159,37,100,17,5016.83,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,118,S10_2016,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10168,27,100,4,3660.93,10/28/2003 0:00,Shipped,4,10,2003,Motorcycles,118,S10_2016,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10180,42,100,12,4695.6,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,118,S10_2016,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Medium
10188,38,96.34,4,3660.92,11/18/2003 0:00,Shipped,4,11,2003,Motorcycles,118,S10_2016,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10201,24,100,5,3025.92,12/1/2003 0:00,Shipped,4,12,2003,Motorcycles,118,S10_2016,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Medium
10210,23,100,2,3009.09,1/12/2004 0:00,Shipped,1,1,2004,Motorcycles,118,S10_2016,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Medium
10223,47,100,4,5422.39,2/20/2004 0:00,Shipped,1,2,2004,Motorcycles,118,S10_2016,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10236,22,100,1,2852.08,4/3/2004 0:00,Shipped,2,4,2004,Motorcycles,118,S10_2016,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Small
10251,44,100,5,5756.52,5/18/2004 0:00,Shipped,2,5,2004,Motorcycles,118,S10_2016,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Medium
10263,40,100,5,4472,6/28/2004 0:00,Shipped,2,6,2004,Motorcycles,118,S10_2016,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10275,22,100,4,2904.44,7/23/2004 0:00,Shipped,3,7,2004,Motorcycles,118,S10_2016,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10285,47,100,9,6484.59,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,118,S10_2016,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10298,39,96.34,1,3757.26,9/27/2004 0:00,Shipped,3,9,2004,Motorcycles,118,S10_2016,Atelier graphique,40.32.2555,"54, rue Royale",,Nantes,,44000,France,EMEA,Schmitt,Carine,Medium
10308,34,100,2,4043.96,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,118,S10_2016,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10318,45,100,4,5566.5,11/2/2004 0:00,Shipped,4,11,2004,Motorcycles,118,S10_2016,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10329,20,100,2,3176,11/15/2004 0:00,Shipped,4,11,2004,Motorcycles,118,S10_2016,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10339,40,68.92,4,2756.8,11/23/2004 0:00,Shipped,4,11,2004,Motorcycles,118,S10_2016,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10361,26,51.15,8,1329.9,12/17/2004 0:00,Shipped,4,12,2004,Motorcycles,118,S10_2016,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10374,39,100,5,5288.01,2/2/2005 0:00,Shipped,1,2,2005,Motorcycles,118,S10_2016,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Medium
10388,50,44.51,5,2225.5,3/3/2005 0:00,Shipped,1,3,2005,Motorcycles,118,S10_2016,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10402,45,100,1,5833.8,4/7/2005 0:00,Shipped,2,4,2005,Motorcycles,118,S10_2016,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10417,45,100,5,5887.35,5/13/2005 0:00,Disputed,2,5,2005,Motorcycles,118,S10_2016,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10107,27,100,4,6065.55,2/24/2003 0:00,Shipped,1,2,2003,Motorcycles,193,S10_4698,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10120,46,100,2,9264.86,4/29/2003 0:00,Shipped,2,4,2003,Motorcycles,193,S10_4698,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Large
10134,31,100,4,7023.98,7/1/2003 0:00,Shipped,3,7,2003,Motorcycles,193,S10_4698,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Large
10145,33,100,8,5176.38,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,193,S10_4698,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10159,22,100,16,4132.7,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,193,S10_4698,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10168,20,100,3,4183,10/28/2003 0:00,Shipped,4,10,2003,Motorcycles,193,S10_4698,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10180,41,100,11,8892.9,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,193,S10_4698,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Large
10188,45,100,3,8714.7,11/18/2003 0:00,Shipped,4,11,2003,Motorcycles,193,S10_4698,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Large
10201,49,100,4,8065.89,12/1/2003 0:00,Shipped,4,12,2003,Motorcycles,193,S10_4698,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Large
10210,34,100,1,6123.4,1/12/2004 0:00,Shipped,1,1,2004,Motorcycles,193,S10_4698,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Medium
10223,49,100,3,9774.03,2/20/2004 0:00,Shipped,1,2,2004,Motorcycles,193,S10_4698,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Large
10237,39,100,9,7023.9,4/5/2004 0:00,Shipped,2,4,2004,Motorcycles,193,S10_4698,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Large
10251,43,100,4,7078.23,5/18/2004 0:00,Shipped,2,5,2004,Motorcycles,193,S10_4698,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Large
10263,41,100,4,8336.94,6/28/2004 0:00,Shipped,2,6,2004,Motorcycles,193,S10_4698,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Large
10275,36,100,3,6901.92,7/23/2004 0:00,Shipped,3,7,2004,Motorcycles,193,S10_4698,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10285,27,100,8,5438.07,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,193,S10_4698,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10299,29,100,11,6683.34,9/30/2004 0:00,Shipped,3,9,2004,Motorcycles,193,S10_4698,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10308,20,100,1,4570.4,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,193,S10_4698,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10318,37,100,3,7667.14,11/2/2004 0:00,Shipped,4,11,2004,Motorcycles,193,S10_4698,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Large
10329,26,100,3,5868.2,11/15/2004 0:00,Shipped,4,11,2004,Motorcycles,193,S10_4698,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10339,39,76.67,3,2990.13,11/23/2004 0:00,Shipped,4,11,2004,Motorcycles,193,S10_4698,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10362,22,100,4,3664.1,1/5/2005 0:00,Shipped,1,1,2005,Motorcycles,193,S10_4698,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10374,22,100,1,3834.38,2/2/2005 0:00,Shipped,1,2,2005,Motorcycles,193,S10_4698,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Medium
10388,21,86.77,7,1822.17,3/3/2005 0:00,Shipped,1,3,2005,Motorcycles,193,S10_4698,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10403,66,100,9,11886.6,4/8/2005 0:00,Shipped,2,4,2005,Motorcycles,193,S10_4698,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Large
10417,56,100,4,9218.16,5/13/2005 0:00,Disputed,2,5,2005,Motorcycles,193,S10_4698,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10105,50,100,2,7208,2/11/2003 0:00,Shipped,1,2,2003,Classic Cars,136,S10_4757,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Large
10119,46,100,11,5004.8,4/28/2003 0:00,Shipped,2,4,2003,Classic Cars,136,S10_4757,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10129,33,100,2,4398.24,6/12/2003 0:00,Shipped,2,6,2003,Classic Cars,136,S10_4757,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10143,49,100,15,5597.76,8/10/2003 0:00,Shipped,3,8,2003,Classic Cars,136,S10_4757,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10155,32,100,13,4526.08,10/6/2003 0:00,Shipped,4,10,2003,Classic Cars,136,S10_4757,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10167,44,100,9,5924.16,10/23/2003 0:00,Cancelled,4,10,2003,Classic Cars,136,S10_4757,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10178,24,100,12,3492.48,11/8/2003 0:00,Shipped,4,11,2003,Classic Cars,136,S10_4757,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10186,26,100,9,3854.24,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,136,S10_4757,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Medium
10197,45,100,6,5324.4,11/26/2003 0:00,Shipped,4,11,2003,Classic Cars,136,S10_4757,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10209,39,100,8,5197.92,1/9/2004 0:00,Shipped,1,1,2004,Classic Cars,136,S10_4757,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Medium
10222,49,100,12,5997.6,2/19/2004 0:00,Shipped,1,2,2004,Classic Cars,136,S10_4757,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10248,20,100,3,2910.4,5/7/2004 0:00,Cancelled,2,5,2004,Classic Cars,136,S10_4757,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10261,27,100,1,3378.24,6/17/2004 0:00,Shipped,2,6,2004,Classic Cars,136,S10_4757,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10273,30,100,4,3508.8,7/21/2004 0:00,Shipped,3,7,2004,Classic Cars,136,S10_4757,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10283,25,100,6,2992,8/20/2004 0:00,Shipped,3,8,2004,Classic Cars,136,S10_4757,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10295,24,100,1,3427.2,9/10/2004 0:00,Shipped,3,9,2004,Classic Cars,136,S10_4757,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10307,22,100,9,2692.8,10/14/2004 0:00,Shipped,4,10,2004,Classic Cars,136,S10_4757,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10316,33,100,17,4128.96,11/1/2004 0:00,Shipped,4,11,2004,Classic Cars,136,S10_4757,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10325,47,64.93,6,3051.71,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,136,S10_4757,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10337,25,48.05,8,1201.25,11/21/2004 0:00,Shipped,4,11,2004,Classic Cars,136,S10_4757,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Small
10350,26,75.47,5,1962.22,12/2/2004 0:00,Shipped,4,12,2004,Classic Cars,136,S10_4757,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10359,48,54.68,6,2624.64,12/15/2004 0:00,Shipped,4,12,2004,Classic Cars,136,S10_4757,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10373,39,100,3,4046.25,1/31/2005 0:00,Shipped,1,1,2005,Classic Cars,136,S10_4757,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10384,34,100,4,4846.7,2/23/2005 0:00,Shipped,1,2,2005,Classic Cars,136,S10_4757,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10395,32,100,2,3370.56,3/17/2005 0:00,Shipped,1,3,2005,Classic Cars,136,S10_4757,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10400,64,100,9,9661.44,4/1/2005 0:00,Shipped,2,4,2005,Classic Cars,136,S10_4757,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Large
10414,19,100,3,2764.88,5/6/2005 0:00,On Hold,2,5,2005,Classic Cars,136,S10_4757,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10103,42,100,4,5398.26,1/29/2003 0:00,Shipped,1,1,2003,Classic Cars,147,S10_4962,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10114,31,100,8,4305.28,4/1/2003 0:00,Shipped,2,4,2003,Classic Cars,147,S10_4962,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10126,22,100,4,3347.74,5/28/2003 0:00,Shipped,2,5,2003,Classic Cars,147,S10_4962,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10140,26,100,4,3188.12,7/24/2003 0:00,Shipped,3,7,2003,Classic Cars,147,S10_4962,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10150,20,100,1,3191.2,9/19/2003 0:00,Shipped,3,9,2003,Classic Cars,147,S10_4962,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10164,21,100,2,3536.82,10/21/2003 0:00,Resolved,4,10,2003,Classic Cars,147,S10_4962,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Medium
10175,33,100,9,5362.83,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,147,S10_4962,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10183,28,100,1,3433.36,11/13/2003 0:00,Shipped,4,11,2003,Classic Cars,147,S10_4962,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Medium
10194,26,100,4,4263.74,11/25/2003 0:00,Shipped,4,11,2003,Classic Cars,147,S10_4962,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10207,31,100,15,4076.19,12/9/2003 0:00,Shipped,4,12,2003,Classic Cars,147,S10_4962,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Medium
10217,48,100,4,7020.48,2/4/2004 0:00,Shipped,1,2,2004,Classic Cars,147,S10_4962,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Large
10229,50,100,9,6426.5,3/11/2004 0:00,Shipped,1,3,2004,Classic Cars,147,S10_4962,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10245,28,100,2,4591.72,5/4/2004 0:00,Shipped,2,5,2004,Classic Cars,147,S10_4962,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10259,26,100,12,4033.38,6/15/2004 0:00,Shipped,2,6,2004,Classic Cars,147,S10_4962,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10270,32,100,2,4302.08,7/19/2004 0:00,Shipped,3,7,2004,Classic Cars,147,S10_4962,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10281,44,100,9,7020.64,8/19/2004 0:00,Shipped,3,8,2004,Classic Cars,147,S10_4962,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Large
10291,30,100,4,3855.9,9/8/2004 0:00,Shipped,3,9,2004,Classic Cars,147,S10_4962,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10305,38,100,13,6680.78,10/13/2004 0:00,Shipped,4,10,2004,Classic Cars,147,S10_4962,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10313,40,100,7,6678,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,147,S10_4962,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10322,46,61.99,8,2851.54,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,147,S10_4962,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10334,26,100,2,3188.12,11/19/2004 0:00,On Hold,4,11,2004,Classic Cars,147,S10_4962,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10347,27,100,2,4428,11/29/2004 0:00,Shipped,4,11,2004,Classic Cars,147,S10_4962,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10357,43,100,9,5780.92,12/10/2004 0:00,Shipped,4,12,2004,Classic Cars,147,S10_4962,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10370,35,65.63,4,2297.05,1/20/2005 0:00,Shipped,1,1,2005,Classic Cars,147,S10_4962,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10381,37,100,6,6231.54,2/17/2005 0:00,Shipped,1,2,2005,Classic Cars,147,S10_4962,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10391,37,46.9,7,1735.3,3/9/2005 0:00,Shipped,1,3,2005,Classic Cars,147,S10_4962,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10411,27,100,2,4427.73,5/1/2005 0:00,Shipped,2,5,2005,Classic Cars,147,S10_4962,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10425,38,100,12,5894.94,5/31/2005 0:00,In Process,2,5,2005,Classic Cars,147,S10_4962,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10108,33,100,6,5265.15,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,194,S12_1099,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10122,42,100,10,7599.9,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,194,S12_1099,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Large
10135,42,100,7,8008.56,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,194,S12_1099,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10147,48,100,7,9245.76,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,194,S12_1099,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Large
10159,41,100,2,8296.35,10/10/2003 0:00,Shipped,4,10,2003,Classic Cars,194,S12_1099,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Large
10169,30,100,2,5019.9,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,194,S12_1099,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10181,27,100,14,5411.07,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,194,S12_1099,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10191,21,100,3,3840.9,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,194,S12_1099,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10203,20,100,8,3930.4,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,194,S12_1099,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10211,41,100,2,7498.9,1/15/2004 0:00,Shipped,1,1,2004,Classic Cars,194,S12_1099,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Large
10225,27,100,9,4517.91,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,194,S12_1099,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10238,28,100,3,5774.72,4/9/2004 0:00,Shipped,2,4,2004,Classic Cars,194,S12_1099,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10253,24,100,13,3922.56,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,194,S12_1099,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10266,44,100,14,9160.36,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,194,S12_1099,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Large
10276,50,100,3,9631,8/2/2004 0:00,Shipped,3,8,2004,Classic Cars,194,S12_1099,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Large
10287,21,100,12,3432.24,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,194,S12_1099,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10300,33,100,5,5521.89,10/4/2003 0:00,Shipped,4,10,2003,Classic Cars,194,S12_1099,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10310,33,100,10,6934.62,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,194,S12_1099,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10320,31,100,3,6876.11,11/3/2004 0:00,Shipped,4,11,2004,Classic Cars,194,S12_1099,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10329,41,71.47,5,2930.27,11/15/2004 0:00,Shipped,4,11,2004,Classic Cars,194,S12_1099,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10341,45,79.65,2,3584.25,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,194,S12_1099,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10363,33,85.39,3,2817.87,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,194,S12_1099,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10375,45,76,7,3420,2/3/2005 0:00,Shipped,1,2,2005,Classic Cars,194,S12_1099,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10389,26,99.04,4,2575.04,3/3/2005 0:00,Shipped,1,3,2005,Classic Cars,194,S12_1099,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10419,12,100,13,1961.28,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,194,S12_1099,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10105,41,100,15,8690.36,2/11/2003 0:00,Shipped,1,2,2003,Classic Cars,207,S12_1108,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Large
10117,33,100,9,6034.38,4/16/2003 0:00,Shipped,2,4,2003,Classic Cars,207,S12_1108,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10127,46,100,2,11279.2,6/3/2003 0:00,Shipped,2,6,2003,Classic Cars,207,S12_1108,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Large
10142,33,100,12,8023.29,8/8/2003 0:00,Shipped,3,8,2003,Classic Cars,207,S12_1108,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10153,20,100,11,4904,9/28/2003 0:00,Shipped,3,9,2003,Classic Cars,207,S12_1108,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10165,44,100,3,8594.52,10/22/2003 0:00,Shipped,4,10,2003,Classic Cars,207,S12_1108,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Large
10176,33,100,2,7474.5,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,207,S12_1108,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Large
10185,21,100,13,3883.74,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,207,S12_1108,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10196,47,100,5,8887.7,11/26/2003 0:00,Shipped,4,11,2003,Classic Cars,207,S12_1108,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Large
10208,46,100,13,8602.92,1/2/2004 0:00,Shipped,1,1,2004,Classic Cars,207,S12_1108,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Large
10220,32,100,2,7181.44,2/12/2004 0:00,Shipped,1,2,2004,Classic Cars,207,S12_1108,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Large
10231,42,100,2,8378.58,3/19/2004 0:00,Shipped,1,3,2004,Classic Cars,207,S12_1108,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Large
10247,44,100,2,10606.2,5/5/2004 0:00,Shipped,2,5,2004,Classic Cars,207,S12_1108,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Large
10272,35,100,2,5818.4,7/20/2004 0:00,Shipped,3,7,2004,Classic Cars,207,S12_1108,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10282,41,100,5,7071.27,8/20/2004 0:00,Shipped,3,8,2004,Classic Cars,207,S12_1108,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10293,46,100,8,8411.56,9/9/2004 0:00,Shipped,3,9,2004,Classic Cars,207,S12_1108,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Large
10306,31,100,13,6570.76,10/14/2004 0:00,Shipped,4,10,2004,Classic Cars,207,S12_1108,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10314,38,100,5,7975.44,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,207,S12_1108,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Large
10325,42,64,8,2688,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,207,S12_1108,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10336,33,57.22,10,1888.26,11/20/2004 0:00,Shipped,4,11,2004,Classic Cars,207,S12_1108,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Small
10348,48,52.36,8,2513.28,11/1/2004 0:00,Shipped,4,11,2004,Classic Cars,207,S12_1108,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10359,42,100,8,4764.48,12/15/2004 0:00,Shipped,4,12,2004,Classic Cars,207,S12_1108,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10371,32,100,6,3560.64,1/23/2005 0:00,Shipped,1,1,2005,Classic Cars,207,S12_1108,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10382,34,100,10,3823.64,2/17/2005 0:00,Shipped,1,2,2005,Classic Cars,207,S12_1108,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10395,33,69.12,1,2280.96,3/17/2005 0:00,Shipped,1,3,2005,Classic Cars,207,S12_1108,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Small
10413,36,100,2,8677.8,5/5/2005 0:00,Shipped,2,5,2005,Classic Cars,207,S12_1108,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Large
10103,27,100,8,3394.98,1/29/2003 0:00,Shipped,1,1,2003,Trucks and Buses,136,S12_1666,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10113,21,100,2,3415.44,3/26/2003 0:00,Shipped,1,3,2003,Trucks and Buses,136,S12_1666,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10126,21,100,8,2439.57,5/28/2003 0:00,Shipped,2,5,2003,Trucks and Buses,136,S12_1666,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10140,38,100,8,4829.8,7/24/2003 0:00,Shipped,3,7,2003,Trucks and Buses,136,S12_1666,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10150,30,100,5,4100.1,9/19/2003 0:00,Shipped,3,9,2003,Trucks and Buses,136,S12_1666,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10164,49,100,6,6563.06,10/21/2003 0:00,Resolved,4,10,2003,Trucks and Buses,136,S12_1666,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Medium
10174,43,100,1,6817.22,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,136,S12_1666,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Medium
10183,41,100,5,6163.94,11/13/2003 0:00,Shipped,4,11,2003,Trucks and Buses,136,S12_1666,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Medium
10194,38,100,8,4933.92,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,136,S12_1666,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10206,28,100,3,4056.36,12/5/2003 0:00,Shipped,4,12,2003,Trucks and Buses,136,S12_1666,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10216,43,100,1,5759.42,2/2/2004 0:00,Shipped,1,2,2004,Trucks and Buses,136,S12_1666,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Medium
10229,25,100,13,3451,3/11/2004 0:00,Shipped,1,3,2004,Trucks and Buses,136,S12_1666,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10245,38,100,6,5920.4,5/4/2004 0:00,Shipped,2,5,2004,Trucks and Buses,136,S12_1666,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10258,41,100,3,6668.24,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,136,S12_1666,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10270,28,100,6,4094.72,7/19/2004 0:00,Shipped,3,7,2004,Trucks and Buses,136,S12_1666,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10281,25,100,13,2938.5,8/19/2004 0:00,Shipped,3,8,2004,Trucks and Buses,136,S12_1666,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10291,41,100,8,6387.8,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,136,S12_1666,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10304,39,100,3,6396,10/11/2004 0:00,Shipped,4,10,2004,Trucks and Buses,136,S12_1666,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Medium
10313,21,100,11,2669.1,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,136,S12_1666,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10322,27,100,9,4784.13,11/4/2004 0:00,Shipped,4,11,2004,Trucks and Buses,136,S12_1666,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10333,33,99.21,6,3273.93,11/18/2004 0:00,Shipped,4,11,2004,Trucks and Buses,136,S12_1666,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Medium
10347,29,100,3,3586.43,11/29/2004 0:00,Shipped,4,11,2004,Trucks and Buses,136,S12_1666,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10357,49,100,8,5960.36,12/10/2004 0:00,Shipped,4,12,2004,Trucks and Buses,136,S12_1666,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10370,49,100,8,8470.14,1/20/2005 0:00,Shipped,1,1,2005,Trucks and Buses,136,S12_1666,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Large
10381,20,100,1,2952,2/17/2005 0:00,Shipped,1,2,2005,Trucks and Buses,136,S12_1666,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10391,39,63.2,9,2464.8,3/9/2005 0:00,Shipped,1,3,2005,Trucks and Buses,136,S12_1666,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10411,40,100,6,6232,5/1/2005 0:00,Shipped,2,5,2005,Trucks and Buses,136,S12_1666,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10424,49,100,3,7969.36,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,136,S12_1666,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10107,21,100,1,3036.6,2/24/2003 0:00,Shipped,1,2,2003,Motorcycles,150,S12_2823,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10121,50,100,4,8284,5/7/2003 0:00,Shipped,2,5,2003,Motorcycles,150,S12_2823,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Large
10134,20,100,1,2711.2,7/1/2003 0:00,Shipped,3,7,2003,Motorcycles,150,S12_2823,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Small
10145,49,100,5,8339.8,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,150,S12_2823,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Large
10159,38,100,13,6238.84,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,150,S12_2823,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10169,35,100,13,4639.25,11/4/2003 0:00,Shipped,4,11,2003,Motorcycles,150,S12_2823,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10180,40,100,8,6747.6,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,150,S12_2823,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Medium
10189,28,100,1,4512.48,11/18/2003 0:00,Shipped,4,11,2003,Motorcycles,150,S12_2823,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10201,25,100,1,4029,12/1/2003 0:00,Shipped,4,12,2003,Motorcycles,150,S12_2823,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Medium
10211,36,100,13,4771.8,1/15/2004 0:00,Shipped,1,1,2004,Motorcycles,150,S12_2823,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10224,43,100,6,6087.94,2/21/2004 0:00,Shipped,1,2,2004,Motorcycles,150,S12_2823,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Medium
10237,32,100,6,4193.28,4/5/2004 0:00,Shipped,2,4,2004,Motorcycles,150,S12_2823,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10251,46,100,1,7552.28,5/18/2004 0:00,Shipped,2,5,2004,Motorcycles,150,S12_2823,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Large
10263,48,100,1,6434.4,6/28/2004 0:00,Shipped,2,6,2004,Motorcycles,150,S12_2823,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10276,43,100,14,5181.5,8/2/2004 0:00,Shipped,3,8,2004,Motorcycles,150,S12_2823,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Medium
10285,49,100,5,6863.92,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,150,S12_2823,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10299,24,100,8,4157.04,9/30/2004 0:00,Shipped,3,9,2004,Motorcycles,150,S12_2823,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10309,26,100,4,4660.24,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,150,S12_2823,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10319,30,100,9,4111.8,11/3/2004 0:00,Shipped,4,11,2004,Motorcycles,150,S12_2823,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Medium
10329,24,100,6,3542.64,11/15/2004 0:00,Shipped,4,11,2004,Motorcycles,150,S12_2823,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10341,55,100,8,8118.55,11/24/2004 0:00,Shipped,4,11,2004,Motorcycles,150,S12_2823,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Large
10362,22,100,1,3877.06,1/5/2005 0:00,Shipped,1,1,2005,Motorcycles,150,S12_2823,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10375,49,78.92,13,3867.08,2/3/2005 0:00,Shipped,1,2,2005,Motorcycles,150,S12_2823,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10388,44,100,6,5951.44,3/3/2005 0:00,Shipped,1,3,2005,Motorcycles,150,S12_2823,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10403,66,100,6,8648.64,4/8/2005 0:00,Shipped,2,4,2005,Motorcycles,150,S12_2823,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Large
10417,21,100,1,3447.78,5/13/2005 0:00,Disputed,2,5,2005,Motorcycles,150,S12_2823,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10104,34,100,1,5958.5,1/31/2003 0:00,Shipped,1,1,2003,Classic Cars,151,S12_3148,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10117,43,100,10,5911.64,4/16/2003 0:00,Shipped,2,4,2003,Classic Cars,151,S12_3148,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10127,46,100,3,7366.44,6/3/2003 0:00,Shipped,2,6,2003,Classic Cars,151,S12_3148,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Large
10142,33,100,13,4985.64,8/8/2003 0:00,Shipped,3,8,2003,Classic Cars,151,S12_3148,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10153,42,100,12,5393.64,9/28/2003 0:00,Shipped,3,9,2003,Classic Cars,151,S12_3148,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10165,34,100,4,4880.02,10/22/2003 0:00,Shipped,4,10,2003,Classic Cars,151,S12_3148,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10176,47,100,3,8378.69,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,151,S12_3148,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Large
10185,33,100,14,4038.21,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,151,S12_3148,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10196,24,100,6,3807.12,11/26/2003 0:00,Shipped,4,11,2003,Classic Cars,151,S12_3148,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10208,26,100,14,3142.36,1/2/2004 0:00,Shipped,1,1,2004,Classic Cars,151,S12_3148,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10220,30,100,3,4713.6,2/12/2004 0:00,Shipped,1,2,2004,Classic Cars,151,S12_3148,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Medium
10230,43,100,1,7016.31,3/15/2004 0:00,Shipped,1,3,2004,Classic Cars,151,S12_3148,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Large
10247,25,100,3,4381.25,5/5/2004 0:00,Shipped,2,5,2004,Classic Cars,151,S12_3148,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10272,27,100,3,4283.01,7/20/2004 0:00,Shipped,3,7,2004,Classic Cars,151,S12_3148,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10282,27,100,6,4364.82,8/20/2004 0:00,Shipped,3,8,2004,Classic Cars,151,S12_3148,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10293,24,100,9,4242.24,9/9/2004 0:00,Shipped,3,9,2004,Classic Cars,151,S12_3148,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10306,34,100,14,4982.7,10/14/2004 0:00,Shipped,4,10,2004,Classic Cars,151,S12_3148,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10314,46,100,6,6393.54,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,151,S12_3148,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10324,27,54.33,1,1466.91,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,151,S12_3148,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10336,33,100,11,4059.33,11/20/2004 0:00,Shipped,4,11,2004,Classic Cars,151,S12_3148,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10348,47,100,4,4801.52,11/1/2004 0:00,Shipped,4,11,2004,Classic Cars,151,S12_3148,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10358,49,55.34,5,2711.66,12/10/2004 0:00,Shipped,4,12,2004,Classic Cars,151,S12_3148,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10372,40,100,4,5862,1/26/2005 0:00,Shipped,1,1,2005,Classic Cars,151,S12_3148,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10382,37,100,11,4071.85,2/17/2005 0:00,Shipped,1,2,2005,Classic Cars,151,S12_3148,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10413,47,100,3,8236.75,5/5/2005 0:00,Shipped,2,5,2005,Classic Cars,151,S12_3148,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Large
10108,45,100,4,6130.35,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,117,S12_3380,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10122,37,99.82,8,3693.34,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,117,S12_3380,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Medium
10135,48,100,5,6031.68,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,117,S12_3380,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10147,31,100,5,3494.94,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,117,S12_3380,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10160,46,100,6,5294.14,10/11/2003 0:00,Shipped,4,10,2003,Classic Cars,117,S12_3380,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Medium
10170,47,100,4,5464.69,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,117,S12_3380,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Medium
10181,28,100,12,2860.76,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,117,S12_3380,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10191,40,100,1,5590,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,117,S12_3380,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10203,20,100,6,2254.8,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,117,S12_3380,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10212,39,100,16,4946.76,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,117,S12_3380,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10225,25,99.82,7,2495.5,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,117,S12_3380,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Small
10238,29,100,1,3167.38,4/9/2004 0:00,Shipped,2,4,2004,Classic Cars,117,S12_3380,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10253,22,100,11,2402.84,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,117,S12_3380,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10266,22,100,12,2454.54,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,117,S12_3380,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10276,47,100,1,5464.69,8/2/2004 0:00,Shipped,3,8,2004,Classic Cars,117,S12_3380,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Medium
10287,45,100,10,4756.5,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,117,S12_3380,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10300,29,100,3,3984.6,10/4/2003 0:00,Shipped,4,10,2003,Classic Cars,117,S12_3380,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10310,24,100,8,3100.32,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,117,S12_3380,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10320,35,100,1,4850.3,11/3/2004 0:00,Shipped,4,11,2004,Classic Cars,117,S12_3380,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10329,46,83.63,13,3846.98,11/15/2004 0:00,Shipped,4,11,2004,Classic Cars,117,S12_3380,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10341,44,95.93,1,4220.92,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,117,S12_3380,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10363,34,96.73,4,3288.82,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,117,S12_3380,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10376,35,100,1,3987.2,2/8/2005 0:00,Shipped,1,2,2005,Classic Cars,117,S12_3380,Boards & Toys Co.,3105552373,4097 Douglas Av.,,Glendale,CA,92561,USA,NA,Young,Leslie,Medium
10389,25,72.38,6,1809.5,3/3/2005 0:00,Shipped,1,3,2005,Classic Cars,117,S12_3380,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10419,10,100,11,1092.2,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,117,S12_3380,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10105,29,100,14,4566.05,2/11/2003 0:00,Shipped,1,2,2003,Classic Cars,173,S12_3891,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10117,39,100,8,5938.14,4/16/2003 0:00,Shipped,2,4,2003,Classic Cars,173,S12_3891,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10127,42,100,1,8138.76,6/3/2003 0:00,Shipped,2,6,2003,Classic Cars,173,S12_3891,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Large
10142,46,100,11,9470.94,8/8/2003 0:00,Shipped,3,8,2003,Classic Cars,173,S12_3891,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10153,49,100,10,7036.89,9/28/2003 0:00,Shipped,3,9,2003,Classic Cars,173,S12_3891,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10165,27,100,2,5559.03,10/22/2003 0:00,Shipped,4,10,2003,Classic Cars,173,S12_3891,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10176,50,100,1,7872.5,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,173,S12_3891,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Large
10185,43,100,12,7886.2,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,173,S12_3891,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Large
10196,38,100,4,7232.16,11/26/2003 0:00,Shipped,4,11,2003,Classic Cars,173,S12_3891,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Large
10208,20,100,12,3114.4,1/2/2004 0:00,Shipped,1,1,2004,Classic Cars,173,S12_3891,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10220,27,100,1,5045.22,2/12/2004 0:00,Shipped,1,2,2004,Classic Cars,173,S12_3891,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Medium
10231,49,100,1,6952.12,3/19/2004 0:00,Shipped,1,3,2004,Classic Cars,173,S12_3891,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Medium
10247,27,100,1,4157.73,5/5/2004 0:00,Shipped,2,5,2004,Classic Cars,173,S12_3891,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10272,39,100,1,7962.24,7/20/2004 0:00,Shipped,3,7,2004,Classic Cars,173,S12_3891,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Large
10282,24,100,4,3778.8,8/20/2004 0:00,Shipped,3,8,2004,Classic Cars,173,S12_3891,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10293,45,100,7,8253,9/9/2004 0:00,Shipped,3,9,2004,Classic Cars,173,S12_3891,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Large
10306,20,100,12,3633.4,10/14/2004 0:00,Shipped,4,10,2004,Classic Cars,173,S12_3891,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10314,36,100,4,6913.8,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,173,S12_3891,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10325,24,100,1,2583.6,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,173,S12_3891,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10336,49,63.38,1,3105.62,11/20/2004 0:00,Shipped,4,11,2004,Classic Cars,173,S12_3891,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10349,26,100,10,4408.56,12/1/2004 0:00,Shipped,4,12,2004,Classic Cars,173,S12_3891,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10359,49,62.09,5,3042.41,12/15/2004 0:00,Shipped,4,12,2004,Classic Cars,173,S12_3891,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10372,34,100,1,5941.5,1/26/2005 0:00,Shipped,1,1,2005,Classic Cars,173,S12_3891,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10382,34,95.35,12,3241.9,2/17/2005 0:00,Shipped,1,2,2005,Classic Cars,173,S12_3891,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10396,33,100,3,6109.29,3/23/2005 0:00,Shipped,1,3,2005,Classic Cars,173,S12_3891,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10413,22,100,1,3387.78,5/5/2005 0:00,Shipped,2,5,2005,Classic Cars,173,S12_3891,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10108,39,89.38,7,3485.82,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,79,S12_3990,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10122,32,63.84,11,2042.88,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,79,S12_3990,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10135,24,75.01,8,1800.24,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,79,S12_3990,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10147,21,63.84,8,1340.64,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,79,S12_3990,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10159,24,73.42,3,1762.08,10/10/2003 0:00,Shipped,4,10,2003,Classic Cars,79,S12_3990,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10169,36,63.84,3,2298.24,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,79,S12_3990,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10181,20,81.4,15,1628,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,79,S12_3990,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10191,30,64.64,4,1939.2,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,79,S12_3990,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10203,44,82.99,9,3651.56,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,79,S12_3990,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10211,28,92.57,3,2591.96,1/15/2004 0:00,Shipped,1,1,2004,Classic Cars,79,S12_3990,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10225,37,77.41,10,2864.17,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,79,S12_3990,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Small
10238,20,74.21,4,1484.2,4/9/2004 0:00,Shipped,2,4,2004,Classic Cars,79,S12_3990,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10253,25,90.17,14,2254.25,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,79,S12_3990,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10266,35,76.61,15,2681.35,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,79,S12_3990,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10276,38,83.79,4,3184.02,8/2/2004 0:00,Shipped,3,8,2004,Classic Cars,79,S12_3990,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Medium
10287,41,69.43,13,2846.63,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,79,S12_3990,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Small
10300,22,76.61,6,1685.42,10/4/2003 0:00,Shipped,4,10,2003,Classic Cars,79,S12_3990,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Small
10310,49,81.4,11,3988.6,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,79,S12_3990,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10320,38,73.42,4,2789.96,11/3/2004 0:00,Shipped,4,11,2004,Classic Cars,79,S12_3990,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Small
10329,33,100,14,3607.56,11/15/2004 0:00,Shipped,4,11,2004,Classic Cars,79,S12_3990,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10341,36,93.56,10,3368.16,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,79,S12_3990,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10363,34,81.62,5,2775.08,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,79,S12_3990,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10377,24,67.83,5,1627.92,2/9/2005 0:00,Shipped,1,2,2005,Classic Cars,79,S12_3990,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10389,36,70.26,7,2529.36,3/3/2005 0:00,Shipped,1,3,2005,Classic Cars,79,S12_3990,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10419,34,90.17,14,3065.78,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,79,S12_3990,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10104,41,100,9,4615.78,1/31/2003 0:00,Shipped,1,1,2003,Trucks and Buses,118,S12_4473,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10115,46,100,5,5723.78,4/4/2003 0:00,Shipped,2,4,2003,Trucks and Buses,118,S12_4473,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10127,24,100,11,2559.6,6/3/2003 0:00,Shipped,2,6,2003,Trucks and Buses,118,S12_4473,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10141,21,100,5,2140.11,8/1/2003 0:00,Shipped,3,8,2003,Trucks and Buses,118,S12_4473,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10151,24,100,3,3327.6,9/21/2003 0:00,Shipped,3,9,2003,Trucks and Buses,118,S12_4473,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10165,48,100,12,6825.6,10/22/2003 0:00,Shipped,4,10,2003,Trucks and Buses,118,S12_4473,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10175,26,100,1,3543.28,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,118,S12_4473,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10184,37,100,6,4516.22,11/14/2003 0:00,Shipped,4,11,2003,Trucks and Buses,118,S12_4473,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Medium
10195,49,100,6,6445.46,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,118,S12_4473,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10207,34,99.54,7,3384.36,12/9/2003 0:00,Shipped,4,12,2003,Trucks and Buses,118,S12_4473,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Medium
10219,48,100,2,4891.68,2/10/2004 0:00,Shipped,1,2,2004,Trucks and Buses,118,S12_4473,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Medium
10229,36,100,1,4521.96,3/11/2004 0:00,Shipped,1,3,2004,Trucks and Buses,118,S12_4473,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10246,46,100,5,5069.66,5/5/2004 0:00,Shipped,2,5,2004,Trucks and Buses,118,S12_4473,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10259,46,100,4,6541.2,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,118,S12_4473,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10271,31,97.17,5,3012.27,7/20/2004 0:00,Shipped,3,7,2004,Trucks and Buses,118,S12_4473,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10281,41,100,1,5247.18,8/19/2004 0:00,Shipped,3,8,2004,Trucks and Buses,118,S12_4473,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10292,21,100,8,2214.87,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,118,S12_4473,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10305,38,100,5,4773.18,10/13/2004 0:00,Shipped,4,10,2004,Trucks and Buses,118,S12_4473,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10314,45,100,14,6185.7,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,118,S12_4473,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10324,26,58.38,7,1517.88,11/5/2004 0:00,Shipped,4,11,2004,Trucks and Buses,118,S12_4473,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10336,38,100,3,6372.6,11/20/2004 0:00,Shipped,4,11,2004,Trucks and Buses,118,S12_4473,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10349,48,100,9,5232.96,12/1/2004 0:00,Shipped,4,12,2004,Trucks and Buses,118,S12_4473,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10358,42,64.16,9,2694.72,12/10/2004 0:00,Shipped,4,12,2004,Trucks and Buses,118,S12_4473,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10371,49,35.71,4,1749.79,1/23/2005 0:00,Shipped,1,1,2005,Trucks and Buses,118,S12_4473,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10382,32,66.58,13,2130.56,2/17/2005 0:00,Shipped,1,2,2005,Trucks and Buses,118,S12_4473,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10412,54,100,5,5951.34,5/3/2005 0:00,Shipped,2,5,2005,Trucks and Buses,118,S12_4473,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10425,33,100,4,4692.6,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,118,S12_4473,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10108,36,100,3,3731.04,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,115,S12_4675,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10122,20,100,7,2142,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,115,S12_4675,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10135,29,97.89,4,2838.81,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,115,S12_4675,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10147,33,97.89,4,3230.37,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,115,S12_4675,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10160,50,100,5,5182,10/11/2003 0:00,Shipped,4,10,2003,Classic Cars,115,S12_4675,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Medium
10170,41,100,3,4391.1,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,115,S12_4675,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Medium
10181,36,100,11,4477.32,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,115,S12_4675,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10192,27,100,16,3544.56,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,115,S12_4675,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10203,47,100,5,5195.85,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,115,S12_4675,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10212,33,100,15,4180.44,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,115,S12_4675,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10225,21,100,6,2684.43,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,115,S12_4675,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Small
10239,21,93.28,5,1958.88,4/12/2004 0:00,Shipped,2,4,2004,Classic Cars,115,S12_4675,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10253,41,100,10,4910.57,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,115,S12_4675,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10266,40,100,11,4468.4,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,115,S12_4675,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10277,28,100,1,3127.88,8/4/2004 0:00,Shipped,3,8,2004,Classic Cars,115,S12_4675,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10287,23,100,9,2675.13,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,115,S12_4675,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Small
10300,23,100,2,2807.61,10/4/2003 0:00,Shipped,4,10,2003,Classic Cars,115,S12_4675,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Small
10310,25,100,7,2504.75,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,115,S12_4675,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10321,24,100,15,2984.88,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,115,S12_4675,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10329,39,64.74,15,2524.86,11/15/2004 0:00,Shipped,4,11,2004,Classic Cars,115,S12_4675,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10341,55,75.2,7,4136,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,115,S12_4675,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10363,46,88.45,6,4068.7,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,115,S12_4675,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10377,50,100,1,5182,2/9/2005 0:00,Shipped,1,2,2005,Classic Cars,115,S12_4675,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10389,47,100,8,5243.79,3/3/2005 0:00,Shipped,1,3,2005,Classic Cars,115,S12_4675,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10405,97,93.28,5,9048.16,4/14/2005 0:00,Shipped,2,4,2005,Classic Cars,115,S12_4675,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Large
10419,32,100,10,3832.64,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,115,S12_4675,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10103,35,100,10,3920,1/29/2003 0:00,Shipped,1,1,2003,Trucks and Buses,116,S18_1097,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10113,49,100,4,4916.66,3/26/2003 0:00,Shipped,1,3,2003,Trucks and Buses,116,S18_1097,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10126,38,100,10,3857,5/28/2003 0:00,Shipped,2,5,2003,Trucks and Buses,116,S18_1097,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10140,32,100,10,4181.44,7/24/2003 0:00,Shipped,3,7,2003,Trucks and Buses,116,S18_1097,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10150,34,100,7,4641,9/19/2003 0:00,Shipped,3,9,2003,Trucks and Buses,116,S18_1097,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10164,36,99.17,8,3570.12,10/21/2003 0:00,Resolved,4,10,2003,Trucks and Buses,116,S18_1097,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Medium
10174,48,93.34,3,4480.32,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,116,S18_1097,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Medium
10183,21,96.84,7,2033.64,11/13/2003 0:00,Shipped,4,11,2003,Trucks and Buses,116,S18_1097,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10194,21,93.34,10,1960.14,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,116,S18_1097,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10206,34,100,5,3966.78,12/5/2003 0:00,Shipped,4,12,2003,Trucks and Buses,116,S18_1097,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10215,46,100,2,5152,1/29/2004 0:00,Shipped,1,1,2004,Trucks and Buses,116,S18_1097,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Medium
10228,32,100,1,3360,3/10/2004 0:00,Shipped,1,3,2004,Trucks and Buses,116,S18_1097,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Medium
10245,29,100,8,3451,5/4/2004 0:00,Shipped,2,5,2004,Trucks and Buses,116,S18_1097,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10258,41,100,5,5453,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,116,S18_1097,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10270,43,96.84,8,4164.12,7/19/2004 0:00,Shipped,3,7,2004,Trucks and Buses,116,S18_1097,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10280,24,100,1,2800.08,8/17/2004 0:00,Shipped,3,8,2004,Trucks and Buses,116,S18_1097,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10291,41,100,10,4687.94,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,116,S18_1097,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10304,46,98,5,4508,10/11/2004 0:00,Shipped,4,10,2004,Trucks and Buses,116,S18_1097,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Medium
10312,32,100,2,4181.44,10/21/2004 0:00,Shipped,4,10,2004,Trucks and Buses,116,S18_1097,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10322,22,100,10,2251.04,11/4/2004 0:00,Shipped,4,11,2004,Trucks and Buses,116,S18_1097,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10333,29,40.25,7,1167.25,11/18/2004 0:00,Shipped,4,11,2004,Trucks and Buses,116,S18_1097,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10347,42,49.6,5,2083.2,11/29/2004 0:00,Shipped,4,11,2004,Trucks and Buses,116,S18_1097,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10357,39,98,1,3822,12/10/2004 0:00,Shipped,4,12,2004,Trucks and Buses,116,S18_1097,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10370,27,100,1,3911.49,1/20/2005 0:00,Shipped,1,1,2005,Trucks and Buses,116,S18_1097,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10381,48,98,2,4704,2/17/2005 0:00,Shipped,1,2,2005,Trucks and Buses,116,S18_1097,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10391,29,85.1,10,2467.9,3/9/2005 0:00,Shipped,1,3,2005,Trucks and Buses,116,S18_1097,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10411,27,100,8,3213,5/1/2005 0:00,Shipped,2,5,2005,Trucks and Buses,116,S18_1097,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10424,54,100,5,7182,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,116,S18_1097,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10109,26,100,4,4379.18,3/10/2003 0:00,Shipped,1,3,2003,Classic Cars,141,S18_1129,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10122,34,100,2,5004.8,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,141,S18_1129,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Medium
10136,25,100,2,3644.75,7/4/2003 0:00,Shipped,3,7,2003,Classic Cars,141,S18_1129,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10148,23,100,13,2702.04,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,141,S18_1129,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10161,28,100,12,3764.88,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,141,S18_1129,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10171,35,100,2,4508,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,141,S18_1129,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10181,44,100,6,5418.16,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,141,S18_1129,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10192,22,100,11,3300.66,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,141,S18_1129,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10204,42,100,17,6182.4,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,141,S18_1129,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10212,29,100,10,4186.73,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,141,S18_1129,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10225,32,100,1,4529.28,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,141,S18_1129,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10240,41,100,3,5628.89,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,141,S18_1129,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Medium
10253,26,100,5,3054.48,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,141,S18_1129,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10266,21,100,6,2526.51,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,141,S18_1129,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10278,34,100,6,4667.86,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,141,S18_1129,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10287,41,100,4,6499.32,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,141,S18_1129,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10301,37,100,8,5917.78,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,141,S18_1129,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Medium
10310,37,100,2,6231.91,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,141,S18_1129,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10321,41,100,10,5803.14,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,141,S18_1129,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10331,46,100,6,6434.02,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,141,S18_1129,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10342,40,100,2,6454.4,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,141,S18_1129,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10356,43,97.6,8,4196.8,12/9/2004 0:00,Shipped,4,12,2004,Classic Cars,141,S18_1129,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10365,30,87.06,1,2611.8,1/7/2005 0:00,Shipped,1,1,2005,Classic Cars,141,S18_1129,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10377,35,100,2,5895.05,2/9/2005 0:00,Shipped,1,2,2005,Classic Cars,141,S18_1129,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10390,36,93.77,14,3375.72,3/4/2005 0:00,Shipped,1,3,2005,Classic Cars,141,S18_1129,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10406,61,100,3,8374.69,4/15/2005 0:00,Disputed,2,4,2005,Classic Cars,141,S18_1129,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Large
10419,38,100,5,4464.24,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,141,S18_1129,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10102,39,100,2,4808.31,1/10/2003 0:00,Shipped,1,1,2003,Vintage Cars,102,S18_1342,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10111,33,99.66,6,3288.78,3/25/2003 0:00,Shipped,1,3,2003,Vintage Cars,102,S18_1342,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Medium
10125,32,100,1,3254.72,5/21/2003 0:00,Shipped,2,5,2003,Vintage Cars,102,S18_1342,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10139,31,100,7,3184.94,7/16/2003 0:00,Shipped,3,7,2003,Vintage Cars,102,S18_1342,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10149,50,100,4,5907.5,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,102,S18_1342,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Medium
10162,48,91.44,2,4389.12,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,102,S18_1342,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10173,43,100,6,5036.16,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,102,S18_1342,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10182,25,87.33,3,2183.25,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,102,S18_1342,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10193,28,100,7,3106.88,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,102,S18_1342,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Medium
10205,36,100,2,3735.72,12/3/2003 0:00,Shipped,4,12,2003,Vintage Cars,102,S18_1342,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10215,27,89.38,10,2413.26,1/29/2004 0:00,Shipped,1,1,2004,Vintage Cars,102,S18_1342,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Small
10227,25,100,3,2953.75,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,102,S18_1342,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10244,40,100,7,4684.8,4/29/2004 0:00,Shipped,2,4,2004,Vintage Cars,102,S18_1342,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10256,34,95.55,2,3248.7,6/8/2004 0:00,Shipped,2,6,2004,Vintage Cars,102,S18_1342,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10280,50,100,9,5239.5,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,102,S18_1342,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10289,38,100,2,4567.98,9/3/2004 0:00,Shipped,3,9,2004,Vintage Cars,102,S18_1342,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10304,37,95.55,13,3535.35,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,102,S18_1342,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Medium
10312,43,89.38,10,3843.34,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,102,S18_1342,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10322,43,86.3,14,3710.9,11/4/2004 0:00,Shipped,4,11,2004,Vintage Cars,102,S18_1342,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10332,46,95.13,15,4375.98,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,102,S18_1342,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10346,42,36.11,3,1516.62,11/29/2004 0:00,Shipped,4,11,2004,Vintage Cars,102,S18_1342,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10356,50,50.18,9,2509,12/9/2004 0:00,Shipped,4,12,2004,Vintage Cars,102,S18_1342,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Small
10369,44,100,8,9240.44,1/20/2005 0:00,Shipped,1,1,2005,Vintage Cars,102,S18_1342,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Large
10380,27,93.16,13,2515.32,2/16/2005 0:00,Shipped,1,2,2005,Vintage Cars,102,S18_1342,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10391,35,100,2,5548.9,3/9/2005 0:00,Shipped,1,3,2005,Vintage Cars,102,S18_1342,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10422,51,95.55,2,4873.05,5/30/2005 0:00,In Process,2,5,2005,Vintage Cars,102,S18_1342,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10102,41,50.14,1,2055.74,1/10/2003 0:00,Shipped,1,1,2003,Vintage Cars,53,S18_1367,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10111,48,49.06,5,2354.88,3/25/2003 0:00,Shipped,1,3,2003,Vintage Cars,53,S18_1367,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10126,42,54.99,17,2309.58,5/28/2003 0:00,Shipped,2,5,2003,Vintage Cars,53,S18_1367,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10139,49,43.13,6,2113.37,7/16/2003 0:00,Shipped,3,7,2003,Vintage Cars,53,S18_1367,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10149,30,58.22,3,1746.6,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,53,S18_1367,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Small
10162,45,51.21,1,2304.45,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,53,S18_1367,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10173,48,44.21,5,2122.08,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,53,S18_1367,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10182,32,54.45,2,1742.4,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,53,S18_1367,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10193,46,53.37,6,2455.02,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,53,S18_1367,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10205,48,63.61,1,3053.28,12/3/2003 0:00,Shipped,4,12,2003,Vintage Cars,53,S18_1367,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10215,33,43.13,9,1423.29,1/29/2004 0:00,Shipped,1,1,2004,Vintage Cars,53,S18_1367,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Small
10227,31,48.52,2,1504.12,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,53,S18_1367,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10244,20,58.22,6,1164.4,4/29/2004 0:00,Shipped,2,4,2004,Vintage Cars,53,S18_1367,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10256,29,51.75,1,1500.75,6/8/2004 0:00,Shipped,2,6,2004,Vintage Cars,53,S18_1367,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10280,27,57.68,8,1557.36,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,53,S18_1367,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10289,24,56.07,1,1345.68,9/3/2004 0:00,Shipped,3,9,2004,Vintage Cars,53,S18_1367,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10304,37,48.52,12,1795.24,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,53,S18_1367,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Small
10312,25,44.21,9,1105.25,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,53,S18_1367,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10322,41,57.68,5,2364.88,11/4/2004 0:00,Shipped,4,11,2004,Vintage Cars,53,S18_1367,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10332,27,89.89,16,2427.03,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,53,S18_1367,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10347,21,58.95,7,1237.95,11/29/2004 0:00,Shipped,4,11,2004,Vintage Cars,53,S18_1367,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10356,22,72.41,6,1593.02,12/9/2004 0:00,Shipped,4,12,2004,Vintage Cars,53,S18_1367,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Small
10369,32,98.63,7,3156.16,1/20/2005 0:00,Shipped,1,1,2005,Vintage Cars,53,S18_1367,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10381,25,52.83,9,1320.75,2/17/2005 0:00,Shipped,1,2,2005,Vintage Cars,53,S18_1367,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10391,42,100,3,4998,3/9/2005 0:00,Shipped,1,3,2005,Vintage Cars,53,S18_1367,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10422,25,51.75,1,1293.75,5/30/2005 0:00,In Process,2,5,2005,Vintage Cars,53,S18_1367,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10110,37,100,16,5433.08,3/18/2003 0:00,Shipped,1,3,2003,Classic Cars,124,S18_1589,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10123,26,100,2,3073.72,5/20/2003 0:00,Shipped,2,5,2003,Classic Cars,124,S18_1589,Atelier graphique,40.32.2555,"54, rue Royale",,Nantes,,44000,France,EMEA,Schmitt,Carine,Medium
10137,44,99.55,2,4380.2,7/10/2003 0:00,Shipped,3,7,2003,Classic Cars,124,S18_1589,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10148,47,100,9,5848.68,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,124,S18_1589,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10161,43,100,8,6153.73,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,124,S18_1589,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10172,42,100,6,4965.24,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,124,S18_1589,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10181,42,100,2,5435.64,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,124,S18_1589,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10192,29,100,7,4258.36,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,124,S18_1589,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10204,40,100,13,4032,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,124,S18_1589,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10212,38,100,6,4492.36,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,124,S18_1589,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10226,38,100,4,4161.38,2/26/2004 0:00,Shipped,1,2,2004,Classic Cars,124,S18_1589,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10241,21,100,11,2508.66,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,124,S18_1589,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10253,24,100,1,3374.88,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,124,S18_1589,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10266,36,100,2,5196.6,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,124,S18_1589,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10278,23,100,2,2604.52,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,124,S18_1589,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10288,20,100,14,2936.8,9/1/2004 0:00,Shipped,3,9,2004,Classic Cars,124,S18_1589,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10301,32,100,4,3424.64,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,124,S18_1589,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Medium
10311,29,100,9,2923.2,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,124,S18_1589,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10321,44,100,6,4489.76,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,124,S18_1589,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10331,44,100,14,4849.24,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,124,S18_1589,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10343,36,100,4,5848.92,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,124,S18_1589,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10367,49,56.3,1,2758.7,1/12/2005 0:00,Resolved,1,1,2005,Classic Cars,124,S18_1589,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10378,34,42.64,5,1449.76,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,124,S18_1589,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10407,59,100,11,7048.14,4/22/2005 0:00,On Hold,2,4,2005,Classic Cars,124,S18_1589,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Large
10419,37,100,1,5202.94,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,124,S18_1589,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10106,36,100,12,5279.4,2/17/2003 0:00,Shipped,1,2,2003,Planes,157,S18_1662,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10119,43,100,3,6916.12,4/28/2003 0:00,Shipped,2,4,2003,Planes,157,S18_1662,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10131,21,100,4,2781.66,6/16/2003 0:00,Shipped,2,6,2003,Planes,157,S18_1662,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Small
10143,32,100,7,5248,8/10/2003 0:00,Shipped,3,8,2003,Planes,157,S18_1662,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10155,38,100,5,6531.44,10/6/2003 0:00,Shipped,4,10,2003,Planes,157,S18_1662,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10167,43,100,1,5763.72,10/23/2003 0:00,Cancelled,4,10,2003,Planes,157,S18_1662,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10178,42,100,4,6490.68,11/8/2003 0:00,Shipped,4,11,2003,Planes,157,S18_1662,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10186,32,100,1,6004.8,11/14/2003 0:00,Shipped,4,11,2003,Planes,157,S18_1662,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Medium
10198,42,100,4,7483.98,11/27/2003 0:00,Shipped,4,11,2003,Planes,157,S18_1662,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Large
10210,31,100,17,5719.5,1/12/2004 0:00,Shipped,1,1,2004,Planes,157,S18_1662,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Medium
10222,49,100,4,6954.08,2/19/2004 0:00,Shipped,1,2,2004,Planes,157,S18_1662,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10250,45,100,14,8160.3,5/11/2004 0:00,Shipped,2,5,2004,Planes,157,S18_1662,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Large
10262,49,100,9,6567.96,6/24/2004 0:00,Cancelled,2,6,2004,Planes,157,S18_1662,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10274,41,100,1,6724,7/21/2004 0:00,Shipped,3,7,2004,Planes,157,S18_1662,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10284,45,100,11,5747.85,8/21/2004 0:00,Shipped,3,8,2004,Planes,157,S18_1662,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Medium
10296,36,100,7,5676.84,9/15/2004 0:00,Shipped,3,9,2004,Planes,157,S18_1662,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Medium
10307,39,100,1,7379.97,10/14/2004 0:00,Shipped,4,10,2004,Planes,157,S18_1662,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Large
10316,27,100,9,3704.13,11/1/2004 0:00,Shipped,4,11,2004,Planes,157,S18_1662,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10327,25,100,6,2804.75,11/10/2004 0:00,Resolved,4,11,2004,Planes,157,S18_1662,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10338,41,100,1,5624.79,11/22/2004 0:00,Shipped,4,11,2004,Planes,157,S18_1662,Royale Belge,(071) 23 67 2555,"Boulevard Tirou, 255",,Charleroi,,B-6000,Belgium,EMEA,Cartrain,Pascale,Medium
10351,39,99.52,1,3881.28,12/3/2004 0:00,Shipped,4,12,2004,Planes,157,S18_1662,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10373,28,57.55,4,1611.4,1/31/2005 0:00,Shipped,1,1,2005,Planes,157,S18_1662,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10386,25,54.57,7,1364.25,3/1/2005 0:00,Resolved,1,3,2005,Planes,157,S18_1662,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10398,33,100,11,4215.09,3/30/2005 0:00,Shipped,1,3,2005,Planes,157,S18_1662,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10400,34,100,1,6433.82,4/1/2005 0:00,Shipped,2,4,2005,Planes,157,S18_1662,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10416,24,100,14,4352.16,5/10/2005 0:00,Shipped,2,5,2005,Planes,157,S18_1662,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10100,30,100,3,5151,1/6/2003 0:00,Shipped,1,1,2003,Vintage Cars,170,S18_1749,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10110,42,100,7,6069,3/18/2003 0:00,Shipped,1,3,2003,Vintage Cars,170,S18_1749,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10124,21,100,6,2856,5/21/2003 0:00,Shipped,2,5,2003,Vintage Cars,170,S18_1749,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10149,34,100,11,5375.4,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,170,S18_1749,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Medium
10162,29,100,9,5176.5,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,170,S18_1749,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10173,24,100,13,3508.8,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,170,S18_1749,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10182,44,100,10,7554.8,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,170,S18_1749,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10193,21,100,14,3141.6,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,170,S18_1749,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Medium
10204,33,100,4,5890.5,12/2/2003 0:00,Shipped,4,12,2003,Vintage Cars,170,S18_1749,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10214,30,100,7,5967,1/26/2004 0:00,Shipped,1,1,2004,Vintage Cars,170,S18_1749,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10227,26,100,10,3712.8,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,170,S18_1749,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10241,41,100,2,7597.3,4/13/2004 0:00,Shipped,2,4,2004,Vintage Cars,170,S18_1749,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Large
10280,26,100,16,3668.6,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,170,S18_1749,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10288,32,100,5,5875.2,9/1/2004 0:00,Shipped,3,9,2004,Vintage Cars,170,S18_1749,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10302,43,100,1,7310,10/6/2003 0:00,Shipped,4,10,2003,Vintage Cars,170,S18_1749,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Large
10312,48,100,17,8078.4,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,170,S18_1749,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10331,44,74.04,7,3257.76,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,170,S18_1749,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10344,45,100,1,7650,11/25/2004 0:00,Shipped,4,11,2004,Vintage Cars,170,S18_1749,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Large
10367,37,100,3,4703.81,1/12/2005 0:00,Resolved,1,1,2005,Vintage Cars,170,S18_1749,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10379,39,100,2,5399.55,2/10/2005 0:00,Shipped,1,2,2005,Vintage Cars,170,S18_1749,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10407,76,100,2,14082.8,4/22/2005 0:00,On Hold,2,4,2005,Vintage Cars,170,S18_1749,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Large
10420,37,100,5,5283.6,5/29/2005 0:00,In Process,2,5,2005,Vintage Cars,170,S18_1749,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10108,38,82.39,2,3130.82,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,77,S18_1889,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10122,43,72.38,6,3112.34,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,77,S18_1889,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Medium
10135,48,79.31,3,3806.88,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,77,S18_1889,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10147,26,82.39,3,2142.14,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,77,S18_1889,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10160,38,88.55,4,3364.9,10/11/2003 0:00,Shipped,4,10,2003,Classic Cars,77,S18_1889,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Medium
10170,20,63.14,2,1262.8,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,77,S18_1889,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Small
10181,22,73.92,10,1626.24,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,77,S18_1889,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10192,45,90.86,15,4088.7,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,77,S18_1889,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10203,45,85.47,4,3846.15,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,77,S18_1889,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10212,20,66.99,14,1339.8,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,77,S18_1889,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10225,47,64.68,5,3039.96,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,77,S18_1889,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10239,46,73.92,4,3400.32,4/12/2004 0:00,Shipped,2,4,2004,Classic Cars,77,S18_1889,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10253,23,83.93,9,1930.39,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,77,S18_1889,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10266,33,74.69,10,2464.77,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,77,S18_1889,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10278,29,90.86,10,2634.94,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,77,S18_1889,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10287,44,82.39,8,3625.16,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,77,S18_1889,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10300,41,92.4,1,3788.4,10/4/2003 0:00,Shipped,4,10,2003,Classic Cars,77,S18_1889,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10310,20,91.63,6,1832.6,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,77,S18_1889,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10321,37,78.54,14,2905.98,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,77,S18_1889,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10329,29,100,9,2954.81,11/15/2004 0:00,Shipped,4,11,2004,Classic Cars,77,S18_1889,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10342,55,65.45,1,3599.75,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,77,S18_1889,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10363,22,100,7,3686.54,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,77,S18_1889,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10377,31,67.76,4,2100.56,2/9/2005 0:00,Shipped,1,2,2005,Classic Cars,77,S18_1889,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10389,49,79.22,3,3881.78,3/3/2005 0:00,Shipped,1,3,2005,Classic Cars,77,S18_1889,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10405,61,73.92,4,4509.12,4/14/2005 0:00,Shipped,2,4,2005,Classic Cars,77,S18_1889,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Medium
10419,39,83.93,9,3273.27,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,77,S18_1889,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10109,38,100,3,4432.7,3/10/2003 0:00,Shipped,1,3,2003,Classic Cars,142,S18_1984,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10122,31,100,1,4100.99,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,142,S18_1984,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Medium
10136,36,100,1,5274.72,7/4/2003 0:00,Shipped,3,7,2003,Classic Cars,142,S18_1984,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10148,25,100,12,4232,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,142,S18_1984,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10161,48,100,11,6145.44,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,142,S18_1984,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10171,35,100,1,4680.2,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,142,S18_1984,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10181,21,100,5,3286.08,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,142,S18_1984,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10192,47,100,10,7421.3,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,142,S18_1984,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Large
10204,38,100,16,6432.64,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,142,S18_1984,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10212,41,100,9,4840.87,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,142,S18_1984,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10226,24,100,7,3892.08,2/26/2004 0:00,Shipped,1,2,2004,Classic Cars,142,S18_1984,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10240,37,100,2,5526.32,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,142,S18_1984,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Medium
10253,33,100,4,4459.62,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,142,S18_1984,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10266,49,100,5,6203.4,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,142,S18_1984,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10278,29,100,5,3754.05,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,142,S18_1984,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10287,24,100,3,3516.48,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,142,S18_1984,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10301,47,100,7,7488.04,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,142,S18_1984,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Large
10310,24,100,1,3448.08,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,142,S18_1984,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10321,25,100,9,3734,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,142,S18_1984,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10331,30,32.47,8,974.1,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,142,S18_1984,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Small
10342,22,100,3,3160.74,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,142,S18_1984,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10356,27,64.69,2,1746.63,12/9/2004 0:00,Shipped,4,12,2004,Classic Cars,142,S18_1984,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Small
10366,34,100,3,4207.84,1/10/2005 0:00,Shipped,1,1,2005,Classic Cars,142,S18_1984,Royale Belge,(071) 23 67 2555,"Boulevard Tirou, 255",,Charleroi,,B-6000,Belgium,EMEA,Cartrain,Pascale,Medium
10377,36,100,6,4352.76,2/9/2005 0:00,Shipped,1,2,2005,Classic Cars,142,S18_1984,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10390,34,43.05,15,1463.7,3/4/2005 0:00,Shipped,1,3,2005,Classic Cars,142,S18_1984,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10406,48,100,2,7169.28,4/15/2005 0:00,Disputed,2,4,2005,Classic Cars,142,S18_1984,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Large
10419,34,100,4,4594.76,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,142,S18_1984,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10104,24,100,8,3457.92,1/31/2003 0:00,Shipped,1,1,2003,Classic Cars,163,S18_2238,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10115,46,100,4,7381.16,4/4/2003 0:00,Shipped,2,4,2003,Classic Cars,163,S18_2238,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Large
10127,45,100,10,7146.9,6/3/2003 0:00,Shipped,2,6,2003,Classic Cars,163,S18_2238,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Large
10141,39,100,4,5938.53,8/1/2003 0:00,Shipped,3,8,2003,Classic Cars,163,S18_2238,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10151,43,100,2,7110.91,9/21/2003 0:00,Shipped,3,9,2003,Classic Cars,163,S18_2238,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Large
10165,29,100,11,5032.95,10/22/2003 0:00,Shipped,4,10,2003,Classic Cars,163,S18_2238,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10176,20,100,10,3667.6,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,163,S18_2238,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10184,46,100,5,7381.16,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,163,S18_2238,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Large
10195,27,100,5,5128.11,11/25/2003 0:00,Shipped,4,11,2003,Classic Cars,163,S18_2238,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10207,44,100,6,7060.24,12/9/2003 0:00,Shipped,4,12,2003,Classic Cars,163,S18_2238,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Large
10219,43,100,1,8448.64,2/10/2004 0:00,Shipped,1,2,2004,Classic Cars,163,S18_2238,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Large
10230,49,100,8,7300.51,3/15/2004 0:00,Shipped,1,3,2004,Classic Cars,163,S18_2238,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Large
10246,40,100,4,6549.2,5/5/2004 0:00,Shipped,2,5,2004,Classic Cars,163,S18_2238,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10259,30,100,3,5697.9,6/15/2004 0:00,Shipped,2,6,2004,Classic Cars,163,S18_2238,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10271,50,100,4,9169,7/20/2004 0:00,Shipped,3,7,2004,Classic Cars,163,S18_2238,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10282,23,100,13,3238.63,8/20/2004 0:00,Shipped,3,8,2004,Classic Cars,163,S18_2238,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10292,26,100,7,4554.94,9/8/2004 0:00,Shipped,3,9,2004,Classic Cars,163,S18_2238,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10305,27,100,4,3934.44,10/13/2004 0:00,Shipped,4,10,2004,Classic Cars,163,S18_2238,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10314,42,100,13,5776.26,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,163,S18_2238,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10324,47,100,8,7207.45,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,163,S18_2238,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Large
10336,49,100,6,7460.74,11/20/2004 0:00,Shipped,4,11,2004,Classic Cars,163,S18_2238,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Large
10349,38,100,8,6719.54,12/1/2004 0:00,Shipped,4,12,2004,Classic Cars,163,S18_2238,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10358,20,100,10,2428,12/10/2004 0:00,Shipped,4,12,2004,Classic Cars,163,S18_2238,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10371,25,100,7,2602.25,1/23/2005 0:00,Shipped,1,1,2005,Classic Cars,163,S18_2238,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10382,25,88,5,2200,2/17/2005 0:00,Shipped,1,2,2005,Classic Cars,163,S18_2238,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10412,41,100,4,6712.93,5/3/2005 0:00,Shipped,2,5,2005,Classic Cars,163,S18_2238,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10425,28,100,3,5318.04,5/31/2005 0:00,In Process,2,5,2005,Classic Cars,163,S18_2238,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10100,50,67.8,2,3390,1/6/2003 0:00,Shipped,1,1,2003,Vintage Cars,60,S18_2248,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10110,32,50.25,6,1608,3/18/2003 0:00,Shipped,1,3,2003,Vintage Cars,60,S18_2248,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10124,42,53.88,5,2262.96,5/21/2003 0:00,Shipped,2,5,2003,Vintage Cars,60,S18_2248,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10149,24,62.36,10,1496.64,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,60,S18_2248,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Small
10162,27,69.62,8,1879.74,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,60,S18_2248,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10173,26,57.51,12,1495.26,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,60,S18_2248,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10182,38,61.15,9,2323.7,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,60,S18_2248,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10193,42,59.33,13,2491.86,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,60,S18_2248,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10204,23,71.44,3,1643.12,12/2/2003 0:00,Shipped,4,12,2003,Vintage Cars,60,S18_2248,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10214,21,62.96,6,1322.16,1/26/2004 0:00,Shipped,1,1,2004,Vintage Cars,60,S18_2248,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10227,28,50.85,9,1423.8,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,60,S18_2248,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10241,33,72.65,1,2397.45,4/13/2004 0:00,Shipped,2,4,2004,Vintage Cars,60,S18_2248,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10280,25,62.96,15,1574,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,60,S18_2248,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10288,28,61.75,4,1729,9/1/2004 0:00,Shipped,3,9,2004,Vintage Cars,60,S18_2248,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10303,46,49.04,2,2255.84,10/6/2004 0:00,Shipped,4,10,2004,Vintage Cars,60,S18_2248,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Small
10312,30,61.15,16,1834.5,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,60,S18_2248,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10332,38,84.25,9,3201.5,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,60,S18_2248,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10344,40,56.91,2,2276.4,11/25/2004 0:00,Shipped,4,11,2004,Vintage Cars,60,S18_2248,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10367,45,100,4,8884.8,1/12/2005 0:00,Resolved,1,1,2005,Vintage Cars,60,S18_2248,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Large
10379,27,49.3,1,1331.1,2/10/2005 0:00,Shipped,1,2,2005,Vintage Cars,60,S18_2248,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10407,42,72.65,1,3051.3,4/22/2005 0:00,On Hold,2,4,2005,Vintage Cars,60,S18_2248,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10420,36,63.57,4,2288.52,5/29/2005 0:00,In Process,2,5,2005,Vintage Cars,60,S18_2248,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10104,29,100,12,3772.61,1/31/2003 0:00,Shipped,1,1,2003,Trucks and Buses,122,S18_2319,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10114,39,100,3,4164.42,4/1/2003 0:00,Shipped,2,4,2003,Trucks and Buses,122,S18_2319,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10127,45,100,14,6295.95,6/3/2003 0:00,Shipped,2,6,2003,Trucks and Buses,122,S18_2319,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10141,47,100,8,6287.66,8/1/2003 0:00,Shipped,3,8,2003,Trucks and Buses,122,S18_2319,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10151,49,100,6,5412.54,9/21/2003 0:00,Shipped,3,9,2003,Trucks and Buses,122,S18_2319,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10165,46,100,15,5984.14,10/22/2003 0:00,Shipped,4,10,2003,Trucks and Buses,122,S18_2319,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10175,48,100,4,5891.04,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,122,S18_2319,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10184,46,100,9,5984.14,11/14/2003 0:00,Shipped,4,11,2003,Trucks and Buses,122,S18_2319,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Medium
10195,35,100,9,3608.15,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,122,S18_2319,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10207,43,100,10,5752.54,12/9/2003 0:00,Shipped,4,12,2003,Trucks and Buses,122,S18_2319,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Medium
10229,26,100,4,3765.32,3/11/2004 0:00,Shipped,1,3,2004,Trucks and Buses,122,S18_2319,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10246,22,98.18,8,2159.96,5/5/2004 0:00,Shipped,2,5,2004,Trucks and Buses,122,S18_2319,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10259,34,99.41,7,3379.94,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,122,S18_2319,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10271,50,100,8,5093.5,7/20/2004 0:00,Shipped,3,7,2004,Trucks and Buses,122,S18_2319,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10281,48,100,4,5773.44,8/19/2004 0:00,Shipped,3,8,2004,Trucks and Buses,122,S18_2319,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10292,41,100,11,4528.86,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,122,S18_2319,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10305,36,100,8,4816.08,10/13/2004 0:00,Shipped,4,10,2004,Trucks and Buses,122,S18_2319,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10313,29,100,2,3416.78,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,122,S18_2319,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10324,33,37.48,10,1236.84,11/5/2004 0:00,Shipped,4,11,2004,Trucks and Buses,122,S18_2319,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10334,46,100,6,5814.86,11/19/2004 0:00,On Hold,4,11,2004,Trucks and Buses,122,S18_2319,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10349,38,100,7,5223.48,12/1/2004 0:00,Shipped,4,12,2004,Trucks and Buses,122,S18_2319,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10358,20,36.42,11,728.4,12/10/2004 0:00,Shipped,4,12,2004,Trucks and Buses,122,S18_2319,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10370,22,100,5,3949,1/20/2005 0:00,Shipped,1,1,2005,Trucks and Buses,122,S18_2319,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10383,27,100,11,3843.99,2/22/2005 0:00,Shipped,1,2,2005,Trucks and Buses,122,S18_2319,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10412,56,98.18,8,5498.08,5/3/2005 0:00,Shipped,2,5,2005,Trucks and Buses,122,S18_2319,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10425,38,99.41,7,3777.58,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,122,S18_2319,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10101,25,100,4,3782,1/9/2003 0:00,Shipped,1,1,2003,Vintage Cars,127,S18_2325,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10110,33,100,4,3859.68,3/18/2003 0:00,Shipped,1,3,2003,Vintage Cars,127,S18_2325,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10124,42,100,3,4431.84,5/21/2003 0:00,Shipped,2,5,2003,Vintage Cars,127,S18_2325,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10149,33,100,8,4950.33,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,127,S18_2325,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Medium
10162,38,100,6,4299.7,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,127,S18_2325,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10173,31,100,10,4492.83,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,127,S18_2325,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10182,20,100,7,2212,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,127,S18_2325,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10193,44,100,11,4642.88,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,127,S18_2325,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Medium
10204,26,100,1,3206.32,12/2/2003 0:00,Shipped,4,12,2003,Vintage Cars,127,S18_2325,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10214,27,100,4,3604.23,1/26/2004 0:00,Shipped,1,1,2004,Vintage Cars,127,S18_2325,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10227,46,100,7,7017.76,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,127,S18_2325,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Large
10243,47,100,2,6154.18,4/26/2004 0:00,Shipped,2,4,2004,Vintage Cars,127,S18_2325,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Medium
10280,37,100,13,4750.8,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,127,S18_2325,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10288,31,100,2,3822.92,9/1/2004 0:00,Shipped,3,9,2004,Vintage Cars,127,S18_2325,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10304,24,100,17,2440.8,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,127,S18_2325,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Small
10312,31,100,14,4729.36,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,127,S18_2325,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10322,50,100,6,12536.5,11/4/2004 0:00,Shipped,4,11,2004,Vintage Cars,127,S18_2325,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Large
10332,35,64.69,8,2264.15,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,127,S18_2325,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10344,30,100,3,3928.2,11/25/2004 0:00,Shipped,4,11,2004,Vintage Cars,127,S18_2325,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Medium
10356,29,100,3,3630.22,12/9/2004 0:00,Shipped,4,12,2004,Vintage Cars,127,S18_2325,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10367,27,100,5,4196.07,1/12/2005 0:00,Resolved,1,1,2005,Vintage Cars,127,S18_2325,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10380,40,100,10,4931.6,2/16/2005 0:00,Shipped,1,2,2005,Vintage Cars,127,S18_2325,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10390,31,98.99,16,3068.69,3/4/2005 0:00,Shipped,1,3,2005,Vintage Cars,127,S18_2325,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10409,6,100,2,785.64,4/23/2005 0:00,Shipped,2,4,2005,Vintage Cars,127,S18_2325,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10420,45,100,2,4977,5/29/2005 0:00,In Process,2,5,2005,Vintage Cars,127,S18_2325,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10103,22,54.09,2,1189.98,1/29/2003 0:00,Shipped,1,1,2003,Trucks and Buses,60,S18_2432,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10114,45,68.67,6,3090.15,4/1/2003 0:00,Shipped,2,4,2003,Trucks and Buses,60,S18_2432,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10126,43,65.02,2,2795.86,5/28/2003 0:00,Shipped,2,5,2003,Trucks and Buses,60,S18_2432,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10140,46,61.99,2,2851.54,7/24/2003 0:00,Shipped,3,7,2003,Trucks and Buses,60,S18_2432,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10151,39,69.28,9,2701.92,9/21/2003 0:00,Shipped,3,9,2003,Trucks and Buses,60,S18_2432,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10165,31,71.1,18,2204.1,10/22/2003 0:00,Shipped,4,10,2003,Trucks and Buses,60,S18_2432,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10175,41,69.28,7,2840.48,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,60,S18_2432,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10184,44,60.16,12,2647.04,11/14/2003 0:00,Shipped,4,11,2003,Trucks and Buses,60,S18_2432,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Small
10194,45,70.49,2,3172.05,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,60,S18_2432,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10207,37,69.89,13,2585.93,12/9/2003 0:00,Shipped,4,12,2003,Trucks and Buses,60,S18_2432,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Small
10217,35,61.38,2,2148.3,2/4/2004 0:00,Shipped,1,2,2004,Trucks and Buses,60,S18_2432,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10229,28,59.55,7,1667.4,3/11/2004 0:00,Shipped,1,3,2004,Trucks and Buses,60,S18_2432,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10246,30,61.99,11,1859.7,5/5/2004 0:00,Shipped,2,5,2004,Trucks and Buses,60,S18_2432,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10259,30,49.22,10,1476.6,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,60,S18_2432,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10271,25,69.28,11,1732,7/20/2004 0:00,Shipped,3,7,2004,Trucks and Buses,60,S18_2432,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10281,29,57.73,7,1674.17,8/19/2004 0:00,Shipped,3,8,2004,Trucks and Buses,60,S18_2432,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10291,26,57.73,2,1500.98,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,60,S18_2432,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10305,41,53.48,11,2192.68,10/13/2004 0:00,Shipped,4,10,2004,Trucks and Buses,60,S18_2432,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10313,34,52.87,5,1797.58,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,60,S18_2432,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10322,35,61.21,11,2142.35,11/4/2004 0:00,Shipped,4,11,2004,Trucks and Buses,60,S18_2432,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10334,34,61.38,1,2086.92,11/19/2004 0:00,On Hold,4,11,2004,Trucks and Buses,60,S18_2432,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Small
10347,50,100,8,6834.5,11/29/2004 0:00,Shipped,4,11,2004,Trucks and Buses,60,S18_2432,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10357,41,61.99,7,2541.59,12/10/2004 0:00,Shipped,4,12,2004,Trucks and Buses,60,S18_2432,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10370,22,96.86,7,2130.92,1/20/2005 0:00,Shipped,1,1,2005,Trucks and Buses,60,S18_2432,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10381,35,48.62,7,1701.7,2/17/2005 0:00,Shipped,1,2,2005,Trucks and Buses,60,S18_2432,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10391,44,38.5,5,1694,3/9/2005 0:00,Shipped,1,3,2005,Trucks and Buses,60,S18_2432,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10412,47,61.99,11,2913.53,5/3/2005 0:00,Shipped,2,5,2005,Trucks and Buses,60,S18_2432,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10425,19,49.22,10,935.18,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,60,S18_2432,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10106,34,90.39,2,3073.26,2/17/2003 0:00,Shipped,1,2,2003,Planes,84,S18_2581,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10120,29,71.81,8,2082.49,4/29/2003 0:00,Shipped,2,4,2003,Planes,84,S18_2581,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10133,49,69.27,3,3394.23,6/27/2003 0:00,Shipped,2,6,2003,Planes,84,S18_2581,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10145,30,85.32,14,2559.6,8/25/2003 0:00,Shipped,3,8,2003,Planes,84,S18_2581,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10168,21,70.96,9,1490.16,10/28/2003 0:00,Shipped,4,10,2003,Planes,84,S18_2581,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10210,50,76.88,7,3844,1/12/2004 0:00,Shipped,1,1,2004,Planes,84,S18_2581,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Medium
10223,47,100,9,4724.91,2/20/2004 0:00,Shipped,1,2,2004,Planes,84,S18_2581,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10235,24,76.03,3,1824.72,4/2/2004 0:00,Shipped,2,4,2004,Planes,84,S18_2581,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10250,27,98.84,4,2668.68,5/11/2004 0:00,Shipped,2,5,2004,Planes,84,S18_2581,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10263,33,86.17,10,2843.61,6/28/2004 0:00,Shipped,2,6,2004,Planes,84,S18_2581,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10275,35,90.39,9,3163.65,7/23/2004 0:00,Shipped,3,7,2004,Planes,84,S18_2581,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10284,31,71.81,1,2226.11,8/21/2004 0:00,Shipped,3,8,2004,Planes,84,S18_2581,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10297,25,82.79,4,2069.75,9/16/2004 0:00,Shipped,3,9,2004,Planes,84,S18_2581,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Small
10308,27,82.79,7,2235.33,10/15/2004 0:00,Shipped,4,10,2004,Planes,84,S18_2581,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10318,31,100,9,3116.43,11/2/2004 0:00,Shipped,4,11,2004,Planes,84,S18_2581,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10327,45,100,8,4781.7,11/10/2004 0:00,Resolved,4,11,2004,Planes,84,S18_2581,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10339,27,100,2,2810.7,11/23/2004 0:00,Shipped,4,11,2004,Planes,84,S18_2581,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10353,27,100,1,3515.67,12/4/2004 0:00,Shipped,4,12,2004,Planes,84,S18_2581,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10374,42,69.27,2,2909.34,2/2/2005 0:00,Shipped,1,2,2005,Planes,84,S18_2581,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Small
10386,21,74.77,18,1570.17,3/1/2005 0:00,Resolved,1,3,2005,Planes,84,S18_2581,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10398,34,76.88,15,2613.92,3/30/2005 0:00,Shipped,1,3,2005,Planes,84,S18_2581,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10401,42,76.03,3,3193.26,4/3/2005 0:00,On Hold,2,4,2005,Planes,84,S18_2581,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Medium
10416,15,98.84,4,1482.6,5/10/2005 0:00,Shipped,2,5,2005,Planes,84,S18_2581,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10107,29,70.87,6,2055.23,2/24/2003 0:00,Shipped,1,2,2003,Motorcycles,60,S18_2625,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10120,46,58.15,4,2674.9,4/29/2003 0:00,Shipped,2,4,2003,Motorcycles,60,S18_2625,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10134,30,61.78,6,1853.4,7/1/2003 0:00,Shipped,3,7,2003,Motorcycles,60,S18_2625,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Small
10145,30,49.67,10,1490.1,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,60,S18_2625,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10159,42,51.48,18,2162.16,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,60,S18_2625,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10168,46,61.18,5,2814.28,10/28/2003 0:00,Shipped,4,10,2003,Motorcycles,60,S18_2625,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10180,25,64.2,13,1605,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,60,S18_2625,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10188,32,65.42,5,2093.44,11/18/2003 0:00,Shipped,4,11,2003,Motorcycles,60,S18_2625,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10201,30,64.81,6,1944.3,12/1/2003 0:00,Shipped,4,12,2003,Motorcycles,60,S18_2625,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10210,40,49.67,3,1986.8,1/12/2004 0:00,Shipped,1,1,2004,Motorcycles,60,S18_2625,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10223,28,60.57,5,1695.96,2/20/2004 0:00,Shipped,1,2,2004,Motorcycles,60,S18_2625,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10236,23,55.72,2,1281.56,4/3/2004 0:00,Shipped,2,4,2004,Motorcycles,60,S18_2625,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Small
10251,29,61.18,6,1774.22,5/18/2004 0:00,Shipped,2,5,2004,Motorcycles,60,S18_2625,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Small
10263,34,58.75,6,1997.5,6/28/2004 0:00,Shipped,2,6,2004,Motorcycles,60,S18_2625,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10275,37,63.6,5,2353.2,7/23/2004 0:00,Shipped,3,7,2004,Motorcycles,60,S18_2625,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10285,20,49.06,10,981.2,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,60,S18_2625,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10298,32,48.46,2,1550.72,9/27/2004 0:00,Shipped,3,9,2004,Motorcycles,60,S18_2625,Atelier graphique,40.32.2555,"54, rue Royale",,Nantes,,44000,France,EMEA,Schmitt,Carine,Small
10308,34,52.09,3,1771.06,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,60,S18_2625,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10318,42,52.7,5,2213.4,11/2/2004 0:00,Shipped,4,11,2004,Motorcycles,60,S18_2625,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10329,38,100,12,5266.04,11/15/2004 0:00,Shipped,4,11,2004,Motorcycles,60,S18_2625,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10339,30,62.16,1,1864.8,11/23/2004 0:00,Shipped,4,11,2004,Motorcycles,60,S18_2625,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10362,23,49.67,3,1142.41,1/5/2005 0:00,Shipped,1,1,2005,Motorcycles,60,S18_2625,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10374,22,53.3,4,1172.6,2/2/2005 0:00,Shipped,1,2,2005,Motorcycles,60,S18_2625,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Small
10389,39,100,5,6981,3/3/2005 0:00,Shipped,1,3,2005,Motorcycles,60,S18_2625,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10402,55,55.72,2,3064.6,4/7/2005 0:00,Shipped,2,4,2005,Motorcycles,60,S18_2625,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10417,36,61.18,6,2202.48,5/13/2005 0:00,Disputed,2,5,2005,Motorcycles,60,S18_2625,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10101,26,100,1,3773.38,1/9/2003 0:00,Shipped,1,1,2003,Vintage Cars,168,S18_2795,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10110,31,100,1,5074.39,3/18/2003 0:00,Shipped,1,3,2003,Vintage Cars,168,S18_2795,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10125,34,100,2,6483.46,5/21/2003 0:00,Shipped,2,5,2003,Vintage Cars,168,S18_2795,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10139,41,100,8,7956.46,7/16/2003 0:00,Shipped,3,7,2003,Vintage Cars,168,S18_2795,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Large
10149,23,100,5,4230.62,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,168,S18_2795,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Medium
10162,48,100,3,7209.12,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,168,S18_2795,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Large
10173,22,100,7,3452.68,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,168,S18_2795,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10182,21,100,4,3047.73,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,168,S18_2795,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10193,22,100,8,3675.32,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,168,S18_2795,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Medium
10205,40,100,3,7492.4,12/3/2003 0:00,Shipped,4,12,2003,Vintage Cars,168,S18_2795,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10214,50,100,1,9534.5,1/26/2004 0:00,Shipped,1,1,2004,Vintage Cars,168,S18_2795,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Large
10227,29,100,4,5579.02,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,168,S18_2795,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10244,43,100,8,5950.34,4/29/2004 0:00,Shipped,2,4,2004,Vintage Cars,168,S18_2795,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10255,24,100,1,3726,6/4/2004 0:00,Shipped,2,6,2004,Vintage Cars,168,S18_2795,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Medium
10280,22,100,10,4455,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,168,S18_2795,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10289,43,100,3,8272.34,9/3/2004 0:00,Shipped,3,9,2004,Vintage Cars,168,S18_2795,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Large
10304,20,100,14,3577.6,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,168,S18_2795,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Medium
10312,25,100,11,3881.25,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,168,S18_2795,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10322,36,100,2,5797.44,11/4/2004 0:00,Shipped,4,11,2004,Vintage Cars,168,S18_2795,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10332,24,52.67,1,1264.08,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,168,S18_2795,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10347,21,100,6,4815.3,11/29/2004 0:00,Shipped,4,11,2004,Vintage Cars,168,S18_2795,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10356,30,100,1,4462.2,12/9/2004 0:00,Shipped,4,12,2004,Vintage Cars,168,S18_2795,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10367,32,94.79,7,3033.28,1/12/2005 0:00,Resolved,1,1,2005,Vintage Cars,168,S18_2795,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10380,21,47.18,8,990.78,2/16/2005 0:00,Shipped,1,2,2005,Vintage Cars,168,S18_2795,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10390,26,78.11,7,2030.86,3/4/2005 0:00,Shipped,1,3,2005,Vintage Cars,168,S18_2795,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10421,35,100,1,5433.75,5/29/2005 0:00,In Process,2,5,2005,Vintage Cars,168,S18_2795,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10109,26,100,1,3157.44,3/10/2003 0:00,Shipped,1,3,2003,Classic Cars,132,S18_2870,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10123,46,100,3,5161.2,5/20/2003 0:00,Shipped,2,5,2003,Classic Cars,132,S18_2870,Atelier graphique,40.32.2555,"54, rue Royale",,Nantes,,44000,France,EMEA,Schmitt,Carine,Medium
10137,37,100,3,4346.76,7/10/2003 0:00,Shipped,3,7,2003,Classic Cars,132,S18_2870,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10148,27,100,10,3528.36,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,132,S18_2870,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10161,23,100,9,3187.8,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,132,S18_2870,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10172,39,100,7,6023.16,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,132,S18_2870,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10181,27,100,3,3884.76,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,132,S18_2870,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10192,38,100,8,4965.84,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,132,S18_2870,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10204,27,100,14,4169.88,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,132,S18_2870,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10212,40,100,7,4910.4,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,132,S18_2870,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10226,24,100,5,3231.36,2/26/2004 0:00,Shipped,1,2,2004,Classic Cars,132,S18_2870,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10241,44,100,12,6853.44,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,132,S18_2870,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Medium
10253,37,100,2,5177.04,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,132,S18_2870,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10266,20,100,3,2824.8,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,132,S18_2870,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10278,39,100,3,4324.32,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,132,S18_2870,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10287,44,100,1,5052.96,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,132,S18_2870,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10301,22,100,5,3223.44,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,132,S18_2870,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Medium
10311,43,100,10,5278.68,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,132,S18_2870,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10321,27,100,7,2851.2,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,132,S18_2870,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10331,26,64.9,10,1687.4,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,132,S18_2870,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Small
10343,25,52.32,3,1308,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,132,S18_2870,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10366,49,100,2,6144.6,1/10/2005 0:00,Shipped,1,1,2005,Classic Cars,132,S18_2870,Royale Belge,(071) 23 67 2555,"Boulevard Tirou, 255",,Charleroi,,B-6000,Belgium,EMEA,Cartrain,Pascale,Medium
10379,29,100,5,5127.2,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,132,S18_2870,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10407,41,100,12,6386.16,4/22/2005 0:00,On Hold,2,4,2005,Classic Cars,132,S18_2870,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10419,55,100,2,7695.6,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,132,S18_2870,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Large
10103,27,83.07,12,2242.89,1/29/2003 0:00,Shipped,1,1,2003,Vintage Cars,101,S18_2949,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10112,23,100,2,2539.89,3/24/2003 0:00,Shipped,1,3,2003,Vintage Cars,101,S18_2949,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Small
10126,31,90.17,12,2795.27,5/28/2003 0:00,Shipped,2,5,2003,Vintage Cars,101,S18_2949,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10139,46,100,1,5545.76,7/16/2003 0:00,Shipped,3,7,2003,Vintage Cars,101,S18_2949,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10150,47,91.18,9,4285.46,9/19/2003 0:00,Shipped,3,9,2003,Vintage Cars,101,S18_2949,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10163,31,100,2,3329.09,10/20/2003 0:00,Shipped,4,10,2003,Vintage Cars,101,S18_2949,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10174,46,100,5,5592.22,11/6/2003 0:00,Shipped,4,11,2003,Vintage Cars,101,S18_2949,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Medium
10183,37,89.15,9,3298.55,11/13/2003 0:00,Shipped,4,11,2003,Vintage Cars,101,S18_2949,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Medium
10193,28,93.21,1,2609.88,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,101,S18_2949,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10206,37,90.17,7,3336.29,12/5/2003 0:00,Shipped,4,12,2003,Vintage Cars,101,S18_2949,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10215,49,100,4,5510.05,1/29/2004 0:00,Shipped,1,1,2004,Vintage Cars,101,S18_2949,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Medium
10228,24,100,3,2504.4,3/10/2004 0:00,Shipped,1,3,2004,Vintage Cars,101,S18_2949,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Small
10244,30,100,1,3525.6,4/29/2004 0:00,Shipped,2,4,2004,Vintage Cars,101,S18_2949,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10257,50,88.14,1,4407,6/14/2004 0:00,Shipped,2,6,2004,Vintage Cars,101,S18_2949,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10270,31,96.24,10,2983.44,7/19/2004 0:00,Shipped,3,7,2004,Vintage Cars,101,S18_2949,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10280,46,100,3,5126.24,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,101,S18_2949,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10291,47,100,12,5713.79,9/8/2004 0:00,Shipped,3,9,2004,Vintage Cars,101,S18_2949,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10304,46,100,7,4613.8,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,101,S18_2949,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Medium
10312,37,100,4,3711.1,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,101,S18_2949,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10322,33,100,12,3524.73,11/4/2004 0:00,Shipped,4,11,2004,Vintage Cars,101,S18_2949,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10333,31,90.17,5,2795.27,11/18/2004 0:00,Shipped,4,11,2004,Vintage Cars,101,S18_2949,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10347,48,100,9,4814.4,11/29/2004 0:00,Shipped,4,11,2004,Vintage Cars,101,S18_2949,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10357,41,87.13,6,3572.33,12/10/2004 0:00,Shipped,4,12,2004,Vintage Cars,101,S18_2949,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10369,42,100,1,4581.36,1/20/2005 0:00,Shipped,1,1,2005,Vintage Cars,101,S18_2949,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10381,41,100,8,4319.76,2/17/2005 0:00,Shipped,1,2,2005,Vintage Cars,101,S18_2949,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10391,32,45.25,6,1448,3/9/2005 0:00,Shipped,1,3,2005,Vintage Cars,101,S18_2949,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10423,10,88.14,1,881.4,5/30/2005 0:00,In Process,2,5,2005,Vintage Cars,101,S18_2949,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10103,35,57.46,14,2011.1,1/29/2003 0:00,Shipped,1,1,2003,Vintage Cars,62,S18_2957,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10111,28,64.33,2,1801.24,3/25/2003 0:00,Shipped,1,3,2003,Vintage Cars,62,S18_2957,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10126,46,73.7,14,3390.2,5/28/2003 0:00,Shipped,2,5,2003,Vintage Cars,62,S18_2957,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10139,20,71.2,3,1424,7/16/2003 0:00,Shipped,3,7,2003,Vintage Cars,62,S18_2957,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10150,30,49.97,11,1499.1,9/19/2003 0:00,Shipped,3,9,2003,Vintage Cars,62,S18_2957,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10163,48,69.96,4,3358.08,10/20/2003 0:00,Shipped,4,10,2003,Vintage Cars,62,S18_2957,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10173,28,53.72,2,1504.16,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,62,S18_2957,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10183,39,68.08,11,2655.12,11/13/2003 0:00,Shipped,4,11,2003,Vintage Cars,62,S18_2957,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10193,24,51.84,3,1244.16,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,62,S18_2957,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10206,28,67.46,9,1888.88,12/5/2003 0:00,Shipped,4,12,2003,Vintage Cars,62,S18_2957,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10215,31,58.71,6,1820.01,1/29/2004 0:00,Shipped,1,1,2004,Vintage Cars,62,S18_2957,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Small
10228,45,63.71,5,2866.95,3/10/2004 0:00,Shipped,1,3,2004,Vintage Cars,62,S18_2957,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Small
10244,24,58.09,3,1394.16,4/29/2004 0:00,Shipped,2,4,2004,Vintage Cars,62,S18_2957,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10257,49,53.72,3,2632.28,6/14/2004 0:00,Shipped,2,6,2004,Vintage Cars,62,S18_2957,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10269,32,63.08,1,2018.56,7/16/2004 0:00,Shipped,3,7,2004,Vintage Cars,62,S18_2957,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10280,43,68.71,5,2954.53,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,62,S18_2957,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10291,37,50.59,14,1871.83,9/8/2004 0:00,Shipped,3,9,2004,Vintage Cars,62,S18_2957,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10304,24,64.96,9,1559.04,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,62,S18_2957,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Small
10312,35,53.72,6,1880.2,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,62,S18_2957,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10322,41,29.87,13,1224.67,11/4/2004 0:00,Shipped,4,11,2004,Vintage Cars,62,S18_2957,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10332,26,100,17,2979.08,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,62,S18_2957,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10347,34,64.96,10,2208.64,11/29/2004 0:00,Shipped,4,11,2004,Vintage Cars,62,S18_2957,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10357,49,70.58,5,3458.42,12/10/2004 0:00,Shipped,4,12,2004,Vintage Cars,62,S18_2957,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10369,28,44.21,6,1237.88,1/20/2005 0:00,Shipped,1,1,2005,Vintage Cars,62,S18_2957,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10381,40,68.08,4,2723.2,2/17/2005 0:00,Shipped,1,2,2005,Vintage Cars,62,S18_2957,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10392,37,59.96,3,2218.52,3/10/2005 0:00,Shipped,1,3,2005,Vintage Cars,62,S18_2957,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Small
10423,31,53.72,3,1665.32,5/30/2005 0:00,In Process,2,5,2005,Vintage Cars,62,S18_2957,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10106,41,83.44,18,3421.04,2/17/2003 0:00,Shipped,1,2,2003,Ships,86,S18_3029,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10119,21,89.46,9,1878.66,4/28/2003 0:00,Shipped,2,4,2003,Ships,86,S18_3029,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10130,40,96.34,2,3853.6,6/16/2003 0:00,Shipped,2,6,2003,Ships,86,S18_3029,Auto-Moto Classics Inc.,6175558428,16780 Pompton St.,,Brickhaven,MA,58339,USA,NA,Taylor,Leslie,Medium
10143,46,74.84,13,3442.64,8/10/2003 0:00,Shipped,3,8,2003,Ships,86,S18_3029,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10155,44,79.14,11,3482.16,10/6/2003 0:00,Shipped,4,10,2003,Ships,86,S18_3029,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10167,46,73.12,7,3363.52,10/23/2003 0:00,Cancelled,4,10,2003,Ships,86,S18_3029,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10178,41,81.72,10,3350.52,11/8/2003 0:00,Shipped,4,11,2003,Ships,86,S18_3029,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10186,32,89.46,7,2862.72,11/14/2003 0:00,Shipped,4,11,2003,Ships,86,S18_3029,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Small
10197,46,87.74,4,4036.04,11/26/2003 0:00,Shipped,4,11,2003,Ships,86,S18_3029,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10209,28,100,6,2817.92,1/9/2004 0:00,Shipped,1,1,2004,Ships,86,S18_3029,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Small
10222,49,94.62,10,4636.38,2/19/2004 0:00,Shipped,1,2,2004,Ships,86,S18_3029,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10248,21,73.98,1,1553.58,5/7/2004 0:00,Cancelled,2,5,2004,Ships,86,S18_3029,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10262,32,84.3,15,2697.6,6/24/2004 0:00,Cancelled,2,6,2004,Ships,86,S18_3029,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10273,34,98.06,2,3334.04,7/21/2004 0:00,Shipped,3,7,2004,Ships,86,S18_3029,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10283,21,98.06,4,2059.26,8/20/2004 0:00,Shipped,3,8,2004,Ships,86,S18_3029,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10296,21,96.34,13,2023.14,9/15/2004 0:00,Shipped,3,9,2004,Ships,86,S18_3029,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10307,31,83.44,7,2586.64,10/14/2004 0:00,Shipped,4,10,2004,Ships,86,S18_3029,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10316,21,94.62,15,1987.02,11/1/2004 0:00,Shipped,4,11,2004,Ships,86,S18_3029,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10327,25,45.86,5,1146.5,11/10/2004 0:00,Resolved,4,11,2004,Ships,86,S18_3029,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10338,28,82.58,3,2312.24,11/22/2004 0:00,Shipped,4,11,2004,Ships,86,S18_3029,Royale Belge,(071) 23 67 2555,"Boulevard Tirou, 255",,Charleroi,,B-6000,Belgium,EMEA,Cartrain,Pascale,Small
10350,43,64.97,6,2793.71,12/2/2004 0:00,Shipped,4,12,2004,Ships,86,S18_3029,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10373,22,86.74,5,1908.28,1/31/2005 0:00,Shipped,1,1,2005,Ships,86,S18_3029,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10386,37,93.01,5,3441.37,3/1/2005 0:00,Resolved,1,3,2005,Ships,86,S18_3029,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10398,28,72.26,18,2023.28,3/30/2005 0:00,Shipped,1,3,2005,Ships,86,S18_3029,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10400,30,74.84,7,2245.2,4/1/2005 0:00,Shipped,2,4,2005,Ships,86,S18_3029,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10414,44,73.98,1,3255.12,5/6/2005 0:00,On Hold,2,5,2005,Ships,86,S18_3029,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10103,25,100,13,2539.5,1/29/2003 0:00,Shipped,1,1,2003,Vintage Cars,104,S18_3136,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10111,43,100,1,4818.15,3/25/2003 0:00,Shipped,1,3,2003,Vintage Cars,104,S18_3136,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Medium
10126,30,97.39,13,2921.7,5/28/2003 0:00,Shipped,2,5,2003,Vintage Cars,104,S18_3136,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10139,20,90.06,2,1801.2,7/16/2003 0:00,Shipped,3,7,2003,Vintage Cars,104,S18_3136,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10150,26,100,10,2804.36,9/19/2003 0:00,Shipped,3,9,2003,Vintage Cars,104,S18_3136,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10163,40,100,3,4900.8,10/20/2003 0:00,Shipped,4,10,2003,Vintage Cars,104,S18_3136,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10173,31,89.01,1,2759.31,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,104,S18_3136,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10183,22,100,10,2488.2,11/13/2003 0:00,Shipped,4,11,2003,Vintage Cars,104,S18_3136,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10193,23,100,2,2769.89,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,104,S18_3136,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10206,30,100,8,3581.4,12/5/2003 0:00,Shipped,4,12,2003,Vintage Cars,104,S18_3136,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10215,49,100,5,5285.14,1/29/2004 0:00,Shipped,1,1,2004,Vintage Cars,104,S18_3136,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Medium
10228,31,100,4,3181.53,3/10/2004 0:00,Shipped,1,3,2004,Vintage Cars,104,S18_3136,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Medium
10244,29,100,2,3340.51,4/29/2004 0:00,Shipped,2,4,2004,Vintage Cars,104,S18_3136,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10257,37,84.82,2,3138.34,6/14/2004 0:00,Shipped,2,6,2004,Vintage Cars,104,S18_3136,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10270,38,100,11,4775.08,7/19/2004 0:00,Shipped,3,7,2004,Vintage Cars,104,S18_3136,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10280,29,100,4,3006.43,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,104,S18_3136,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10291,23,100,13,2866.26,9/8/2004 0:00,Shipped,3,9,2004,Vintage Cars,104,S18_3136,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10304,26,85.87,8,2232.62,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,104,S18_3136,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Small
10312,38,100,5,4457.02,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,104,S18_3136,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10322,48,47.04,7,2257.92,11/4/2004 0:00,Shipped,4,11,2004,Vintage Cars,104,S18_3136,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10332,40,39.8,18,1592,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,104,S18_3136,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10347,45,100,11,4948.2,11/29/2004 0:00,Shipped,4,11,2004,Vintage Cars,104,S18_3136,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10357,44,100,4,5160.76,12/10/2004 0:00,Shipped,4,12,2004,Vintage Cars,104,S18_3136,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10369,21,94.22,5,1978.62,1/20/2005 0:00,Shipped,1,1,2005,Vintage Cars,104,S18_3136,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10381,35,100,5,4288.2,2/17/2005 0:00,Shipped,1,2,2005,Vintage Cars,104,S18_3136,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10392,29,86.92,2,2520.68,3/10/2005 0:00,Shipped,1,3,2005,Vintage Cars,104,S18_3136,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Small
10423,21,84.82,2,1781.22,5/30/2005 0:00,In Process,2,5,2005,Vintage Cars,104,S18_3136,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10105,22,100,11,3065.04,2/11/2003 0:00,Shipped,1,2,2003,Vintage Cars,136,S18_3140,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10117,26,100,5,3551.34,4/16/2003 0:00,Shipped,2,4,2003,Vintage Cars,136,S18_3140,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10128,41,100,2,5544.02,6/6/2003 0:00,Shipped,2,6,2003,Vintage Cars,136,S18_3140,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10142,47,100,8,6034.33,8/8/2003 0:00,Shipped,3,8,2003,Vintage Cars,136,S18_3140,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10153,31,100,7,3641.57,9/28/2003 0:00,Shipped,3,9,2003,Vintage Cars,136,S18_3140,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10166,43,100,2,6930.74,10/21/2003 0:00,Shipped,4,10,2003,Vintage Cars,136,S18_3140,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10177,23,100,9,3675.63,11/7/2003 0:00,Shipped,4,11,2003,Vintage Cars,136,S18_3140,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Medium
10185,28,100,9,3442.04,11/14/2003 0:00,Shipped,4,11,2003,Vintage Cars,136,S18_3140,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10196,49,100,1,6893.81,11/26/2003 0:00,Shipped,4,11,2003,Vintage Cars,136,S18_3140,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10208,24,100,9,2622.48,1/2/2004 0:00,Shipped,1,1,2004,Vintage Cars,136,S18_3140,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10221,33,100,3,4417.38,2/18/2004 0:00,Shipped,1,2,2004,Vintage Cars,136,S18_3140,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10232,22,100,6,3606.02,3/20/2004 0:00,Shipped,1,3,2004,Vintage Cars,136,S18_3140,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10248,32,100,12,3802.56,5/7/2004 0:00,Cancelled,2,5,2004,Vintage Cars,136,S18_3140,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10273,40,100,13,5026.4,7/21/2004 0:00,Shipped,3,7,2004,Vintage Cars,136,S18_3140,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10282,43,100,1,6695.53,8/20/2004 0:00,Shipped,3,8,2004,Vintage Cars,136,S18_3140,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10293,24,100,4,2819.28,9/9/2004 0:00,Shipped,3,9,2004,Vintage Cars,136,S18_3140,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10306,32,100,9,3759.04,10/14/2004 0:00,Shipped,4,10,2004,Vintage Cars,136,S18_3140,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10314,20,100,1,2731.8,10/22/2004 0:00,Shipped,4,10,2004,Vintage Cars,136,S18_3140,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10325,24,69.12,9,1658.88,11/5/2004 0:00,Shipped,4,11,2004,Vintage Cars,136,S18_3140,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10336,48,100,12,5778.24,11/20/2004 0:00,Shipped,4,11,2004,Vintage Cars,136,S18_3140,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10350,44,100,1,5191.12,12/2/2004 0:00,Shipped,4,12,2004,Vintage Cars,136,S18_3140,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10372,28,100,3,3862.88,1/26/2005 0:00,Shipped,1,1,2005,Vintage Cars,136,S18_3140,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10383,24,61.52,9,1476.48,2/22/2005 0:00,Shipped,1,2,2005,Vintage Cars,136,S18_3140,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10396,33,100,2,5273.73,3/23/2005 0:00,Shipped,1,3,2005,Vintage Cars,136,S18_3140,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10414,41,100,12,4872.03,5/6/2005 0:00,On Hold,2,5,2005,Vintage Cars,136,S18_3140,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10104,23,100,13,4556.99,1/31/2003 0:00,Shipped,1,1,2003,Classic Cars,169,S18_3232,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10109,46,100,5,8257,3/10/2003 0:00,Shipped,1,3,2003,Classic Cars,169,S18_3232,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Large
10114,48,100,4,8209.44,4/1/2003 0:00,Shipped,2,4,2003,Classic Cars,169,S18_3232,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Large
10122,25,100,3,3598.5,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,169,S18_3232,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Medium
10127,22,100,15,3837.24,6/3/2003 0:00,Shipped,2,6,2003,Classic Cars,169,S18_3232,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10136,41,100,3,8331.61,7/4/2003 0:00,Shipped,3,7,2003,Classic Cars,169,S18_3232,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Large
10141,34,100,9,4836.5,8/1/2003 0:00,Shipped,3,8,2003,Classic Cars,169,S18_3232,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10148,32,100,14,5418.88,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,169,S18_3232,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10151,21,100,7,3734.01,9/21/2003 0:00,Shipped,3,9,2003,Classic Cars,169,S18_3232,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10160,20,100,1,3996.4,10/11/2003 0:00,Shipped,4,10,2003,Classic Cars,169,S18_3232,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Medium
10165,47,100,16,8754.69,10/22/2003 0:00,Shipped,4,10,2003,Classic Cars,169,S18_3232,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Large
10171,39,100,3,5481.45,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,169,S18_3232,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10175,29,100,5,4419.89,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,169,S18_3232,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10181,45,100,7,6324.75,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,169,S18_3232,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10184,28,100,10,4409.72,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,169,S18_3232,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Medium
10192,26,100,12,3918.46,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,169,S18_3232,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10195,50,100,10,7620.5,11/25/2003 0:00,Shipped,4,11,2003,Classic Cars,169,S18_3232,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Large
10203,48,100,1,8291.04,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,169,S18_3232,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10207,25,100,11,3937.25,12/9/2003 0:00,Shipped,4,12,2003,Classic Cars,169,S18_3232,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Medium
10212,40,100,11,5554.4,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,169,S18_3232,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10225,43,100,2,6407.86,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,169,S18_3232,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10229,22,100,5,4172.52,3/11/2004 0:00,Shipped,1,3,2004,Classic Cars,169,S18_3232,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10239,47,100,1,7083.37,4/12/2004 0:00,Shipped,2,4,2004,Classic Cars,169,S18_3232,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Large
10246,36,100,9,7132.68,5/5/2004 0:00,Shipped,2,5,2004,Classic Cars,169,S18_3232,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10253,40,100,6,6773.6,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,169,S18_3232,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10259,27,100,8,3657.69,6/15/2004 0:00,Shipped,2,6,2004,Classic Cars,169,S18_3232,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10266,29,100,7,4812.55,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,169,S18_3232,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10271,20,100,9,3928.6,7/20/2004 0:00,Shipped,3,7,2004,Classic Cars,169,S18_3232,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10278,42,100,7,6401.22,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,169,S18_3232,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10281,25,100,5,4191.25,8/19/2004 0:00,Shipped,3,8,2004,Classic Cars,169,S18_3232,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10287,36,100,5,5852.52,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,169,S18_3232,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10292,21,100,12,2844.87,9/8/2004 0:00,Shipped,3,9,2004,Classic Cars,169,S18_3232,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10301,23,100,9,4011.66,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,169,S18_3232,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Medium
10305,37,100,9,7455.87,10/13/2004 0:00,Shipped,4,10,2004,Classic Cars,169,S18_3232,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Large
10310,48,100,3,8940.96,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,169,S18_3232,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Large
10313,25,100,3,4572.25,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,169,S18_3232,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10321,33,100,11,5700.09,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,169,S18_3232,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10324,27,100,12,3155.49,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,169,S18_3232,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10331,27,100,11,4170.69,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,169,S18_3232,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10334,20,100,3,2878.8,11/19/2004 0:00,On Hold,4,11,2004,Classic Cars,169,S18_3232,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Small
10342,30,100,4,5029.5,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,169,S18_3232,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10349,48,100,6,7396.8,12/1/2004 0:00,Shipped,4,12,2004,Classic Cars,169,S18_3232,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Large
10358,32,93.49,12,2991.68,12/10/2004 0:00,Shipped,4,12,2004,Classic Cars,169,S18_3232,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10366,34,100,1,6275.72,1/10/2005 0:00,Shipped,1,1,2005,Classic Cars,169,S18_3232,Royale Belge,(071) 23 67 2555,"Boulevard Tirou, 255",,Charleroi,,B-6000,Belgium,EMEA,Cartrain,Pascale,Medium
10370,27,56.85,9,1534.95,1/20/2005 0:00,Shipped,1,1,2005,Classic Cars,169,S18_3232,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10377,39,100,3,7264.53,2/9/2005 0:00,Shipped,1,2,2005,Classic Cars,169,S18_3232,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Large
10383,47,100,6,6869.05,2/22/2005 0:00,Shipped,1,2,2005,Classic Cars,169,S18_3232,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10394,22,100,5,3353.02,3/15/2005 0:00,Shipped,1,3,2005,Classic Cars,169,S18_3232,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10405,55,100,1,8289.05,4/14/2005 0:00,Shipped,2,4,2005,Classic Cars,169,S18_3232,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Large
10412,60,100,9,11887.8,5/3/2005 0:00,Shipped,2,5,2005,Classic Cars,169,S18_3232,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10419,35,100,6,5926.9,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,169,S18_3232,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10425,28,100,8,3793.16,5/31/2005 0:00,In Process,2,5,2005,Classic Cars,169,S18_3232,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10105,38,100,13,4330.1,2/11/2003 0:00,Shipped,1,2,2003,Trains,100,S18_3259,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10117,21,95.8,7,2011.8,4/16/2003 0:00,Shipped,2,4,2003,Trains,100,S18_3259,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10128,41,100,4,4837.18,6/6/2003 0:00,Shipped,2,6,2003,Trains,100,S18_3259,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10142,22,97.81,10,2151.82,8/8/2003 0:00,Shipped,3,8,2003,Trains,100,S18_3259,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10153,29,88.74,9,2573.46,9/28/2003 0:00,Shipped,3,9,2003,Trains,100,S18_3259,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10165,50,100,1,5344.5,10/22/2003 0:00,Shipped,4,10,2003,Trains,100,S18_3259,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10177,29,100,11,3070.52,11/7/2003 0:00,Shipped,4,11,2003,Trains,100,S18_3259,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Medium
10185,49,80.67,11,3952.83,11/14/2003 0:00,Shipped,4,11,2003,Trains,100,S18_3259,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10196,35,100,3,3564.75,11/26/2003 0:00,Shipped,4,11,2003,Trains,100,S18_3259,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10208,48,100,11,5614.56,1/2/2004 0:00,Shipped,1,1,2004,Trains,100,S18_3259,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10221,23,80.67,5,1855.41,2/18/2004 0:00,Shipped,1,2,2004,Trains,100,S18_3259,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10232,48,95.8,8,4598.4,3/20/2004 0:00,Shipped,1,3,2004,Trains,100,S18_3259,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10248,42,100,14,5082.42,5/7/2004 0:00,Cancelled,2,5,2004,Trains,100,S18_3259,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10273,47,100,15,5450.59,7/21/2004 0:00,Shipped,3,7,2004,Trains,100,S18_3259,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10282,36,100,3,4174.92,8/20/2004 0:00,Shipped,3,8,2004,Trains,100,S18_3259,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10293,22,100,6,2418.24,9/9/2004 0:00,Shipped,3,9,2004,Trains,100,S18_3259,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10306,40,91.76,11,3670.4,10/14/2004 0:00,Shipped,4,10,2004,Trains,100,S18_3259,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10314,23,100,3,2481.7,10/22/2004 0:00,Shipped,4,10,2004,Trains,100,S18_3259,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10326,32,100,6,3807.68,11/9/2004 0:00,Shipped,4,11,2004,Trains,100,S18_3259,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10336,21,100,7,2230.41,11/20/2004 0:00,Shipped,4,11,2004,Trains,100,S18_3259,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Small
10350,41,93.04,2,3814.64,12/2/2004 0:00,Shipped,4,12,2004,Trains,100,S18_3259,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10372,25,84.71,5,2117.75,1/26/2005 0:00,Shipped,1,1,2005,Trains,100,S18_3259,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10383,26,100,12,3340.48,2/22/2005 0:00,Shipped,1,2,2005,Trains,100,S18_3259,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10396,24,89.75,4,2154,3/23/2005 0:00,Shipped,1,3,2005,Trains,100,S18_3259,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10414,48,100,14,5808.48,5/6/2005 0:00,On Hold,2,5,2005,Trains,100,S18_3259,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10108,26,68.35,9,1777.1,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,80,S18_3278,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10122,21,73.17,13,1536.57,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,80,S18_3278,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10135,45,78,10,3510,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,80,S18_3278,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10147,36,86.04,10,3097.44,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,80,S18_3278,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10159,21,81.21,5,1705.41,10/10/2003 0:00,Shipped,4,10,2003,Classic Cars,80,S18_3278,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10169,32,70.76,5,2264.32,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,80,S18_3278,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10181,30,82.82,17,2484.6,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,80,S18_3278,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10191,36,94.88,6,3415.68,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,80,S18_3278,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10203,33,86.04,11,2839.32,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,80,S18_3278,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10211,35,78,5,2730,1/15/2004 0:00,Shipped,1,1,2004,Classic Cars,80,S18_3278,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10225,37,95.69,12,3540.53,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,80,S18_3278,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10238,41,73.17,6,2999.97,4/9/2004 0:00,Shipped,2,4,2004,Classic Cars,80,S18_3278,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10252,20,76.39,2,1527.8,5/26/2004 0:00,Shipped,2,5,2004,Classic Cars,80,S18_3278,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10265,45,86.84,2,3907.8,7/2/2004 0:00,Shipped,3,7,2004,Classic Cars,80,S18_3278,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Medium
10276,38,69.96,6,2658.48,8/2/2004 0:00,Shipped,3,8,2004,Classic Cars,80,S18_3278,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Small
10287,43,70.76,15,3042.68,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,80,S18_3278,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10300,49,78.8,8,3861.2,10/4/2003 0:00,Shipped,4,10,2003,Classic Cars,80,S18_3278,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10310,27,80.41,13,2171.07,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,80,S18_3278,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10319,46,73.98,1,3403.08,11/3/2004 0:00,Shipped,4,11,2004,Classic Cars,80,S18_3278,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Medium
10329,38,59.1,10,2245.8,11/15/2004 0:00,Shipped,4,11,2004,Classic Cars,80,S18_3278,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10342,25,66.74,5,1668.5,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,80,S18_3278,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10363,46,60.3,10,2773.8,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,80,S18_3278,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10378,22,100,4,2464,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,80,S18_3278,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10390,40,100,9,5491.6,3/4/2005 0:00,Shipped,1,3,2005,Classic Cars,80,S18_3278,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10103,46,100,16,4791.82,1/29/2003 0:00,Shipped,1,1,2003,Vintage Cars,99,S18_3320,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10111,39,100,4,4178.85,3/25/2003 0:00,Shipped,1,3,2003,Vintage Cars,99,S18_3320,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Medium
10126,38,82.34,16,3128.92,5/28/2003 0:00,Shipped,2,5,2003,Vintage Cars,99,S18_3320,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10139,30,100,5,3095.4,7/16/2003 0:00,Shipped,3,7,2003,Vintage Cars,99,S18_3320,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10149,42,94.25,2,3958.5,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,99,S18_3320,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Medium
10163,43,100,6,4991.44,10/20/2003 0:00,Shipped,4,10,2003,Vintage Cars,99,S18_3320,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10173,29,95.24,4,2761.96,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,99,S18_3320,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10182,33,86.31,1,2848.23,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,99,S18_3320,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10193,32,79.37,5,2539.84,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,99,S18_3320,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10206,28,87.3,11,2444.4,12/5/2003 0:00,Shipped,4,12,2003,Vintage Cars,99,S18_3320,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10215,41,100,8,4555.92,1/29/2004 0:00,Shipped,1,1,2004,Vintage Cars,99,S18_3320,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Medium
10227,33,100,1,3666.96,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,99,S18_3320,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10244,36,84.33,5,3035.88,4/29/2004 0:00,Shipped,2,4,2004,Vintage Cars,99,S18_3320,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10257,26,89.29,5,2321.54,6/14/2004 0:00,Shipped,2,6,2004,Vintage Cars,99,S18_3320,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10280,34,100,7,3474.46,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,99,S18_3320,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10290,26,96.23,2,2501.98,9/7/2004 0:00,Shipped,3,9,2004,Vintage Cars,99,S18_3320,Auto-Moto Classics Inc.,6175558428,16780 Pompton St.,,Brickhaven,MA,58339,USA,NA,Taylor,Leslie,Small
10304,38,100,11,3958.46,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,99,S18_3320,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Medium
10312,33,100,8,3535.95,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,99,S18_3320,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10323,33,91.27,2,3011.91,11/5/2004 0:00,Shipped,4,11,2004,Vintage Cars,99,S18_3320,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10333,46,100,2,11336.7,11/18/2004 0:00,Shipped,4,11,2004,Vintage Cars,99,S18_3320,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Large
10347,26,100,12,2656.94,11/29/2004 0:00,Shipped,4,11,2004,Vintage Cars,99,S18_3320,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10357,25,100,3,2604.25,12/10/2004 0:00,Shipped,4,12,2004,Vintage Cars,99,S18_3320,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10369,45,73.08,4,3288.6,1/20/2005 0:00,Shipped,1,1,2005,Vintage Cars,99,S18_3320,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10382,50,100,7,8935.5,2/17/2005 0:00,Shipped,1,2,2005,Vintage Cars,99,S18_3320,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10392,36,100,1,4035.96,3/10/2005 0:00,Shipped,1,3,2005,Vintage Cars,99,S18_3320,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Medium
10423,21,89.29,5,1875.09,5/30/2005 0:00,In Process,2,5,2005,Vintage Cars,99,S18_3320,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10108,29,100,8,4049.56,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,146,S18_3482,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10122,21,100,12,2469.39,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,146,S18_3482,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10135,42,100,9,5432.7,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,146,S18_3482,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10147,37,100,9,4405.22,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,146,S18_3482,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10159,25,100,4,3638,10/10/2003 0:00,Shipped,4,10,2003,Classic Cars,146,S18_3482,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10169,36,100,4,4444.92,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,146,S18_3482,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10181,22,100,16,3395.48,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,146,S18_3482,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10191,23,100,5,3414.58,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,146,S18_3482,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10203,32,100,10,5127.04,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,146,S18_3482,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10211,28,100,4,3745.28,1/15/2004 0:00,Shipped,1,1,2004,Classic Cars,146,S18_3482,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10225,27,100,11,4564.08,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,146,S18_3482,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10238,49,100,5,6554.24,4/9/2004 0:00,Shipped,2,4,2004,Classic Cars,146,S18_3482,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10252,41,100,1,6749.83,5/26/2004 0:00,Shipped,2,5,2004,Classic Cars,146,S18_3482,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10265,49,100,1,8427.02,7/2/2004 0:00,Shipped,3,7,2004,Classic Cars,146,S18_3482,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Large
10276,30,100,5,3924.6,8/2/2004 0:00,Shipped,3,8,2004,Classic Cars,146,S18_3482,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Medium
10287,40,100,14,6761.6,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,146,S18_3482,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10300,23,100,7,3786.49,10/4/2003 0:00,Shipped,4,10,2003,Classic Cars,146,S18_3482,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10310,49,100,12,6266.12,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,146,S18_3482,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10320,25,100,5,3491,11/3/2004 0:00,Shipped,4,11,2004,Classic Cars,146,S18_3482,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10330,37,100,3,4405.22,11/16/2004 0:00,Shipped,4,11,2004,Classic Cars,146,S18_3482,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10342,55,100,7,6548.3,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,146,S18_3482,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10355,23,100,7,3177.91,12/7/2004 0:00,Shipped,4,12,2004,Classic Cars,146,S18_3482,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10363,24,100,11,4142.64,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,146,S18_3482,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10378,43,96.49,10,4149.07,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,146,S18_3482,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10390,50,100,1,7397,3/4/2005 0:00,Shipped,1,3,2005,Classic Cars,146,S18_3482,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10109,47,100,2,6241.6,3/10/2003 0:00,Shipped,1,3,2003,Classic Cars,141,S18_3685,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10123,34,100,4,5331.88,5/20/2003 0:00,Shipped,2,5,2003,Classic Cars,141,S18_3685,Atelier graphique,40.32.2555,"54, rue Royale",,Nantes,,44000,France,EMEA,Schmitt,Carine,Medium
10137,31,100,4,5124.3,7/10/2003 0:00,Shipped,3,7,2003,Classic Cars,141,S18_3685,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10148,28,100,11,3639.44,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,141,S18_3685,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10161,36,100,10,5544,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,141,S18_3685,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10172,48,100,8,5493.12,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,141,S18_3685,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10181,39,100,4,5785.26,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,141,S18_3685,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10192,45,100,9,5340.6,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,141,S18_3685,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10204,35,100,15,5735.8,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,141,S18_3685,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10212,45,100,8,6357.6,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,141,S18_3685,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10226,46,100,6,7343.9,2/26/2004 0:00,Shipped,1,2,2004,Classic Cars,141,S18_3685,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Large
10240,37,100,1,5959.22,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,141,S18_3685,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Medium
10253,31,100,3,4029.38,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,141,S18_3685,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10266,33,100,4,5035.14,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,141,S18_3685,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10278,31,100,4,4116.8,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,141,S18_3685,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10287,27,100,2,4310.55,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,141,S18_3685,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10301,39,100,6,6446.7,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,141,S18_3685,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Medium
10311,32,100,11,3616.64,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,141,S18_3685,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10321,28,100,8,4232.76,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,141,S18_3685,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10331,26,67.91,12,1765.66,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,141,S18_3685,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Small
10343,44,84.88,2,3734.72,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,141,S18_3685,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10367,46,100,6,4808.38,1/12/2005 0:00,Resolved,1,1,2005,Classic Cars,141,S18_3685,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10379,32,70.83,4,2266.56,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,141,S18_3685,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10406,65,100,1,10468.9,4/15/2005 0:00,Disputed,2,4,2005,Classic Cars,141,S18_3685,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Large
10419,43,100,3,5589.14,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,141,S18_3685,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10108,43,67.77,12,2914.11,3/3/2003 0:00,Shipped,1,3,2003,Motorcycles,62,S18_3782,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10122,35,49.74,16,1740.9,5/8/2003 0:00,Shipped,2,5,2003,Motorcycles,62,S18_3782,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10135,45,50.36,13,2266.2,7/2/2003 0:00,Shipped,3,7,2003,Motorcycles,62,S18_3782,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10146,47,67.14,2,3155.58,9/3/2003 0:00,Shipped,3,9,2003,Motorcycles,62,S18_3782,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10159,21,64.66,8,1357.86,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,62,S18_3782,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10169,38,68.39,8,2598.82,11/4/2003 0:00,Shipped,4,11,2003,Motorcycles,62,S18_3782,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10180,21,50.36,3,1057.56,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,62,S18_3782,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10191,43,72.74,9,3127.82,11/20/2003 0:00,Shipped,4,11,2003,Motorcycles,62,S18_3782,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10211,46,54.09,8,2488.14,1/15/2004 0:00,Shipped,1,1,2004,Motorcycles,62,S18_3782,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10224,38,58.44,1,2220.72,2/21/2004 0:00,Shipped,1,2,2004,Motorcycles,62,S18_3782,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10237,26,52.22,1,1357.72,4/5/2004 0:00,Shipped,2,4,2004,Motorcycles,62,S18_3782,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10252,31,52.84,5,1638.04,5/26/2004 0:00,Shipped,2,5,2004,Motorcycles,62,S18_3782,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10264,48,54.71,3,2626.08,6/30/2004 0:00,Shipped,2,6,2004,Motorcycles,62,S18_3782,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10276,33,50.36,9,1661.88,8/2/2004 0:00,Shipped,3,8,2004,Motorcycles,62,S18_3782,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Small
10286,38,57.2,1,2173.6,8/28/2004 0:00,Shipped,3,8,2004,Motorcycles,62,S18_3782,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Small
10299,39,55.95,3,2182.05,9/30/2004 0:00,Shipped,3,9,2004,Motorcycles,62,S18_3782,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10310,42,67.14,16,2819.88,10/16/2004 0:00,Shipped,4,10,2004,Motorcycles,62,S18_3782,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10319,44,59.06,4,2598.64,11/3/2004 0:00,Shipped,4,11,2004,Motorcycles,62,S18_3782,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Small
10330,29,69.63,2,2019.27,11/16/2004 0:00,Shipped,4,11,2004,Motorcycles,62,S18_3782,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10342,26,55.95,8,1454.7,11/24/2004 0:00,Shipped,4,11,2004,Motorcycles,62,S18_3782,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10355,31,53.47,1,1657.57,12/7/2004 0:00,Shipped,4,12,2004,Motorcycles,62,S18_3782,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10363,32,89.12,12,2851.84,1/6/2005 0:00,Shipped,1,1,2005,Motorcycles,62,S18_3782,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10378,28,100,9,4609.64,2/10/2005 0:00,Shipped,1,2,2005,Motorcycles,62,S18_3782,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10390,36,100,2,5079.96,3/4/2005 0:00,Shipped,1,3,2005,Motorcycles,62,S18_3782,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10403,36,52.22,1,1879.92,4/8/2005 0:00,Shipped,2,4,2005,Motorcycles,62,S18_3782,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10106,41,100,17,4774.86,2/17/2003 0:00,Shipped,1,2,2003,Vintage Cars,105,S18_3856,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10119,27,99.52,8,2687.04,4/28/2003 0:00,Shipped,2,4,2003,Vintage Cars,105,S18_3856,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10130,33,100,1,3423.75,6/16/2003 0:00,Shipped,2,6,2003,Vintage Cars,105,S18_3856,Auto-Moto Classics Inc.,6175558428,16780 Pompton St.,,Brickhaven,MA,58339,USA,NA,Taylor,Leslie,Medium
10143,34,100,12,3455.76,8/10/2003 0:00,Shipped,3,8,2003,Vintage Cars,105,S18_3856,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10155,29,100,10,3622.97,10/6/2003 0:00,Shipped,4,10,2003,Vintage Cars,105,S18_3856,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10167,34,100,6,3599.58,10/23/2003 0:00,Cancelled,4,10,2003,Vintage Cars,105,S18_3856,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10178,48,100,9,5386.56,11/8/2003 0:00,Shipped,4,11,2003,Vintage Cars,105,S18_3856,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10186,46,100,6,4918.78,11/14/2003 0:00,Shipped,4,11,2003,Vintage Cars,105,S18_3856,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Medium
10197,22,100,3,2538.8,11/26/2003 0:00,Shipped,4,11,2003,Vintage Cars,105,S18_3856,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10209,20,100,5,2498.6,1/9/2004 0:00,Shipped,1,1,2004,Vintage Cars,105,S18_3856,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Small
10222,45,85.75,9,3858.75,2/19/2004 0:00,Shipped,1,2,2004,Vintage Cars,105,S18_3856,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10249,46,100,5,5600.5,5/8/2004 0:00,Shipped,2,5,2004,Vintage Cars,105,S18_3856,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Medium
10262,34,100,14,4103.46,6/24/2004 0:00,Cancelled,2,6,2004,Vintage Cars,105,S18_3856,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10273,50,85.75,1,4287.5,7/21/2004 0:00,Shipped,3,7,2004,Vintage Cars,105,S18_3856,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10283,46,100,3,5795.54,8/20/2004 0:00,Shipped,3,8,2004,Vintage Cars,105,S18_3856,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10296,22,84.7,12,1863.4,9/15/2004 0:00,Shipped,3,9,2004,Vintage Cars,105,S18_3856,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10307,48,86.81,6,4166.88,10/14/2004 0:00,Shipped,4,10,2004,Vintage Cars,105,S18_3856,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Medium
10316,47,86.81,14,4080.07,11/1/2004 0:00,Shipped,4,11,2004,Vintage Cars,105,S18_3856,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10328,34,100,6,3815.48,11/12/2004 0:00,Shipped,4,11,2004,Vintage Cars,105,S18_3856,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10338,45,100,2,5526.45,11/22/2004 0:00,Shipped,4,11,2004,Vintage Cars,105,S18_3856,Royale Belge,(071) 23 67 2555,"Boulevard Tirou, 255",,Charleroi,,B-6000,Belgium,EMEA,Cartrain,Pascale,Medium
10351,20,100,2,3374.6,12/3/2004 0:00,Shipped,4,12,2004,Vintage Cars,105,S18_3856,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10373,50,60.49,6,3024.5,1/31/2005 0:00,Shipped,1,1,2005,Vintage Cars,105,S18_3856,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10386,22,57.55,6,1266.1,3/1/2005 0:00,Resolved,1,3,2005,Vintage Cars,105,S18_3856,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10398,45,100,17,4811.85,3/30/2005 0:00,Shipped,1,3,2005,Vintage Cars,105,S18_3856,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10400,58,100,6,7307.42,4/1/2005 0:00,Shipped,2,4,2005,Vintage Cars,105,S18_3856,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Large
10415,51,100,5,6209.25,5/9/2005 0:00,Disputed,2,5,2005,Vintage Cars,105,S18_3856,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Medium
10104,38,100,3,5348.5,1/31/2003 0:00,Shipped,1,1,2003,Classic Cars,143,S18_4027,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10117,22,100,12,2780.58,4/16/2003 0:00,Shipped,2,4,2003,Classic Cars,143,S18_4027,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10127,25,100,5,3447,6/3/2003 0:00,Shipped,2,6,2003,Classic Cars,143,S18_4027,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10142,24,100,15,3791.52,8/8/2003 0:00,Shipped,3,8,2003,Classic Cars,143,S18_4027,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10152,35,100,1,4524.1,9/25/2003 0:00,Shipped,3,9,2003,Classic Cars,143,S18_4027,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Medium
10165,28,100,6,3337.6,10/22/2003 0:00,Shipped,4,10,2003,Classic Cars,143,S18_4027,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10176,36,100,5,5532.12,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,143,S18_4027,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10185,39,100,16,5096.91,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,143,S18_4027,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10196,27,100,8,4537.08,11/26/2003 0:00,Shipped,4,11,2003,Classic Cars,143,S18_4027,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10207,40,100,1,6146.8,12/9/2003 0:00,Shipped,4,12,2003,Classic Cars,143,S18_4027,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Medium
10220,50,100,5,8258,2/12/2004 0:00,Shipped,1,2,2004,Classic Cars,143,S18_4027,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Large
10230,42,100,3,7238.28,3/15/2004 0:00,Shipped,1,3,2004,Classic Cars,143,S18_4027,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Large
10247,48,100,5,6756,5/5/2004 0:00,Shipped,2,5,2004,Classic Cars,143,S18_4027,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10272,25,100,5,3734,7/20/2004 0:00,Shipped,3,7,2004,Classic Cars,143,S18_4027,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10282,31,100,8,4674.8,8/20/2004 0:00,Shipped,3,8,2004,Classic Cars,143,S18_4027,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10292,44,100,2,7140.76,9/8/2004 0:00,Shipped,3,9,2004,Classic Cars,143,S18_4027,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Large
10306,23,100,16,3600.65,10/14/2004 0:00,Shipped,4,10,2004,Classic Cars,143,S18_4027,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10314,29,100,8,4206.74,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,143,S18_4027,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10324,49,100,13,5379.71,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,143,S18_4027,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10337,36,100,3,5679.36,11/21/2004 0:00,Shipped,4,11,2004,Classic Cars,143,S18_4027,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10349,34,100,5,4394.84,12/1/2004 0:00,Shipped,4,12,2004,Classic Cars,143,S18_4027,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10358,25,100,13,2528.25,12/10/2004 0:00,Shipped,4,12,2004,Classic Cars,143,S18_4027,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10372,48,100,6,7031.52,1/26/2005 0:00,Shipped,1,1,2005,Classic Cars,143,S18_4027,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Large
10383,38,100,1,5340.9,2/22/2005 0:00,Shipped,1,2,2005,Classic Cars,143,S18_4027,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10394,37,100,1,6376.58,3/15/2005 0:00,Shipped,1,3,2005,Classic Cars,143,S18_4027,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10413,49,100,5,6896.75,5/5/2005 0:00,Shipped,2,5,2005,Classic Cars,143,S18_4027,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10100,22,86.51,4,1903.22,1/6/2003 0:00,Shipped,1,1,2003,Vintage Cars,92,S18_4409,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10110,28,89.27,8,2499.56,3/18/2003 0:00,Shipped,1,3,2003,Vintage Cars,92,S18_4409,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10124,36,85.59,7,3081.24,5/21/2003 0:00,Shipped,2,5,2003,Vintage Cars,92,S18_4409,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10148,34,100,1,3598.22,9/11/2003 0:00,Shipped,3,9,2003,Vintage Cars,92,S18_4409,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10162,39,100,10,3912.09,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,92,S18_4409,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10173,21,75.46,14,1584.66,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,92,S18_4409,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10182,36,100,11,3942.72,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,92,S18_4409,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10193,24,97.55,15,2341.2,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,92,S18_4409,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10204,29,85.59,5,2482.11,12/2/2003 0:00,Shipped,4,12,2003,Vintage Cars,92,S18_4409,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10213,38,94.79,1,3602.02,1/22/2004 0:00,Shipped,1,1,2004,Vintage Cars,92,S18_4409,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Medium
10227,34,100,11,3566.94,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,92,S18_4409,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10241,42,90.19,3,3787.98,4/13/2004 0:00,Shipped,2,4,2004,Vintage Cars,92,S18_4409,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Medium
10280,35,100,17,3704.05,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,92,S18_4409,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10288,35,80.99,6,2834.65,9/1/2004 0:00,Shipped,3,9,2004,Vintage Cars,92,S18_4409,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10302,38,89.27,2,3392.26,10/6/2003 0:00,Shipped,4,10,2003,Vintage Cars,92,S18_4409,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10311,41,81.91,1,3358.31,10/16/2004 0:00,Shipped,4,10,2004,Vintage Cars,92,S18_4409,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10332,50,100,2,7310,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,92,S18_4409,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Large
10344,21,100,4,2203.11,11/25/2004 0:00,Shipped,4,11,2004,Vintage Cars,92,S18_4409,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10367,43,62.72,8,2696.96,1/12/2005 0:00,Resolved,1,1,2005,Vintage Cars,92,S18_4409,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10380,32,100,1,3376.64,2/16/2005 0:00,Shipped,1,2,2005,Vintage Cars,92,S18_4409,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10407,6,90.19,3,541.14,4/22/2005 0:00,On Hold,2,4,2005,Vintage Cars,92,S18_4409,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10420,66,92.95,6,6134.7,5/29/2005 0:00,In Process,2,5,2005,Vintage Cars,92,S18_4409,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10105,41,82.5,10,3382.5,2/11/2003 0:00,Shipped,1,2,2003,Vintage Cars,87,S18_4522,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10117,23,97.42,4,2240.66,4/16/2003 0:00,Shipped,2,4,2003,Vintage Cars,87,S18_4522,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10128,43,92.16,1,3962.88,6/6/2003 0:00,Shipped,2,6,2003,Vintage Cars,87,S18_4522,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10142,24,70.22,7,1685.28,8/8/2003 0:00,Shipped,3,8,2003,Vintage Cars,87,S18_4522,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10153,22,83.38,6,1834.36,9/28/2003 0:00,Shipped,3,9,2003,Vintage Cars,87,S18_4522,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10166,26,73.73,1,1916.98,10/21/2003 0:00,Shipped,4,10,2003,Vintage Cars,87,S18_4522,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10177,35,74.6,8,2611,11/7/2003 0:00,Shipped,4,11,2003,Vintage Cars,87,S18_4522,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Small
10185,47,77.24,8,3630.28,11/14/2003 0:00,Shipped,4,11,2003,Vintage Cars,87,S18_4522,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10197,50,100,14,5090.5,11/26/2003 0:00,Shipped,4,11,2003,Vintage Cars,87,S18_4522,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10208,45,87.77,8,3949.65,1/2/2004 0:00,Shipped,1,1,2004,Vintage Cars,87,S18_4522,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10221,39,89.53,2,3491.67,2/18/2004 0:00,Shipped,1,2,2004,Vintage Cars,87,S18_4522,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10232,23,89.53,5,2059.19,3/20/2004 0:00,Shipped,1,3,2004,Vintage Cars,87,S18_4522,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10248,42,75.48,11,3170.16,5/7/2004 0:00,Cancelled,2,5,2004,Vintage Cars,87,S18_4522,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10261,20,89.53,9,1790.6,6/17/2004 0:00,Shipped,2,6,2004,Vintage Cars,87,S18_4522,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Small
10273,33,71.09,12,2345.97,7/21/2004 0:00,Shipped,3,7,2004,Vintage Cars,87,S18_4522,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10283,34,100,14,3580.88,8/20/2004 0:00,Shipped,3,8,2004,Vintage Cars,87,S18_4522,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10293,49,100,3,4946.06,9/9/2004 0:00,Shipped,3,9,2004,Vintage Cars,87,S18_4522,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Medium
10306,39,90.4,8,3525.6,10/14/2004 0:00,Shipped,4,10,2004,Vintage Cars,87,S18_4522,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10315,36,100,7,3602.16,10/29/2004 0:00,Shipped,4,10,2004,Vintage Cars,87,S18_4522,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10326,50,86.01,5,4300.5,11/9/2004 0:00,Shipped,4,11,2004,Vintage Cars,87,S18_4522,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10337,29,100,2,4498.19,11/21/2004 0:00,Shipped,4,11,2004,Vintage Cars,87,S18_4522,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10350,30,100,3,3023.1,12/2/2004 0:00,Shipped,4,12,2004,Vintage Cars,87,S18_4522,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10372,41,86.89,7,3562.49,1/26/2005 0:00,Shipped,1,1,2005,Vintage Cars,87,S18_4522,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10383,28,58.58,7,1640.24,2/22/2005 0:00,Shipped,1,2,2005,Vintage Cars,87,S18_4522,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10396,45,100,5,4739.4,3/23/2005 0:00,Shipped,1,3,2005,Vintage Cars,87,S18_4522,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10414,16,75.48,11,1207.68,5/6/2005 0:00,On Hold,2,5,2005,Vintage Cars,87,S18_4522,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10103,36,100,5,4228.2,1/29/2003 0:00,Shipped,1,1,2003,Trucks and Buses,121,S18_4600,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10114,41,100,9,4815.45,4/1/2003 0:00,Shipped,2,4,2003,Trucks and Buses,121,S18_4600,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10126,50,100,5,7083,5/28/2003 0:00,Shipped,2,5,2003,Trucks and Buses,121,S18_4600,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Large
10140,40,100,5,4601.2,7/24/2003 0:00,Shipped,3,7,2003,Trucks and Buses,121,S18_4600,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10150,49,100,2,6467.02,9/19/2003 0:00,Shipped,3,9,2003,Trucks and Buses,121,S18_4600,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10164,45,100,3,5012.55,10/21/2003 0:00,Resolved,4,10,2003,Trucks and Buses,121,S18_4600,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Medium
10175,47,100,10,5121.59,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,121,S18_4600,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10183,21,100,2,2441.04,11/13/2003 0:00,Shipped,4,11,2003,Trucks and Buses,121,S18_4600,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10194,32,100,5,4262.08,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,121,S18_4600,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10207,47,100,16,6658.02,12/9/2003 0:00,Shipped,4,12,2003,Trucks and Buses,121,S18_4600,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Medium
10217,38,100,5,4509.08,2/4/2004 0:00,Shipped,1,2,2004,Trucks and Buses,121,S18_4600,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10229,41,100,10,4716.23,3/11/2004 0:00,Shipped,1,3,2004,Trucks and Buses,121,S18_4600,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10245,21,100,3,2390.22,5/4/2004 0:00,Shipped,2,5,2004,Trucks and Buses,121,S18_4600,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Small
10259,41,100,13,4666.62,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,121,S18_4600,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10270,38,100,3,5383.08,7/19/2004 0:00,Shipped,3,7,2004,Trucks and Buses,121,S18_4600,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10281,25,99.29,10,2482.25,8/19/2004 0:00,Shipped,3,8,2004,Trucks and Buses,121,S18_4600,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10291,48,100,5,5288.64,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,121,S18_4600,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10305,22,99.29,14,2184.38,10/13/2004 0:00,Shipped,4,10,2004,Trucks and Buses,121,S18_4600,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10313,28,100,8,2881.76,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,121,S18_4600,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10323,47,100,1,6203.06,11/5/2004 0:00,Shipped,4,11,2004,Trucks and Buses,121,S18_4600,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10334,49,100,4,6763.47,11/19/2004 0:00,On Hold,4,11,2004,Trucks and Buses,121,S18_4600,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10347,45,100,4,5884.65,11/29/2004 0:00,Shipped,4,11,2004,Trucks and Buses,121,S18_4600,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10357,28,100,2,3559.64,12/10/2004 0:00,Shipped,4,12,2004,Trucks and Buses,121,S18_4600,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10370,29,57.53,6,1668.37,1/20/2005 0:00,Shipped,1,1,2005,Trucks and Buses,121,S18_4600,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10382,39,100,1,4890.6,2/17/2005 0:00,Shipped,1,2,2005,Trucks and Buses,121,S18_4600,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10411,46,100,3,5235.72,5/1/2005 0:00,Shipped,2,5,2005,Trucks and Buses,121,S18_4600,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10425,38,100,13,4325.16,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,121,S18_4600,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10103,41,47.29,9,1938.89,1/29/2003 0:00,Shipped,1,1,2003,Vintage Cars,50,S18_4668,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10113,50,49.81,3,2490.5,3/26/2003 0:00,Shipped,1,3,2003,Vintage Cars,50,S18_4668,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10126,43,53.83,9,2314.69,5/28/2003 0:00,Shipped,2,5,2003,Vintage Cars,50,S18_4668,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10140,29,43.27,9,1254.83,7/24/2003 0:00,Shipped,3,7,2003,Vintage Cars,50,S18_4668,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10150,30,42.76,6,1282.8,9/19/2003 0:00,Shipped,3,9,2003,Vintage Cars,50,S18_4668,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10164,25,53.83,7,1345.75,10/21/2003 0:00,Resolved,4,10,2003,Vintage Cars,50,S18_4668,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Small
10174,49,44.78,2,2194.22,11/6/2003 0:00,Shipped,4,11,2003,Vintage Cars,50,S18_4668,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Small
10183,40,49.3,6,1972,11/13/2003 0:00,Shipped,4,11,2003,Vintage Cars,50,S18_4668,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10194,41,44.78,9,1835.98,11/25/2003 0:00,Shipped,4,11,2003,Vintage Cars,50,S18_4668,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10206,21,53.33,4,1119.93,12/5/2003 0:00,Shipped,4,12,2003,Vintage Cars,50,S18_4668,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10215,46,45.28,1,2082.88,1/29/2004 0:00,Shipped,1,1,2004,Vintage Cars,50,S18_4668,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Small
10229,39,40.25,14,1569.75,3/11/2004 0:00,Shipped,1,3,2004,Vintage Cars,50,S18_4668,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10245,45,59.87,7,2694.15,5/4/2004 0:00,Shipped,2,5,2004,Vintage Cars,50,S18_4668,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Small
10258,21,59.87,4,1257.27,6/15/2004 0:00,Shipped,2,6,2004,Vintage Cars,50,S18_4668,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10270,44,58.36,7,2567.84,7/19/2004 0:00,Shipped,3,7,2004,Vintage Cars,50,S18_4668,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10281,44,59.87,14,2634.28,8/19/2004 0:00,Shipped,3,8,2004,Vintage Cars,50,S18_4668,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10291,29,51.82,9,1502.78,9/8/2004 0:00,Shipped,3,9,2004,Vintage Cars,50,S18_4668,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10304,34,49.3,4,1676.2,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,50,S18_4668,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Small
10312,39,56.85,1,2217.15,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,50,S18_4668,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10324,38,100,6,6832.02,11/5/2004 0:00,Shipped,4,11,2004,Vintage Cars,50,S18_4668,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10333,24,79.86,8,1916.64,11/18/2004 0:00,Shipped,4,11,2004,Vintage Cars,50,S18_4668,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10348,29,100,6,7110.8,11/1/2004 0:00,Shipped,4,11,2004,Vintage Cars,50,S18_4668,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Large
10358,30,100,8,5302.8,12/10/2004 0:00,Shipped,4,12,2004,Vintage Cars,50,S18_4668,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10370,20,100,2,2730,1/20/2005 0:00,Shipped,1,1,2005,Vintage Cars,50,S18_4668,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10382,39,100,2,7827.3,2/17/2005 0:00,Shipped,1,2,2005,Vintage Cars,50,S18_4668,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Large
10411,35,59.87,7,2095.45,5/1/2005 0:00,Shipped,2,5,2005,Vintage Cars,50,S18_4668,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Small
10424,26,59.87,4,1556.62,5/31/2005 0:00,In Process,2,5,2005,Vintage Cars,50,S18_4668,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10108,44,100,11,5565.12,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,148,S18_4721,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10122,28,100,15,3583.16,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,148,S18_4721,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Medium
10135,31,100,12,4705.18,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,148,S18_4721,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10146,29,100,1,4444.54,9/3/2003 0:00,Shipped,3,9,2003,Classic Cars,148,S18_4721,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10159,32,100,7,4618.88,10/10/2003 0:00,Shipped,4,10,2003,Classic Cars,148,S18_4721,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10169,33,100,7,4910.4,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,148,S18_4721,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10180,44,100,2,5565.12,11/11/2003 0:00,Shipped,4,11,2003,Classic Cars,148,S18_4721,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Medium
10191,32,100,8,4237.76,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,148,S18_4721,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10211,41,100,7,5673.58,1/15/2004 0:00,Shipped,1,1,2004,Classic Cars,148,S18_4721,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10225,35,100,14,5260.15,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,148,S18_4721,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10238,44,100,8,6350.96,4/9/2004 0:00,Shipped,2,4,2004,Classic Cars,148,S18_4721,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10252,26,100,4,3559.4,5/26/2004 0:00,Shipped,2,5,2004,Classic Cars,148,S18_4721,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10264,20,100,2,2410.6,6/30/2004 0:00,Shipped,2,6,2004,Classic Cars,148,S18_4721,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10276,48,100,8,5713.92,8/2/2004 0:00,Shipped,3,8,2004,Classic Cars,148,S18_4721,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Medium
10287,34,100,17,4300.32,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,148,S18_4721,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10299,49,100,2,7947.31,9/30/2004 0:00,Shipped,3,9,2004,Classic Cars,148,S18_4721,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Large
10310,40,100,15,5356.8,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,148,S18_4721,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10319,45,100,3,7901.1,11/3/2004 0:00,Shipped,4,11,2004,Classic Cars,148,S18_4721,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Large
10330,50,100,4,6101,11/16/2004 0:00,Shipped,4,11,2004,Classic Cars,148,S18_4721,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10342,38,100,11,6276.46,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,148,S18_4721,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10355,25,100,2,4203.5,12/7/2004 0:00,Shipped,4,12,2004,Classic Cars,148,S18_4721,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10363,28,58.18,13,1629.04,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,148,S18_4721,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10378,49,67.14,8,3289.86,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,148,S18_4721,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10390,49,100,3,6862.94,3/4/2005 0:00,Shipped,1,3,2005,Classic Cars,148,S18_4721,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10110,42,61.29,9,2574.18,3/18/2003 0:00,Shipped,1,3,2003,Classic Cars,71,S18_4933,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10124,23,57.73,8,1327.79,5/21/2003 0:00,Shipped,2,5,2003,Classic Cars,71,S18_4933,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10148,29,81.25,2,2356.25,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,71,S18_4933,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10161,25,80.54,1,2013.5,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,71,S18_4933,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10173,39,71.98,15,2807.22,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,71,S18_4933,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10182,44,69.84,12,3072.96,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,71,S18_4933,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10193,25,76.26,16,1906.5,11/21/2003 0:00,Shipped,4,11,2003,Classic Cars,71,S18_4933,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10204,45,76.26,6,3431.7,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,71,S18_4933,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10213,25,83.39,2,2084.75,1/22/2004 0:00,Shipped,1,1,2004,Classic Cars,71,S18_4933,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Small
10227,37,57.73,12,2136.01,3/2/2004 0:00,Shipped,1,3,2004,Classic Cars,71,S18_4933,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10241,30,66.99,4,2009.7,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,71,S18_4933,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10267,36,75.55,1,2719.8,7/7/2004 0:00,Shipped,3,7,2004,Classic Cars,71,S18_4933,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10279,26,60.58,1,1575.08,8/9/2004 0:00,Shipped,3,8,2004,Classic Cars,71,S18_4933,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10288,23,73.41,7,1688.43,9/1/2004 0:00,Shipped,3,9,2004,Classic Cars,71,S18_4933,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10302,23,72.7,3,1672.1,10/6/2003 0:00,Shipped,4,10,2003,Classic Cars,71,S18_4933,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10311,25,66.99,2,1674.75,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,71,S18_4933,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10332,21,100,3,3472.98,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,71,S18_4933,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10344,26,63.43,5,1649.18,11/25/2004 0:00,Shipped,4,11,2004,Classic Cars,71,S18_4933,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10367,44,85.25,9,3751,1/12/2005 0:00,Resolved,1,1,2005,Classic Cars,71,S18_4933,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10380,24,100,2,4536,2/16/2005 0:00,Shipped,1,2,2005,Classic Cars,71,S18_4933,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10407,66,66.99,4,4421.34,4/22/2005 0:00,On Hold,2,4,2005,Classic Cars,71,S18_4933,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10420,36,57.73,7,2078.28,5/29/2005 0:00,In Process,2,5,2005,Classic Cars,71,S18_4933,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10110,36,85.25,13,3069,3/18/2003 0:00,Shipped,1,3,2003,Classic Cars,73,S24_1046,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10124,22,77.9,12,1713.8,5/21/2003 0:00,Shipped,2,5,2003,Classic Cars,73,S24_1046,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10148,25,60.26,6,1506.5,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,73,S24_1046,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10161,37,72.76,5,2692.12,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,73,S24_1046,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10172,32,75.69,3,2422.08,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,73,S24_1046,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10182,47,74.22,16,3488.34,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,73,S24_1046,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10192,37,69.82,4,2583.34,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,73,S24_1046,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10204,20,62.47,10,1249.4,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,73,S24_1046,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10212,41,82.31,3,3374.71,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,73,S24_1046,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10226,21,60.26,1,1265.46,2/26/2004 0:00,Shipped,1,2,2004,Classic Cars,73,S24_1046,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10241,22,76.43,8,1681.46,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,73,S24_1046,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10267,40,80.1,5,3204,7/7/2004 0:00,Shipped,3,7,2004,Classic Cars,73,S24_1046,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10279,32,74.96,5,2398.72,8/9/2004 0:00,Shipped,3,8,2004,Classic Cars,73,S24_1046,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10288,36,66.14,11,2381.04,9/1/2004 0:00,Shipped,3,9,2004,Classic Cars,73,S24_1046,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10301,27,72.02,1,1944.54,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,73,S24_1046,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10311,26,87.45,6,2273.7,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,73,S24_1046,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10321,30,70.55,3,2116.5,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,73,S24_1046,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10332,23,56.84,4,1307.32,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,73,S24_1046,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10344,29,59.53,7,1726.37,11/25/2004 0:00,Shipped,4,11,2004,Classic Cars,73,S24_1046,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10367,21,60.37,10,1267.77,1/12/2005 0:00,Resolved,1,1,2005,Classic Cars,73,S24_1046,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10380,34,100,3,3441.82,2/16/2005 0:00,Shipped,1,2,2005,Classic Cars,73,S24_1046,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10407,26,76.43,8,1987.18,4/22/2005 0:00,On Hold,2,4,2005,Classic Cars,73,S24_1046,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10420,60,64.67,11,3880.2,5/29/2005 0:00,In Process,2,5,2005,Classic Cars,73,S24_1046,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10104,35,55.49,6,1942.15,1/31/2003 0:00,Shipped,1,1,2003,Classic Cars,57,S24_1444,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10115,47,69.36,2,3259.92,4/4/2003 0:00,Shipped,2,4,2003,Classic Cars,57,S24_1444,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10127,20,60.69,8,1213.8,6/3/2003 0:00,Shipped,2,6,2003,Classic Cars,57,S24_1444,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10141,20,54.33,2,1086.6,8/1/2003 0:00,Shipped,3,8,2003,Classic Cars,57,S24_1444,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10152,25,65.31,4,1632.75,9/25/2003 0:00,Shipped,3,9,2003,Classic Cars,57,S24_1444,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Small
10165,25,69.36,9,1734,10/22/2003 0:00,Shipped,4,10,2003,Classic Cars,57,S24_1444,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10176,27,68.78,8,1857.06,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,57,S24_1444,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10184,31,60.11,3,1863.41,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,57,S24_1444,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Small
10195,44,66.47,3,2924.68,11/25/2003 0:00,Shipped,4,11,2003,Classic Cars,57,S24_1444,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10207,49,46.82,4,2294.18,12/9/2003 0:00,Shipped,4,12,2003,Classic Cars,57,S24_1444,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Small
10220,26,56.07,8,1457.82,2/12/2004 0:00,Shipped,1,2,2004,Classic Cars,57,S24_1444,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Small
10230,36,54.33,6,1955.88,3/15/2004 0:00,Shipped,1,3,2004,Classic Cars,57,S24_1444,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Small
10246,44,52.6,2,2314.4,5/5/2004 0:00,Shipped,2,5,2004,Classic Cars,57,S24_1444,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10259,28,46.82,1,1310.96,6/15/2004 0:00,Shipped,2,6,2004,Classic Cars,57,S24_1444,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10271,45,64.74,2,2913.3,7/20/2004 0:00,Shipped,3,7,2004,Classic Cars,57,S24_1444,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10282,29,46.82,11,1357.78,8/20/2004 0:00,Shipped,3,8,2004,Classic Cars,57,S24_1444,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10292,40,53.75,5,2150,9/8/2004 0:00,Shipped,3,9,2004,Classic Cars,57,S24_1444,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10305,45,61.85,2,2783.25,10/13/2004 0:00,Shipped,4,10,2004,Classic Cars,57,S24_1444,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10314,44,53.18,11,2339.92,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,57,S24_1444,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10324,25,69.16,14,1729,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,57,S24_1444,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10336,45,100,4,5972.4,11/20/2004 0:00,Shipped,4,11,2004,Classic Cars,57,S24_1444,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10349,48,47.4,4,2275.2,12/1/2004 0:00,Shipped,4,12,2004,Classic Cars,57,S24_1444,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10358,44,60.76,14,2673.44,12/10/2004 0:00,Shipped,4,12,2004,Classic Cars,57,S24_1444,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10371,25,97.27,12,2431.75,1/23/2005 0:00,Shipped,1,1,2005,Classic Cars,57,S24_1444,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10383,22,91.76,2,2018.72,2/22/2005 0:00,Shipped,1,2,2005,Classic Cars,57,S24_1444,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10394,31,50.29,2,1558.99,3/15/2005 0:00,Shipped,1,3,2005,Classic Cars,57,S24_1444,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10412,21,52.6,2,1104.6,5/3/2005 0:00,Shipped,2,5,2005,Classic Cars,57,S24_1444,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10425,55,46.82,1,2575.1,5/31/2005 0:00,In Process,2,5,2005,Classic Cars,57,S24_1444,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10107,25,100,3,2845.75,2/24/2003 0:00,Shipped,1,2,2003,Motorcycles,112,S24_1578,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10120,35,98.05,1,3431.75,4/29/2003 0:00,Shipped,2,4,2003,Motorcycles,112,S24_1578,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10134,35,93.54,3,3273.9,7/1/2003 0:00,Shipped,3,7,2003,Motorcycles,112,S24_1578,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10145,43,95.8,7,4119.4,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,112,S24_1578,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10159,44,100,15,5355.68,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,112,S24_1578,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10168,50,100,2,5747.5,10/28/2003 0:00,Shipped,4,10,2003,Motorcycles,112,S24_1578,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10180,48,100,10,5355.36,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,112,S24_1578,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Medium
10188,25,100,2,2535.75,11/18/2003 0:00,Shipped,4,11,2003,Motorcycles,112,S24_1578,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10201,39,100,3,4351.23,12/1/2003 0:00,Shipped,4,12,2003,Motorcycles,112,S24_1578,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Medium
10211,25,90.16,15,2254,1/15/2004 0:00,Shipped,1,1,2004,Motorcycles,112,S24_1578,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10223,32,91.29,2,2921.28,2/20/2004 0:00,Shipped,1,2,2004,Motorcycles,112,S24_1578,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10237,20,100,8,2299,4/5/2004 0:00,Shipped,2,4,2004,Motorcycles,112,S24_1578,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10251,26,100,3,2637.18,5/18/2004 0:00,Shipped,2,5,2004,Motorcycles,112,S24_1578,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Small
10263,42,100,3,4307.52,6/28/2004 0:00,Shipped,2,6,2004,Motorcycles,112,S24_1578,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10275,21,100,2,2153.76,7/23/2004 0:00,Shipped,3,7,2004,Motorcycles,112,S24_1578,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10285,34,100,7,3716.88,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,112,S24_1578,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10299,47,100,10,5455.76,9/30/2004 0:00,Shipped,3,9,2004,Motorcycles,112,S24_1578,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10309,21,100,6,2650.62,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,112,S24_1578,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10318,48,100,2,6437.28,11/2/2004 0:00,Shipped,4,11,2004,Motorcycles,112,S24_1578,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10329,30,87.78,7,2633.4,11/15/2004 0:00,Shipped,4,11,2004,Motorcycles,112,S24_1578,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10339,27,84.39,10,2278.53,11/23/2004 0:00,Shipped,4,11,2004,Motorcycles,112,S24_1578,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10362,50,96.92,2,4846,1/5/2005 0:00,Shipped,1,1,2005,Motorcycles,112,S24_1578,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10374,38,100,6,4197.1,2/2/2005 0:00,Shipped,1,2,2005,Motorcycles,112,S24_1578,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Medium
10389,45,100,1,4597.65,3/3/2005 0:00,Shipped,1,3,2005,Motorcycles,112,S24_1578,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10403,46,100,8,5287.7,4/8/2005 0:00,Shipped,2,4,2005,Motorcycles,112,S24_1578,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10417,35,100,3,3550.05,5/13/2005 0:00,Disputed,2,5,2005,Motorcycles,112,S24_1578,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10110,29,59.37,15,1721.73,3/18/2003 0:00,Shipped,1,3,2003,Classic Cars,50,S24_1628,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10123,50,59.87,1,2993.5,5/20/2003 0:00,Shipped,2,5,2003,Classic Cars,50,S24_1628,Atelier graphique,40.32.2555,"54, rue Royale",,Nantes,,44000,France,EMEA,Schmitt,Carine,Small
10137,26,49.81,1,1295.06,7/10/2003 0:00,Shipped,3,7,2003,Classic Cars,50,S24_1628,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10148,47,56.85,8,2671.95,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,50,S24_1628,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10161,23,53.33,7,1226.59,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,50,S24_1628,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10172,34,42.76,5,1453.84,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,50,S24_1628,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10181,34,53.83,1,1830.22,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,50,S24_1628,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10192,47,53.83,6,2530.01,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,50,S24_1628,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10204,45,49.81,12,2241.45,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,50,S24_1628,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10212,45,53.33,5,2399.85,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,50,S24_1628,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10226,36,43.27,3,1557.72,2/26/2004 0:00,Shipped,1,2,2004,Classic Cars,50,S24_1628,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10241,21,40.25,10,845.25,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,50,S24_1628,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10266,28,48.3,1,1352.4,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,50,S24_1628,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10278,35,45.28,1,1584.8,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,50,S24_1628,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10288,50,52.32,13,2616,9/1/2004 0:00,Shipped,3,9,2004,Classic Cars,50,S24_1628,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10301,22,51.32,3,1129.04,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,50,S24_1628,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10311,45,49.3,8,2218.5,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,50,S24_1628,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10321,48,42.26,5,2028.48,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,50,S24_1628,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10332,20,87.96,5,1759.2,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,50,S24_1628,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10343,27,36.21,6,977.67,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,50,S24_1628,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10367,38,38.5,11,1463,1/12/2005 0:00,Resolved,1,1,2005,Classic Cars,50,S24_1628,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10379,32,100,3,3970.56,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,50,S24_1628,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10407,64,40.25,10,2576,4/22/2005 0:00,On Hold,2,4,2005,Classic Cars,50,S24_1628,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10420,37,60.37,13,2233.69,5/29/2005 0:00,In Process,2,5,2005,Classic Cars,50,S24_1628,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10106,28,88.63,4,2481.64,2/17/2003 0:00,Shipped,1,2,2003,Planes,109,S24_1785,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10120,39,100,10,4651.53,4/29/2003 0:00,Shipped,2,4,2003,Planes,109,S24_1785,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10133,41,94.1,5,3858.1,6/27/2003 0:00,Shipped,2,6,2003,Planes,109,S24_1785,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10145,40,87.54,16,3501.6,8/25/2003 0:00,Shipped,3,8,2003,Planes,109,S24_1785,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10168,49,100,11,6433.7,10/28/2003 0:00,Shipped,4,10,2003,Planes,109,S24_1785,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10210,27,98.48,9,2658.96,1/12/2004 0:00,Shipped,1,1,2004,Planes,109,S24_1785,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10223,34,100,11,3608.76,2/20/2004 0:00,Shipped,1,2,2004,Planes,109,S24_1785,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10235,23,96.29,5,2214.67,4/2/2004 0:00,Shipped,2,4,2004,Planes,109,S24_1785,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10250,31,88.63,6,2747.53,5/11/2004 0:00,Shipped,2,5,2004,Planes,109,S24_1785,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10262,34,97.38,1,3310.92,6/24/2004 0:00,Cancelled,2,6,2004,Planes,109,S24_1785,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10275,25,95.2,11,2380,7/23/2004 0:00,Shipped,3,7,2004,Planes,109,S24_1785,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10284,22,100,3,2310.88,8/21/2004 0:00,Shipped,3,8,2004,Planes,109,S24_1785,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10297,32,100,6,4061.76,9/16/2004 0:00,Shipped,3,9,2004,Planes,109,S24_1785,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Medium
10308,31,100,9,3493.7,10/15/2004 0:00,Shipped,4,10,2004,Planes,109,S24_1785,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10316,25,100,1,2872.25,11/1/2004 0:00,Shipped,4,11,2004,Planes,109,S24_1785,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10328,47,87.54,14,4114.38,11/12/2004 0:00,Shipped,4,11,2004,Planes,109,S24_1785,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10339,21,50.65,7,1063.65,11/23/2004 0:00,Shipped,4,11,2004,Planes,109,S24_1785,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10353,28,71.73,2,2008.44,12/4/2004 0:00,Shipped,4,12,2004,Planes,109,S24_1785,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Small
10374,46,94.1,3,4328.6,2/2/2005 0:00,Shipped,1,2,2005,Planes,109,S24_1785,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Medium
10386,33,41.71,11,1376.43,3/1/2005 0:00,Resolved,1,3,2005,Planes,109,S24_1785,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10398,43,100,16,5552.16,3/30/2005 0:00,Shipped,1,3,2005,Planes,109,S24_1785,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10401,38,96.29,5,3659.02,4/3/2005 0:00,On Hold,2,4,2005,Planes,109,S24_1785,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Medium
10416,47,88.63,6,4165.61,5/10/2005 0:00,Shipped,2,5,2005,Planes,109,S24_1785,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10101,45,31.2,3,1404,1/9/2003 0:00,Shipped,1,1,2003,Vintage Cars,33,S24_1937,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Small
10110,20,35.51,3,710.2,3/18/2003 0:00,Shipped,1,3,2003,Vintage Cars,33,S24_1937,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10124,45,37.84,2,1702.8,5/21/2003 0:00,Shipped,2,5,2003,Vintage Cars,33,S24_1937,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10149,36,33.19,7,1194.84,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,33,S24_1937,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Small
10162,37,27.22,5,1007.14,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,33,S24_1937,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10173,31,31.53,9,977.43,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,33,S24_1937,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10182,39,36.84,6,1436.76,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,33,S24_1937,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10193,26,29.21,10,759.46,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,33,S24_1937,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10205,32,37.17,5,1189.44,12/3/2003 0:00,Shipped,4,12,2003,Vintage Cars,33,S24_1937,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10214,20,34.19,3,683.8,1/26/2004 0:00,Shipped,1,1,2004,Vintage Cars,33,S24_1937,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10227,42,29.21,6,1226.82,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,33,S24_1937,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10243,33,29.54,1,974.82,4/26/2004 0:00,Shipped,2,4,2004,Vintage Cars,33,S24_1937,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Small
10280,20,28.88,12,577.6,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,33,S24_1937,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10288,29,38.17,1,1106.93,9/1/2004 0:00,Shipped,3,9,2004,Vintage Cars,33,S24_1937,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10304,23,30.2,16,694.6,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,33,S24_1937,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Small
10312,39,29.54,13,1152.06,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,33,S24_1937,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10322,20,100,3,2624,11/4/2004 0:00,Shipped,4,11,2004,Vintage Cars,33,S24_1937,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10332,45,81.91,6,3685.95,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,33,S24_1937,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10344,20,35.18,6,703.6,11/25/2004 0:00,Shipped,4,11,2004,Vintage Cars,33,S24_1937,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10356,48,100,5,9720,12/9/2004 0:00,Shipped,4,12,2004,Vintage Cars,33,S24_1937,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Large
10367,23,36.29,13,834.67,1/12/2005 0:00,Resolved,1,1,2005,Vintage Cars,33,S24_1937,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10380,32,70.56,4,2257.92,2/16/2005 0:00,Shipped,1,2,2005,Vintage Cars,33,S24_1937,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10391,33,100,8,8344.71,3/9/2005 0:00,Shipped,1,3,2005,Vintage Cars,33,S24_1937,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Large
10409,61,29.54,1,1801.94,4/23/2005 0:00,Shipped,2,4,2005,Vintage Cars,33,S24_1937,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10420,45,26.88,1,1209.6,5/29/2005 0:00,In Process,2,5,2005,Vintage Cars,33,S24_1937,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10107,38,83.03,7,3155.14,2/24/2003 0:00,Shipped,1,2,2003,Motorcycles,76,S24_2000,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10120,34,83.79,5,2848.86,4/29/2003 0:00,Shipped,2,4,2003,Motorcycles,76,S24_2000,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10134,43,83.03,7,3570.29,7/1/2003 0:00,Shipped,3,7,2003,Motorcycles,76,S24_2000,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10145,47,83.03,11,3902.41,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,76,S24_2000,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10158,22,67.03,1,1474.66,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,76,S24_2000,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10168,29,75.41,6,2186.89,10/28/2003 0:00,Shipped,4,10,2003,Motorcycles,76,S24_2000,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10180,28,68.55,14,1919.4,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,76,S24_2000,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10188,40,91.4,6,3656,11/18/2003 0:00,Shipped,4,11,2003,Motorcycles,76,S24_2000,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10201,25,73.88,7,1847,12/1/2003 0:00,Shipped,4,12,2003,Motorcycles,76,S24_2000,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10210,30,61.7,4,1851,1/12/2004 0:00,Shipped,1,1,2004,Motorcycles,76,S24_2000,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10223,38,69.31,6,2633.78,2/20/2004 0:00,Shipped,1,2,2004,Motorcycles,76,S24_2000,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10236,36,87.6,3,3153.6,4/3/2004 0:00,Shipped,2,4,2004,Motorcycles,76,S24_2000,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10250,32,87.6,1,2803.2,5/11/2004 0:00,Shipped,2,5,2004,Motorcycles,76,S24_2000,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10263,37,62.46,7,2311.02,6/28/2004 0:00,Shipped,2,6,2004,Motorcycles,76,S24_2000,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10275,30,79.98,6,2399.4,7/23/2004 0:00,Shipped,3,7,2004,Motorcycles,76,S24_2000,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10285,39,70.08,11,2733.12,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,76,S24_2000,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10297,32,65.51,1,2096.32,9/16/2004 0:00,Shipped,3,9,2004,Motorcycles,76,S24_2000,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Small
10308,47,63.22,4,2971.34,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,76,S24_2000,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10318,26,86.83,6,2257.58,11/2/2004 0:00,Shipped,4,11,2004,Motorcycles,76,S24_2000,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10329,37,94.43,4,3493.91,11/15/2004 0:00,Shipped,4,11,2004,Motorcycles,76,S24_2000,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10340,55,79.98,8,4398.9,11/24/2004 0:00,Shipped,4,11,2004,Motorcycles,76,S24_2000,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10363,21,100,8,3595.62,1/6/2005 0:00,Shipped,1,1,2005,Motorcycles,76,S24_2000,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10375,23,100,9,2443.29,2/3/2005 0:00,Shipped,1,2,2005,Motorcycles,76,S24_2000,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10389,49,81.4,2,3988.6,3/3/2005 0:00,Shipped,1,3,2005,Motorcycles,76,S24_2000,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10402,59,87.6,3,5168.4,4/7/2005 0:00,Shipped,2,4,2005,Motorcycles,76,S24_2000,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10416,32,87.6,1,2803.2,5/10/2005 0:00,Shipped,2,5,2005,Motorcycles,76,S24_2000,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10105,43,100,9,6341.21,2/11/2003 0:00,Shipped,1,2,2003,Ships,122,S24_2011,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10117,41,100,3,5189.78,4/16/2003 0:00,Shipped,2,4,2003,Ships,122,S24_2011,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10129,45,100,9,6027.75,6/12/2003 0:00,Shipped,2,6,2003,Ships,122,S24_2011,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10142,33,100,6,3366,8/8/2003 0:00,Shipped,3,8,2003,Ships,122,S24_2011,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10153,40,100,5,5456.4,9/28/2003 0:00,Shipped,3,9,2003,Ships,122,S24_2011,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10167,33,100,16,3812.16,10/23/2003 0:00,Cancelled,4,10,2003,Ships,122,S24_2011,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10177,50,100,7,6083,11/7/2003 0:00,Shipped,4,11,2003,Ships,122,S24_2011,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Medium
10185,30,100,7,3170.7,11/14/2003 0:00,Shipped,4,11,2003,Ships,122,S24_2011,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10197,41,100,13,4534.6,11/26/2003 0:00,Shipped,4,11,2003,Ships,122,S24_2011,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10208,35,100,7,4301.15,1/2/2004 0:00,Shipped,1,1,2004,Ships,122,S24_2011,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10221,49,100,1,6804.63,2/18/2004 0:00,Shipped,1,2,2004,Ships,122,S24_2011,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10232,46,100,4,5652.94,3/20/2004 0:00,Shipped,1,3,2004,Ships,122,S24_2011,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10248,48,100,10,6960.48,5/7/2004 0:00,Cancelled,2,5,2004,Ships,122,S24_2011,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10261,36,100,8,4512.6,6/17/2004 0:00,Shipped,2,6,2004,Ships,122,S24_2011,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10273,22,100,11,2784.76,7/21/2004 0:00,Shipped,3,7,2004,Ships,122,S24_2011,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10283,42,100,13,5316.36,8/20/2004 0:00,Shipped,3,8,2004,Ships,122,S24_2011,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10293,21,100,2,2941.89,9/9/2004 0:00,Shipped,3,9,2004,Ships,122,S24_2011,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10306,29,100,7,3207.4,10/14/2004 0:00,Shipped,4,10,2004,Ships,122,S24_2011,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10315,35,100,6,4215.05,10/29/2004 0:00,Shipped,4,10,2004,Ships,122,S24_2011,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10326,41,100,4,4333.29,11/9/2004 0:00,Shipped,4,11,2004,Ships,122,S24_2011,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10337,29,71.97,4,2087.13,11/21/2004 0:00,Shipped,4,11,2004,Ships,122,S24_2011,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Small
10350,34,50.33,7,1711.22,12/2/2004 0:00,Shipped,4,12,2004,Ships,122,S24_2011,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10372,37,100,8,3910.53,1/26/2005 0:00,Shipped,1,1,2005,Ships,122,S24_2011,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10384,28,80.54,3,2255.12,2/23/2005 0:00,Shipped,1,2,2005,Ships,122,S24_2011,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10396,49,100,6,5720.75,3/23/2005 0:00,Shipped,1,3,2005,Ships,122,S24_2011,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10414,23,100,10,3335.23,5/6/2005 0:00,On Hold,2,5,2005,Ships,122,S24_2011,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10101,46,53.76,2,2472.96,1/9/2003 0:00,Shipped,1,1,2003,Vintage Cars,44,S24_2022,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Small
10110,39,44.35,2,1729.65,3/18/2003 0:00,Shipped,1,3,2003,Vintage Cars,44,S24_2022,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10124,22,45.25,1,995.5,5/21/2003 0:00,Shipped,2,5,2003,Vintage Cars,44,S24_2022,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10149,49,49.28,6,2414.72,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,44,S24_2022,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Small
10162,43,36.29,4,1560.47,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,44,S24_2022,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10173,27,41.22,8,1112.94,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,44,S24_2022,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10182,31,36.74,5,1138.94,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,44,S24_2022,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10193,20,50.62,9,1012.4,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,44,S24_2022,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10205,24,38.08,4,913.92,12/3/2003 0:00,Shipped,4,12,2003,Vintage Cars,44,S24_2022,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10214,49,47.94,2,2349.06,1/26/2004 0:00,Shipped,1,1,2004,Vintage Cars,44,S24_2022,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10227,24,48.38,5,1161.12,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,44,S24_2022,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10244,39,45.25,9,1764.75,4/29/2004 0:00,Shipped,2,4,2004,Vintage Cars,44,S24_2022,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10255,37,45.7,2,1690.9,6/4/2004 0:00,Shipped,2,6,2004,Vintage Cars,44,S24_2022,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10280,45,47.49,11,2137.05,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,44,S24_2022,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10289,45,48.38,4,2177.1,9/3/2004 0:00,Shipped,3,9,2004,Vintage Cars,44,S24_2022,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10304,44,39.42,15,1734.48,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,44,S24_2022,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Small
10312,23,37.63,12,865.49,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,44,S24_2022,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10322,30,100,4,3500.1,11/4/2004 0:00,Shipped,4,11,2004,Vintage Cars,44,S24_2022,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10332,26,85.52,10,2223.52,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,44,S24_2022,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10345,43,53.76,1,2311.68,11/25/2004 0:00,Shipped,4,11,2004,Vintage Cars,44,S24_2022,Atelier graphique,40.32.2555,"54, rue Royale",,Nantes,,44000,France,EMEA,Schmitt,Carine,Small
10356,26,31.86,7,828.36,12/9/2004 0:00,Shipped,4,12,2004,Vintage Cars,44,S24_2022,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Small
10367,28,30.59,12,856.52,1/12/2005 0:00,Resolved,1,1,2005,Vintage Cars,44,S24_2022,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10380,27,68.35,5,1845.45,2/16/2005 0:00,Shipped,1,2,2005,Vintage Cars,44,S24_2022,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10391,24,100,1,4042.08,3/9/2005 0:00,Shipped,1,3,2005,Vintage Cars,44,S24_2022,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10421,40,45.7,2,1828,5/29/2005 0:00,In Process,2,5,2005,Vintage Cars,44,S24_2022,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10103,36,100,1,3680.28,1/29/2003 0:00,Shipped,1,1,2003,Trucks and Buses,127,S24_2300,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10114,21,100,5,2925.09,4/1/2003 0:00,Shipped,2,4,2003,Trucks and Buses,127,S24_2300,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Small
10126,27,100,1,3415.77,5/28/2003 0:00,Shipped,2,5,2003,Trucks and Buses,127,S24_2300,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10140,47,100,1,5105.14,7/24/2003 0:00,Shipped,3,7,2003,Trucks and Buses,127,S24_2300,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10151,42,100,8,5098.8,9/21/2003 0:00,Shipped,3,9,2003,Trucks and Buses,127,S24_2300,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10165,32,100,17,4661.76,10/22/2003 0:00,Shipped,4,10,2003,Trucks and Buses,127,S24_2300,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10175,28,100,6,2969.96,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,127,S24_2300,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10184,24,100,11,3496.32,11/14/2003 0:00,Shipped,4,11,2003,Trucks and Buses,127,S24_2300,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Medium
10194,49,100,1,5760.93,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,127,S24_2300,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10207,46,100,12,6819.04,12/9/2003 0:00,Shipped,4,12,2003,Trucks and Buses,127,S24_2300,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Medium
10217,28,100,1,3148.88,2/4/2004 0:00,Shipped,1,2,2004,Trucks and Buses,127,S24_2300,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10229,48,100,6,5704.32,3/11/2004 0:00,Shipped,1,3,2004,Trucks and Buses,127,S24_2300,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10246,29,100,10,3520.6,5/5/2004 0:00,Shipped,2,5,2004,Trucks and Buses,127,S24_2300,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10259,47,100,9,5285.62,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,127,S24_2300,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10271,43,100,10,5605.05,7/20/2004 0:00,Shipped,3,7,2004,Trucks and Buses,127,S24_2300,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10281,25,100,6,2779.5,8/19/2004 0:00,Shipped,3,8,2004,Trucks and Buses,127,S24_2300,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10291,48,100,1,5398.08,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,127,S24_2300,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10305,24,100,10,3189.6,10/13/2004 0:00,Shipped,4,10,2004,Trucks and Buses,127,S24_2300,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10313,42,100,4,5581.8,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,127,S24_2300,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10324,31,100,2,3820.44,11/5/2004 0:00,Shipped,4,11,2004,Trucks and Buses,127,S24_2300,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10334,42,100,5,5528.04,11/19/2004 0:00,On Hold,4,11,2004,Trucks and Buses,127,S24_2300,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10348,37,100,1,5981.42,11/1/2004 0:00,Shipped,4,11,2004,Trucks and Buses,127,S24_2300,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10358,41,100,7,5684.65,12/10/2004 0:00,Shipped,4,12,2004,Trucks and Buses,127,S24_2300,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10371,20,100,5,3449.4,1/23/2005 0:00,Shipped,1,1,2005,Trucks and Buses,127,S24_2300,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10382,20,100,3,2654.4,2/17/2005 0:00,Shipped,1,2,2005,Trucks and Buses,127,S24_2300,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10412,70,100,10,8498,5/3/2005 0:00,Shipped,2,5,2005,Trucks and Buses,127,S24_2300,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Large
10425,49,100,9,5510.54,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,127,S24_2300,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10108,35,58.87,15,2060.45,3/3/2003 0:00,Shipped,1,3,2003,Motorcycles,69,S24_2360,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10121,32,76.88,2,2460.16,5/7/2003 0:00,Shipped,2,5,2003,Motorcycles,69,S24_2360,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10135,29,61.64,16,1787.56,7/2/2003 0:00,Shipped,3,7,2003,Motorcycles,69,S24_2360,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10145,27,60.95,3,1645.65,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,69,S24_2360,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10159,27,80.34,11,2169.18,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,69,S24_2360,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10169,38,74.11,11,2816.18,11/4/2003 0:00,Shipped,4,11,2003,Motorcycles,69,S24_2360,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10180,35,72.03,6,2521.05,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,69,S24_2360,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10190,42,76.19,3,3199.98,11/19/2003 0:00,Shipped,4,11,2003,Motorcycles,69,S24_2360,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10211,21,63.72,11,1338.12,1/15/2004 0:00,Shipped,1,1,2004,Motorcycles,69,S24_2360,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10224,37,80.34,4,2972.58,2/21/2004 0:00,Shipped,1,2,2004,Motorcycles,69,S24_2360,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10237,26,79.65,4,2070.9,4/5/2004 0:00,Shipped,2,4,2004,Motorcycles,69,S24_2360,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10252,47,65.8,8,3092.6,5/26/2004 0:00,Shipped,2,5,2004,Motorcycles,69,S24_2360,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10264,37,65.1,6,2408.7,6/30/2004 0:00,Shipped,2,6,2004,Motorcycles,69,S24_2360,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10276,46,75.49,12,3472.54,8/2/2004 0:00,Shipped,3,8,2004,Motorcycles,69,S24_2360,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Medium
10285,38,59.56,3,2263.28,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,69,S24_2360,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10299,33,66.49,6,2194.17,9/30/2004 0:00,Shipped,3,9,2004,Motorcycles,69,S24_2360,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10309,24,56.1,2,1346.4,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,69,S24_2360,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10319,31,81.73,7,2533.63,11/3/2004 0:00,Shipped,4,11,2004,Motorcycles,69,S24_2360,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Small
10330,42,81.03,1,3403.26,11/16/2004 0:00,Shipped,4,11,2004,Motorcycles,69,S24_2360,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10341,32,100,6,3307.2,11/24/2004 0:00,Shipped,4,11,2004,Motorcycles,69,S24_2360,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10355,41,70.65,3,2896.65,12/7/2004 0:00,Shipped,4,12,2004,Motorcycles,69,S24_2360,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10363,43,61.23,14,2632.89,1/6/2005 0:00,Shipped,1,1,2005,Motorcycles,69,S24_2360,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10375,20,100,14,2046,2/3/2005 0:00,Shipped,1,2,2005,Motorcycles,69,S24_2360,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10390,35,65.13,4,2279.55,3/4/2005 0:00,Shipped,1,3,2005,Motorcycles,69,S24_2360,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10403,27,79.65,4,2150.55,4/8/2005 0:00,Shipped,2,4,2005,Motorcycles,69,S24_2360,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10110,43,78.15,11,3360.45,3/18/2003 0:00,Shipped,1,3,2003,Classic Cars,90,S24_2766,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10124,32,72.7,10,2326.4,5/21/2003 0:00,Shipped,2,5,2003,Classic Cars,90,S24_2766,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10148,21,73.6,4,1545.6,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,90,S24_2766,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10161,20,100,3,2144.6,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,90,S24_2766,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10172,22,74.51,1,1639.22,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,90,S24_2766,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10182,36,73.6,14,2649.6,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,90,S24_2766,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10192,46,83.6,2,3845.6,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,90,S24_2766,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10204,47,96.32,8,4527.04,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,90,S24_2766,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10212,45,88.14,1,3966.3,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,90,S24_2766,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10227,47,88.14,14,4142.58,3/2/2004 0:00,Shipped,1,3,2004,Classic Cars,90,S24_2766,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10241,47,94.5,6,4441.5,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,90,S24_2766,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Medium
10267,38,87.24,3,3315.12,7/7/2004 0:00,Shipped,3,7,2004,Classic Cars,90,S24_2766,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10279,49,79.97,3,3918.53,8/9/2004 0:00,Shipped,3,8,2004,Classic Cars,90,S24_2766,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10288,35,80.87,9,2830.45,9/1/2004 0:00,Shipped,3,9,2004,Classic Cars,90,S24_2766,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10302,49,100,5,5298.86,10/6/2003 0:00,Shipped,4,10,2003,Classic Cars,90,S24_2766,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10311,28,93.6,4,2620.8,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,90,S24_2766,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10321,30,72.7,1,2181,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,90,S24_2766,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10332,39,86.72,7,3382.08,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,90,S24_2766,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10346,25,100,1,2876.75,11/29/2004 0:00,Shipped,4,11,2004,Classic Cars,90,S24_2766,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10368,40,100,2,4107.2,1/19/2005 0:00,Shipped,1,1,2005,Classic Cars,90,S24_2766,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10380,36,37.5,6,1350,2/16/2005 0:00,Shipped,1,2,2005,Classic Cars,90,S24_2766,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10407,76,94.5,6,7182,4/22/2005 0:00,On Hold,2,4,2005,Classic Cars,90,S24_2766,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Large
10420,39,100,9,3933.93,5/29/2005 0:00,In Process,2,5,2005,Classic Cars,90,S24_2766,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10104,44,39.6,10,1742.4,1/31/2003 0:00,Shipped,1,1,2003,Classic Cars,35,S24_2840,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10114,24,30.06,1,721.44,4/1/2003 0:00,Shipped,2,4,2003,Classic Cars,35,S24_2840,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Small
10127,39,38.19,12,1489.41,6/3/2003 0:00,Shipped,2,6,2003,Classic Cars,35,S24_2840,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10141,21,42.43,6,891.03,8/1/2003 0:00,Shipped,3,8,2003,Classic Cars,35,S24_2840,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10151,30,40.31,4,1209.3,9/21/2003 0:00,Shipped,3,9,2003,Classic Cars,35,S24_2840,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10165,27,31.82,13,859.14,10/22/2003 0:00,Shipped,4,10,2003,Classic Cars,35,S24_2840,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10175,37,31.12,2,1151.44,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,35,S24_2840,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10184,42,31.82,7,1336.44,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,35,S24_2840,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Small
10195,32,28.29,7,905.28,11/25/2003 0:00,Shipped,4,11,2003,Classic Cars,35,S24_2840,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10207,42,29.7,8,1247.4,12/9/2003 0:00,Shipped,4,12,2003,Classic Cars,35,S24_2840,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Small
10219,21,40.31,3,846.51,2/10/2004 0:00,Shipped,1,2,2004,Classic Cars,35,S24_2840,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Small
10229,33,32.88,2,1085.04,3/11/2004 0:00,Shipped,1,3,2004,Classic Cars,35,S24_2840,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10246,49,36.07,6,1767.43,5/5/2004 0:00,Shipped,2,5,2004,Classic Cars,35,S24_2840,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10259,31,33.24,5,1030.44,6/15/2004 0:00,Shipped,2,6,2004,Classic Cars,35,S24_2840,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10271,38,41.72,6,1585.36,7/20/2004 0:00,Shipped,3,7,2004,Classic Cars,35,S24_2840,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10281,20,40.66,2,813.2,8/19/2004 0:00,Shipped,3,8,2004,Classic Cars,35,S24_2840,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10292,39,30.06,9,1172.34,9/8/2004 0:00,Shipped,3,9,2004,Classic Cars,35,S24_2840,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10305,48,31.47,6,1510.56,10/13/2004 0:00,Shipped,4,10,2004,Classic Cars,35,S24_2840,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10314,39,37.13,15,1448.07,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,35,S24_2840,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10324,30,100,9,3338.1,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,35,S24_2840,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10335,33,37.13,2,1225.29,11/19/2004 0:00,Shipped,4,11,2004,Classic Cars,35,S24_2840,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10349,36,37.13,3,1336.68,12/1/2004 0:00,Shipped,4,12,2004,Classic Cars,35,S24_2840,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10358,36,82.94,4,2985.84,12/10/2004 0:00,Shipped,4,12,2004,Classic Cars,35,S24_2840,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10371,45,100,8,5545.8,1/23/2005 0:00,Shipped,1,1,2005,Classic Cars,35,S24_2840,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10383,40,100,3,6089.6,2/22/2005 0:00,Shipped,1,2,2005,Classic Cars,35,S24_2840,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10394,46,38.9,6,1789.4,3/15/2005 0:00,Shipped,1,3,2005,Classic Cars,35,S24_2840,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10412,30,36.07,6,1082.1,5/3/2005 0:00,Shipped,2,5,2005,Classic Cars,35,S24_2840,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10425,31,33.24,5,1030.44,5/31/2005 0:00,In Process,2,5,2005,Classic Cars,35,S24_2840,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10106,49,74.68,13,3659.32,2/17/2003 0:00,Shipped,1,2,2003,Planes,68,S24_2841,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10119,41,59.6,4,2443.6,4/28/2003 0:00,Shipped,2,4,2003,Planes,68,S24_2841,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10131,35,67.14,5,2349.9,6/16/2003 0:00,Shipped,2,6,2003,Planes,68,S24_2841,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Small
10143,27,60.97,8,1646.19,8/10/2003 0:00,Shipped,3,8,2003,Planes,68,S24_2841,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10155,23,72.62,6,1670.26,10/6/2003 0:00,Shipped,4,10,2003,Planes,68,S24_2841,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10167,21,69.88,2,1467.48,10/23/2003 0:00,Cancelled,4,10,2003,Planes,68,S24_2841,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10178,34,80.84,5,2748.56,11/8/2003 0:00,Shipped,4,11,2003,Planes,68,S24_2841,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Small
10186,22,69.2,2,1522.4,11/14/2003 0:00,Shipped,4,11,2003,Planes,68,S24_2841,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Small
10198,48,67.82,5,3255.36,11/27/2003 0:00,Shipped,4,11,2003,Planes,68,S24_2841,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10209,43,82.21,1,3535.03,1/9/2004 0:00,Shipped,1,1,2004,Planes,68,S24_2841,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Medium
10222,32,81.53,5,2608.96,2/19/2004 0:00,Shipped,1,2,2004,Planes,68,S24_2841,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10249,20,67.82,1,1356.4,5/8/2004 0:00,Shipped,2,5,2004,Planes,68,S24_2841,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Small
10262,24,67.14,10,1611.36,6/24/2004 0:00,Cancelled,2,6,2004,Planes,68,S24_2841,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10274,40,65.08,2,2603.2,7/21/2004 0:00,Shipped,3,7,2004,Planes,68,S24_2841,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10284,30,73.99,12,2219.7,8/21/2004 0:00,Shipped,3,8,2004,Planes,68,S24_2841,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10296,21,71.25,8,1496.25,9/15/2004 0:00,Shipped,3,9,2004,Planes,68,S24_2841,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10307,25,75.36,2,1884,10/14/2004 0:00,Shipped,4,10,2004,Planes,68,S24_2841,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10316,34,63.71,10,2166.14,11/1/2004 0:00,Shipped,4,11,2004,Planes,68,S24_2841,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10328,48,58.92,1,2828.16,11/12/2004 0:00,Shipped,4,11,2004,Planes,68,S24_2841,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10339,55,100,12,6214.45,11/23/2004 0:00,Shipped,4,11,2004,Planes,68,S24_2841,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10351,25,74.68,5,1867,12/3/2004 0:00,Shipped,4,12,2004,Planes,68,S24_2841,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10373,38,70.44,7,2676.72,1/31/2005 0:00,Shipped,1,1,2005,Planes,68,S24_2841,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10386,39,55.96,1,2182.44,3/1/2005 0:00,Resolved,1,3,2005,Planes,68,S24_2841,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10398,28,57.55,3,1611.4,3/30/2005 0:00,Shipped,1,3,2005,Planes,68,S24_2841,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10400,24,61.66,2,1479.84,4/1/2005 0:00,Shipped,2,4,2005,Planes,68,S24_2841,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10415,21,67.82,1,1424.22,5/9/2005 0:00,Disputed,2,5,2005,Planes,68,S24_2841,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10110,46,100,10,5942.28,3/18/2003 0:00,Shipped,1,3,2003,Classic Cars,117,S24_2887,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10124,25,93.95,9,2348.75,5/21/2003 0:00,Shipped,2,5,2003,Classic Cars,117,S24_2887,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10148,34,100,3,4392.12,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,117,S24_2887,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10161,25,100,2,2759.75,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,117,S24_2887,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10173,23,100,16,2728.03,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,117,S24_2887,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10182,20,100,13,2395.8,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,117,S24_2887,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10192,23,100,1,3052.33,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,117,S24_2887,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10204,42,100,7,4242,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,117,S24_2887,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10213,27,100,3,2790.45,1/22/2004 0:00,Shipped,1,1,2004,Classic Cars,117,S24_2887,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Small
10227,33,100,13,4340.49,3/2/2004 0:00,Shipped,1,3,2004,Classic Cars,117,S24_2887,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10241,28,98.65,5,2762.2,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,117,S24_2887,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10267,43,100,2,4645.72,7/7/2004 0:00,Shipped,3,7,2004,Classic Cars,117,S24_2887,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10279,48,100,2,5580.96,8/9/2004 0:00,Shipped,3,8,2004,Classic Cars,117,S24_2887,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10288,48,100,8,6539.04,9/1/2004 0:00,Shipped,3,9,2004,Classic Cars,117,S24_2887,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10302,45,100,4,5548.95,10/6/2003 0:00,Shipped,4,10,2003,Classic Cars,117,S24_2887,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10311,43,100,3,4595.41,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,117,S24_2887,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10332,44,42.26,11,1859.44,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,117,S24_2887,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10346,24,87.24,5,2093.76,11/29/2004 0:00,Shipped,4,11,2004,Classic Cars,117,S24_2887,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10368,31,100,5,4223.13,1/19/2005 0:00,Shipped,1,1,2005,Classic Cars,117,S24_2887,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10380,44,36.29,7,1596.76,2/16/2005 0:00,Shipped,1,2,2005,Classic Cars,117,S24_2887,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10407,59,98.65,5,5820.35,4/22/2005 0:00,On Hold,2,4,2005,Classic Cars,117,S24_2887,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10420,55,96.3,8,5296.5,5/29/2005 0:00,In Process,2,5,2005,Classic Cars,117,S24_2887,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10109,29,32.1,6,930.9,3/10/2003 0:00,Shipped,1,3,2003,Classic Cars,37,S24_2972,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Small
10122,39,30.96,4,1207.44,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,37,S24_2972,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10135,20,35.87,1,717.4,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,37,S24_2972,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10147,25,42.67,1,1066.75,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,37,S24_2972,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10160,42,37,2,1554,10/11/2003 0:00,Shipped,4,10,2003,Classic Cars,37,S24_2972,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Small
10171,36,35.49,4,1277.64,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,37,S24_2972,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Small
10181,37,42.67,8,1578.79,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,37,S24_2972,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10192,30,30.59,13,917.7,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,37,S24_2972,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10203,21,37,2,777,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,37,S24_2972,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10212,34,43.42,12,1476.28,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,37,S24_2972,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10225,42,36.63,3,1538.46,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,37,S24_2972,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Small
10239,20,44.56,2,891.2,4/12/2004 0:00,Shipped,2,4,2004,Classic Cars,37,S24_2972,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10253,40,42.67,7,1706.8,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,37,S24_2972,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10266,34,40.4,8,1373.6,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,37,S24_2972,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10278,31,38.89,8,1205.59,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,37,S24_2972,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10287,36,39.65,6,1427.4,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,37,S24_2972,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Small
10301,48,34.36,10,1649.28,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,37,S24_2972,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10310,33,41.91,4,1383.03,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,37,S24_2972,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10321,37,33.23,12,1229.51,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,37,S24_2972,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10331,27,42.24,13,1140.48,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,37,S24_2972,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Small
10342,39,40.4,9,1575.6,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,37,S24_2972,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10355,36,38.52,4,1386.72,12/7/2004 0:00,Shipped,4,12,2004,Classic Cars,37,S24_2972,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10367,36,100,2,5018.4,1/12/2005 0:00,Resolved,1,1,2005,Classic Cars,37,S24_2972,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10378,41,100,7,5856.85,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,37,S24_2972,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10390,37,100,5,4894.73,3/4/2005 0:00,Shipped,1,3,2005,Classic Cars,37,S24_2972,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10405,47,44.56,2,2094.32,4/14/2005 0:00,Shipped,2,4,2005,Classic Cars,37,S24_2972,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10419,15,42.67,7,640.05,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,37,S24_2972,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10105,44,72.58,4,3193.52,2/11/2003 0:00,Shipped,1,2,2003,Vintage Cars,88,S24_3151,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10119,35,87.62,13,3066.7,4/28/2003 0:00,Shipped,2,4,2003,Vintage Cars,88,S24_3151,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10129,41,94.71,4,3883.11,6/12/2003 0:00,Shipped,2,6,2003,Vintage Cars,88,S24_3151,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10142,49,98.25,1,4814.25,8/8/2003 0:00,Shipped,3,8,2003,Vintage Cars,88,S24_3151,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10154,31,91.17,2,2826.27,10/2/2003 0:00,Shipped,4,10,2003,Vintage Cars,88,S24_3151,Boards & Toys Co.,3105552373,4097 Douglas Av.,,Glendale,CA,92561,USA,NA,Young,Leslie,Small
10167,20,79.66,11,1593.2,10/23/2003 0:00,Cancelled,4,10,2003,Vintage Cars,88,S24_3151,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10177,45,72.58,2,3266.1,11/7/2003 0:00,Shipped,4,11,2003,Vintage Cars,88,S24_3151,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Medium
10185,33,74.35,2,2453.55,11/14/2003 0:00,Shipped,4,11,2003,Vintage Cars,88,S24_3151,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10197,47,83.2,8,3910.4,11/26/2003 0:00,Shipped,4,11,2003,Vintage Cars,88,S24_3151,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10208,20,89.4,2,1788,1/2/2004 0:00,Shipped,1,1,2004,Vintage Cars,88,S24_3151,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10222,47,70.81,14,3328.07,2/19/2004 0:00,Shipped,1,2,2004,Vintage Cars,88,S24_3151,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10233,40,94.71,2,3788.4,3/29/2004 0:00,Shipped,1,3,2004,Vintage Cars,88,S24_3151,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Medium
10248,30,100,5,3053.7,5/7/2004 0:00,Cancelled,2,5,2004,Vintage Cars,88,S24_3151,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10261,22,91.17,3,2005.74,6/17/2004 0:00,Shipped,2,6,2004,Vintage Cars,88,S24_3151,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Small
10273,27,100,6,2796.12,7/21/2004 0:00,Shipped,3,7,2004,Vintage Cars,88,S24_3151,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10283,34,92.94,8,3159.96,8/20/2004 0:00,Shipped,3,8,2004,Vintage Cars,88,S24_3151,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10295,46,84.97,3,3908.62,9/10/2004 0:00,Shipped,3,9,2004,Vintage Cars,88,S24_3151,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10306,31,84.08,2,2606.48,10/14/2004 0:00,Shipped,4,10,2004,Vintage Cars,88,S24_3151,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10315,24,86.74,1,2081.76,10/29/2004 0:00,Shipped,4,10,2004,Vintage Cars,88,S24_3151,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10326,41,85.85,3,3519.85,11/9/2004 0:00,Shipped,4,11,2004,Vintage Cars,88,S24_3151,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Medium
10339,55,100,13,10758,11/23/2004 0:00,Shipped,4,11,2004,Vintage Cars,88,S24_3151,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Large
10350,30,100,9,3021,12/2/2004 0:00,Shipped,4,12,2004,Vintage Cars,88,S24_3151,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10373,33,57.32,12,1891.56,1/31/2005 0:00,Shipped,1,1,2005,Vintage Cars,88,S24_3151,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10384,43,97.87,2,4208.41,2/23/2005 0:00,Shipped,1,2,2005,Vintage Cars,88,S24_3151,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10396,27,83.2,7,2246.4,3/23/2005 0:00,Shipped,1,3,2005,Vintage Cars,88,S24_3151,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10414,60,100,5,6107.4,5/6/2005 0:00,On Hold,2,5,2005,Vintage Cars,88,S24_3151,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10110,27,73.62,12,1987.74,3/18/2003 0:00,Shipped,1,3,2003,Classic Cars,85,S24_3191,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10124,49,83.04,11,4068.96,5/21/2003 0:00,Shipped,2,5,2003,Classic Cars,85,S24_3191,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10148,31,73.62,5,2282.22,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,85,S24_3191,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10161,20,77.05,4,1541,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,85,S24_3191,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10172,24,81.33,2,1951.92,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,85,S24_3191,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10182,33,94.17,15,3107.61,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,85,S24_3191,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10192,32,72.77,3,2328.64,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,85,S24_3191,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10204,40,79.62,9,3184.8,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,85,S24_3191,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10212,27,79.62,2,2149.74,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,85,S24_3191,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10227,40,79.62,15,3184.8,3/2/2004 0:00,Shipped,1,3,2004,Classic Cars,85,S24_3191,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10241,26,81.33,7,2114.58,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,85,S24_3191,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10267,44,96.74,4,4256.56,7/7/2004 0:00,Shipped,3,7,2004,Classic Cars,85,S24_3191,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10279,33,71.06,4,2344.98,8/9/2004 0:00,Shipped,3,8,2004,Classic Cars,85,S24_3191,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10288,34,68.49,10,2328.66,9/1/2004 0:00,Shipped,3,9,2004,Classic Cars,85,S24_3191,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10302,48,74.48,6,3575.04,10/6/2003 0:00,Shipped,4,10,2003,Classic Cars,85,S24_3191,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10311,25,83.04,5,2076,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,85,S24_3191,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10321,39,84.75,2,3305.25,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,85,S24_3191,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10332,45,34.19,12,1538.55,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,85,S24_3191,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10346,24,100,2,3325.92,11/29/2004 0:00,Shipped,4,11,2004,Classic Cars,85,S24_3191,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10368,46,79.62,1,3662.52,1/19/2005 0:00,Shipped,1,1,2005,Classic Cars,85,S24_3191,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10380,44,79.06,9,3478.64,2/16/2005 0:00,Shipped,1,2,2005,Classic Cars,85,S24_3191,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10407,13,81.33,7,1057.29,4/22/2005 0:00,On Hold,2,4,2005,Classic Cars,85,S24_3191,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10420,35,96.74,10,3385.9,5/29/2005 0:00,In Process,2,5,2005,Classic Cars,85,S24_3191,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10108,30,63.07,5,1892.1,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,61,S24_3371,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10122,34,50.21,9,1707.14,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,61,S24_3371,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10135,27,66.13,6,1785.51,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,61,S24_3371,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10147,30,68.58,6,2057.4,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,61,S24_3371,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10159,50,69.8,1,3490,10/10/2003 0:00,Shipped,4,10,2003,Classic Cars,61,S24_3371,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10169,34,50.21,1,1707.14,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,61,S24_3371,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10181,23,65.52,13,1506.96,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,61,S24_3371,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Small
10191,48,60.01,2,2880.48,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,61,S24_3371,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10203,34,64.9,7,2206.6,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,61,S24_3371,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10211,48,48.98,1,2351.04,1/15/2004 0:00,Shipped,1,1,2004,Classic Cars,61,S24_3371,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10225,24,50.21,8,1205.04,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,61,S24_3371,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Small
10238,47,62.45,2,2935.15,4/9/2004 0:00,Shipped,2,4,2004,Classic Cars,61,S24_3371,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10253,24,52.66,12,1263.84,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,61,S24_3371,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10266,47,62.45,13,2935.15,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,61,S24_3371,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10276,20,61.23,2,1224.6,8/2/2004 0:00,Shipped,3,8,2004,Classic Cars,61,S24_3371,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Small
10287,20,67.97,11,1359.4,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,61,S24_3371,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Small
10300,31,58.78,4,1822.18,10/4/2003 0:00,Shipped,4,10,2003,Classic Cars,61,S24_3371,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Small
10310,38,56.94,9,2163.72,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,61,S24_3371,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10320,26,61.23,2,1591.98,11/3/2004 0:00,Shipped,4,11,2004,Classic Cars,61,S24_3371,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Small
10331,25,100,9,3078.5,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,61,S24_3371,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10342,48,62.45,10,2997.6,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,61,S24_3371,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10355,44,62.45,6,2747.8,12/7/2004 0:00,Shipped,4,12,2004,Classic Cars,61,S24_3371,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10363,21,100,15,2447.76,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,61,S24_3371,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10378,46,41.54,6,1910.84,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,61,S24_3371,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10390,46,52.84,6,2430.64,3/4/2005 0:00,Shipped,1,3,2005,Classic Cars,61,S24_3371,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10419,55,52.66,12,2896.3,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,61,S24_3371,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10106,31,52.6,14,1630.6,2/17/2003 0:00,Shipped,1,2,2003,Vintage Cars,65,S24_3420,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10119,20,72.98,5,1459.6,4/28/2003 0:00,Shipped,2,4,2003,Vintage Cars,65,S24_3420,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10131,29,59.18,6,1716.22,6/16/2003 0:00,Shipped,2,6,2003,Vintage Cars,65,S24_3420,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Small
10143,33,77.59,9,2560.47,8/10/2003 0:00,Shipped,3,8,2003,Vintage Cars,65,S24_3420,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10155,34,55.89,7,1900.26,10/6/2003 0:00,Shipped,4,10,2003,Vintage Cars,65,S24_3420,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10167,32,63.12,3,2019.84,10/23/2003 0:00,Cancelled,4,10,2003,Vintage Cars,65,S24_3420,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10178,27,73.64,6,1988.28,11/8/2003 0:00,Shipped,4,11,2003,Vintage Cars,65,S24_3420,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Small
10186,21,69.04,3,1449.84,11/14/2003 0:00,Shipped,4,11,2003,Vintage Cars,65,S24_3420,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Small
10198,27,71.67,6,1935.09,11/27/2003 0:00,Shipped,4,11,2003,Vintage Cars,65,S24_3420,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10209,36,77.59,2,2793.24,1/9/2004 0:00,Shipped,1,1,2004,Vintage Cars,65,S24_3420,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Small
10222,43,70.35,6,3025.05,2/19/2004 0:00,Shipped,1,2,2004,Vintage Cars,65,S24_3420,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10249,25,69.7,2,1742.5,5/8/2004 0:00,Shipped,2,5,2004,Vintage Cars,65,S24_3420,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Small
10262,46,70.35,11,3236.1,6/24/2004 0:00,Cancelled,2,6,2004,Vintage Cars,65,S24_3420,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10274,24,72.33,3,1735.92,7/21/2004 0:00,Shipped,3,7,2004,Vintage Cars,65,S24_3420,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10284,39,71.67,13,2795.13,8/21/2004 0:00,Shipped,3,8,2004,Vintage Cars,65,S24_3420,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10296,31,53.92,9,1671.52,9/15/2004 0:00,Shipped,3,9,2004,Vintage Cars,65,S24_3420,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10307,22,71.67,3,1576.74,10/14/2004 0:00,Shipped,4,10,2004,Vintage Cars,65,S24_3420,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10316,47,76.93,11,3615.71,11/1/2004 0:00,Shipped,4,11,2004,Vintage Cars,65,S24_3420,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10328,20,72.98,2,1459.6,11/12/2004 0:00,Shipped,4,11,2004,Vintage Cars,65,S24_3420,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10339,29,99.69,14,2891.01,11/23/2004 0:00,Shipped,4,11,2004,Vintage Cars,65,S24_3420,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10351,38,68.38,4,2598.44,12/3/2004 0:00,Shipped,4,12,2004,Vintage Cars,65,S24_3420,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10361,34,100,6,3871.92,12/17/2004 0:00,Shipped,4,12,2004,Vintage Cars,65,S24_3420,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10373,46,66,11,3036,1/31/2005 0:00,Shipped,1,1,2005,Vintage Cars,65,S24_3420,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10386,35,63.76,9,2231.6,3/1/2005 0:00,Resolved,1,3,2005,Vintage Cars,65,S24_3420,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10398,34,71.67,13,2436.78,3/30/2005 0:00,Shipped,1,3,2005,Vintage Cars,65,S24_3420,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10400,38,57.2,3,2173.6,4/1/2005 0:00,Shipped,2,4,2005,Vintage Cars,65,S24_3420,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10415,18,69.7,2,1254.6,5/9/2005 0:00,Disputed,2,5,2005,Vintage Cars,65,S24_3420,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10110,37,100,14,3724.42,3/18/2003 0:00,Shipped,1,3,2003,Classic Cars,107,S24_3432,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10124,43,100,13,5203,5/21/2003 0:00,Shipped,2,5,2003,Classic Cars,107,S24_3432,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10148,27,100,7,3469.5,9/11/2003 0:00,Shipped,3,9,2003,Classic Cars,107,S24_3432,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10161,30,100,6,3148.2,10/17/2003 0:00,Shipped,4,10,2003,Classic Cars,107,S24_3432,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10172,22,98.51,4,2167.22,11/5/2003 0:00,Shipped,4,11,2003,Classic Cars,107,S24_3432,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10182,49,100,17,6244.07,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,107,S24_3432,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10192,46,100,5,5566,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,107,S24_3432,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10204,48,91.02,11,4368.96,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,107,S24_3432,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10212,46,87.81,4,4039.26,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,107,S24_3432,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10226,48,92.09,2,4420.32,2/26/2004 0:00,Shipped,1,2,2004,Classic Cars,107,S24_3432,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10241,27,86.73,9,2341.71,4/13/2004 0:00,Shipped,2,4,2004,Classic Cars,107,S24_3432,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Small
10267,43,100,6,5110.98,7/7/2004 0:00,Shipped,3,7,2004,Classic Cars,107,S24_3432,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10279,48,100,6,6168,8/9/2004 0:00,Shipped,3,8,2004,Classic Cars,107,S24_3432,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10288,41,100,12,4873.26,9/1/2004 0:00,Shipped,3,9,2004,Classic Cars,107,S24_3432,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10301,22,96.37,2,2120.14,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,107,S24_3432,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10311,46,92.09,7,4236.14,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,107,S24_3432,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10321,21,89.95,4,1888.95,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,107,S24_3432,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Small
10332,31,37.18,13,1152.58,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,107,S24_3432,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10346,26,95.88,6,2492.88,11/29/2004 0:00,Shipped,4,11,2004,Classic Cars,107,S24_3432,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10368,20,99.58,4,1991.6,1/19/2005 0:00,Shipped,1,1,2005,Classic Cars,107,S24_3432,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10380,34,100,11,3953.18,2/16/2005 0:00,Shipped,1,2,2005,Classic Cars,107,S24_3432,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10407,43,86.73,9,3729.39,4/22/2005 0:00,On Hold,2,4,2005,Classic Cars,107,S24_3432,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10420,26,100,12,2617.16,5/29/2005 0:00,In Process,2,5,2005,Classic Cars,107,S24_3432,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10105,50,79.67,1,3983.5,2/11/2003 0:00,Shipped,1,2,2003,Vintage Cars,83,S24_3816,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10119,35,90.57,10,3169.95,4/28/2003 0:00,Shipped,2,4,2003,Vintage Cars,83,S24_3816,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10129,50,77.99,1,3899.5,6/12/2003 0:00,Shipped,2,6,2003,Vintage Cars,83,S24_3816,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10143,23,80.51,14,1851.73,8/10/2003 0:00,Shipped,3,8,2003,Vintage Cars,83,S24_3816,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10155,37,67.93,12,2513.41,10/6/2003 0:00,Shipped,4,10,2003,Vintage Cars,83,S24_3816,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10167,29,83.86,8,2431.94,10/23/2003 0:00,Cancelled,4,10,2003,Vintage Cars,83,S24_3816,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10178,21,72.12,11,1514.52,11/8/2003 0:00,Shipped,4,11,2003,Vintage Cars,83,S24_3816,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Small
10186,36,85.54,8,3079.44,11/14/2003 0:00,Shipped,4,11,2003,Vintage Cars,83,S24_3816,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Medium
10197,22,86.38,5,1900.36,11/26/2003 0:00,Shipped,4,11,2003,Vintage Cars,83,S24_3816,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10209,22,89.73,7,1974.06,1/9/2004 0:00,Shipped,1,1,2004,Vintage Cars,83,S24_3816,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Small
10222,46,80.51,11,3703.46,2/19/2004 0:00,Shipped,1,2,2004,Vintage Cars,83,S24_3816,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10248,23,76.31,2,1755.13,5/7/2004 0:00,Cancelled,2,5,2004,Vintage Cars,83,S24_3816,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10262,49,87.21,16,4273.29,6/24/2004 0:00,Cancelled,2,6,2004,Vintage Cars,83,S24_3816,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10273,48,83.02,3,3984.96,7/21/2004 0:00,Shipped,3,7,2004,Vintage Cars,83,S24_3816,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10283,33,72.96,5,2407.68,8/20/2004 0:00,Shipped,3,8,2004,Vintage Cars,83,S24_3816,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10296,22,77.15,14,1697.3,9/15/2004 0:00,Shipped,3,9,2004,Vintage Cars,83,S24_3816,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10307,22,91.41,8,2011.02,10/14/2004 0:00,Shipped,4,10,2004,Vintage Cars,83,S24_3816,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10316,25,92.25,16,2306.25,11/1/2004 0:00,Shipped,4,11,2004,Vintage Cars,83,S24_3816,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10326,20,92.25,2,1845,11/9/2004 0:00,Shipped,4,11,2004,Vintage Cars,83,S24_3816,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Small
10339,42,59.36,16,2493.12,11/23/2004 0:00,Shipped,4,11,2004,Vintage Cars,83,S24_3816,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10350,25,60.34,10,1508.5,12/2/2004 0:00,Shipped,4,12,2004,Vintage Cars,83,S24_3816,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10373,23,100,10,2394.3,1/31/2005 0:00,Shipped,1,1,2005,Vintage Cars,83,S24_3816,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10385,37,85.54,2,3164.98,2/28/2005 0:00,Shipped,1,2,2005,Vintage Cars,83,S24_3816,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10396,37,90.57,8,3351.09,3/23/2005 0:00,Shipped,1,3,2005,Vintage Cars,83,S24_3816,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10400,42,72.96,8,3064.32,4/1/2005 0:00,Shipped,2,4,2005,Vintage Cars,83,S24_3816,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10414,51,76.31,2,3891.81,5/6/2005 0:00,On Hold,2,5,2005,Vintage Cars,83,S24_3816,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10108,40,100,1,5448.8,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,140,S24_3856,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10122,43,100,5,5494.97,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,140,S24_3856,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Medium
10135,47,100,2,6336.07,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,140,S24_3856,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10147,23,100,2,2906.97,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,140,S24_3856,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10160,35,100,3,4767.7,10/11/2003 0:00,Shipped,4,10,2003,Classic Cars,140,S24_3856,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Medium
10170,34,100,1,3819.56,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,140,S24_3856,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Medium
10181,25,100,9,3861.75,11/12/2003 0:00,Shipped,4,11,2003,Classic Cars,140,S24_3856,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10192,45,100,14,6319.35,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,140,S24_3856,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Medium
10203,47,100,3,6996.42,12/2/2003 0:00,Shipped,4,12,2003,Classic Cars,140,S24_3856,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10212,49,100,13,6949.67,1/16/2004 0:00,Shipped,1,1,2004,Classic Cars,140,S24_3856,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10225,40,100,4,4550,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,140,S24_3856,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10239,29,100,3,4479.63,4/12/2004 0:00,Shipped,2,4,2004,Classic Cars,140,S24_3856,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10253,39,100,8,5148,6/1/2004 0:00,Cancelled,2,6,2004,Classic Cars,140,S24_3856,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10266,24,100,9,2932.08,7/6/2004 0:00,Shipped,3,7,2004,Classic Cars,140,S24_3856,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10278,25,100,9,3159.75,8/6/2004 0:00,Shipped,3,8,2004,Classic Cars,140,S24_3856,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Medium
10287,36,100,7,4297.32,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,140,S24_3856,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10301,50,100,11,7723.5,10/5/2003 0:00,Shipped,4,10,2003,Classic Cars,140,S24_3856,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Large
10310,45,100,5,5497.65,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,140,S24_3856,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10321,26,100,13,4052.88,11/4/2004 0:00,Shipped,4,11,2004,Classic Cars,140,S24_3856,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10331,21,100,1,3135.93,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,140,S24_3856,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10342,42,100,6,5013.54,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,140,S24_3856,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10355,32,100,8,5302.72,12/7/2004 0:00,Shipped,4,12,2004,Classic Cars,140,S24_3856,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10363,31,94.58,1,2931.98,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,140,S24_3856,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10378,33,53.27,3,1757.91,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,140,S24_3856,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10390,45,100,8,6763.05,3/4/2005 0:00,Shipped,1,3,2005,Classic Cars,140,S24_3856,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10405,76,100,3,11739.7,4/14/2005 0:00,Shipped,2,4,2005,Classic Cars,140,S24_3856,Mini Caravy,88.60.1555,"24, place Kluber",,Strasbourg,,67000,France,EMEA,Citeaux,Frederique,Large
10419,70,100,8,9240,5/17/2005 0:00,Shipped,2,5,2005,Classic Cars,140,S24_3856,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Large
10106,50,64.83,11,3241.5,2/17/2003 0:00,Shipped,1,2,2003,Planes,68,S24_3949,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10119,28,70.29,2,1968.12,4/28/2003 0:00,Shipped,2,4,2003,Planes,68,S24_3949,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10131,50,81.89,3,4094.5,6/16/2003 0:00,Shipped,2,6,2003,Planes,68,S24_3949,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10143,28,66.19,6,1853.32,8/10/2003 0:00,Shipped,3,8,2003,Planes,68,S24_3949,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10155,44,77.11,4,3392.84,10/6/2003 0:00,Shipped,4,10,2003,Planes,68,S24_3949,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10168,27,73.02,18,1971.54,10/28/2003 0:00,Shipped,4,10,2003,Planes,68,S24_3949,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10178,30,72.33,3,2169.9,11/8/2003 0:00,Shipped,4,11,2003,Planes,68,S24_3949,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Small
10198,43,66.19,3,2846.17,11/27/2003 0:00,Shipped,4,11,2003,Planes,68,S24_3949,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10210,29,69.6,16,2018.4,1/12/2004 0:00,Shipped,1,1,2004,Planes,68,S24_3949,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10222,48,56.64,3,2718.72,2/19/2004 0:00,Shipped,1,2,2004,Planes,68,S24_3949,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10235,33,60.05,12,1981.65,4/2/2004 0:00,Shipped,2,4,2004,Planes,68,S24_3949,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10250,40,75.06,13,3002.4,5/11/2004 0:00,Shipped,2,5,2004,Planes,68,S24_3949,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10262,48,61.42,8,2948.16,6/24/2004 0:00,Cancelled,2,6,2004,Planes,68,S24_3949,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10275,41,81.89,18,3357.49,7/23/2004 0:00,Shipped,3,7,2004,Planes,68,S24_3949,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10284,21,55.96,10,1175.16,8/21/2004 0:00,Shipped,3,8,2004,Planes,68,S24_3949,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10296,32,71.65,6,2292.8,9/15/2004 0:00,Shipped,3,9,2004,Planes,68,S24_3949,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10308,43,76.43,16,3286.49,10/15/2004 0:00,Shipped,4,10,2004,Planes,68,S24_3949,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10316,30,77.79,8,2333.7,11/1/2004 0:00,Shipped,4,11,2004,Planes,68,S24_3949,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10328,35,76.43,3,2675.05,11/12/2004 0:00,Shipped,4,11,2004,Planes,68,S24_3949,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10339,45,96.92,11,4361.4,11/23/2004 0:00,Shipped,4,11,2004,Planes,68,S24_3949,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10351,34,59.37,3,2018.58,12/3/2004 0:00,Shipped,4,12,2004,Planes,68,S24_3949,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10361,26,100,7,3710.98,12/17/2004 0:00,Shipped,4,12,2004,Planes,68,S24_3949,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10373,39,73,13,2847,1/31/2005 0:00,Shipped,1,1,2005,Planes,68,S24_3949,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10386,41,73.32,12,3006.12,3/1/2005 0:00,Resolved,1,3,2005,Planes,68,S24_3949,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10398,41,68.24,2,2797.84,3/30/2005 0:00,Shipped,1,3,2005,Planes,68,S24_3949,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10401,64,60.05,12,3843.2,4/3/2005 0:00,On Hold,2,4,2005,Planes,68,S24_3949,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Medium
10416,18,75.06,13,1351.08,5/10/2005 0:00,Shipped,2,5,2005,Planes,68,S24_3949,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10100,49,34.47,1,1689.03,1/6/2003 0:00,Shipped,1,1,2003,Vintage Cars,41,S24_3969,Online Diecast Creations Co.,6035558647,2304 Long Airport Avenue,,Nashua,NH,62005,USA,NA,Young,Valarie,Small
10110,48,34.47,5,1654.56,3/18/2003 0:00,Shipped,1,3,2003,Vintage Cars,41,S24_3969,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10124,46,33.23,4,1528.58,5/21/2003 0:00,Shipped,2,5,2003,Vintage Cars,41,S24_3969,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10149,26,38.98,9,1013.48,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,41,S24_3969,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Small
10162,37,38.98,7,1442.26,10/18/2003 0:00,Shipped,4,10,2003,Vintage Cars,41,S24_3969,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10173,35,33.23,11,1163.05,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,41,S24_3969,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10182,23,42.26,8,971.98,11/12/2003 0:00,Shipped,4,11,2003,Vintage Cars,41,S24_3969,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10193,22,41.03,12,902.66,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,41,S24_3969,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10204,39,33.23,2,1295.97,12/2/2003 0:00,Shipped,4,12,2003,Vintage Cars,41,S24_3969,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10214,44,34.88,5,1534.72,1/26/2004 0:00,Shipped,1,1,2004,Vintage Cars,41,S24_3969,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10227,27,43.9,8,1185.3,3/2/2004 0:00,Shipped,1,3,2004,Vintage Cars,41,S24_3969,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10242,46,36.93,1,1698.78,4/20/2004 0:00,Shipped,2,4,2004,Vintage Cars,41,S24_3969,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Small
10280,33,41.85,14,1381.05,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,41,S24_3969,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10288,33,40.62,3,1340.46,9/1/2004 0:00,Shipped,3,9,2004,Vintage Cars,41,S24_3969,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10303,24,40.21,1,965.04,10/6/2004 0:00,Shipped,4,10,2004,Vintage Cars,41,S24_3969,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Small
10312,31,35.29,15,1093.99,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,41,S24_3969,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10332,41,77.24,14,3166.84,11/17/2004 0:00,Shipped,4,11,2004,Vintage Cars,41,S24_3969,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10346,22,97.44,4,2143.68,11/29/2004 0:00,Shipped,4,11,2004,Vintage Cars,41,S24_3969,Signal Gift Stores,7025551838,8489 Strong St.,,Las Vegas,NV,83030,USA,NA,King,Sue,Small
10368,46,37.34,3,1717.64,1/19/2005 0:00,Shipped,1,1,2005,Vintage Cars,41,S24_3969,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10380,43,95.03,12,4086.29,2/16/2005 0:00,Shipped,1,2,2005,Vintage Cars,41,S24_3969,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10408,15,36.93,1,553.95,4/22/2005 0:00,Shipped,2,4,2005,Vintage Cars,41,S24_3969,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10420,15,43.49,3,652.35,5/29/2005 0:00,In Process,2,5,2005,Vintage Cars,41,S24_3969,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10104,26,100,5,2921.62,1/31/2003 0:00,Shipped,1,1,2003,Classic Cars,118,S24_4048,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10115,44,100,1,5568.64,4/4/2003 0:00,Shipped,2,4,2003,Classic Cars,118,S24_4048,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10127,20,96.99,7,1939.8,6/3/2003 0:00,Shipped,2,6,2003,Classic Cars,118,S24_4048,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10141,40,94.62,1,3784.8,8/1/2003 0:00,Shipped,3,8,2003,Classic Cars,118,S24_4048,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10152,23,100,3,2802.09,9/25/2003 0:00,Shipped,3,9,2003,Classic Cars,118,S24_4048,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Small
10165,24,99.36,8,2384.64,10/22/2003 0:00,Shipped,4,10,2003,Classic Cars,118,S24_4048,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10176,29,100,7,2915.66,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,118,S24_4048,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10184,49,100,2,5795.72,11/14/2003 0:00,Shipped,4,11,2003,Classic Cars,118,S24_4048,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Medium
10195,34,100,2,3699.88,11/25/2003 0:00,Shipped,4,11,2003,Classic Cars,118,S24_4048,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10207,28,100,3,2980.6,12/9/2003 0:00,Shipped,4,12,2003,Classic Cars,118,S24_4048,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Small
10220,37,100,7,5032.74,2/12/2004 0:00,Shipped,1,2,2004,Classic Cars,118,S24_4048,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Medium
10230,45,100,5,4737.15,3/15/2004 0:00,Shipped,1,3,2004,Classic Cars,118,S24_4048,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10246,46,100,1,6311.2,5/5/2004 0:00,Shipped,2,5,2004,Classic Cars,118,S24_4048,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10271,22,100,1,3070.54,7/20/2004 0:00,Shipped,3,7,2004,Classic Cars,118,S24_4048,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10282,39,100,10,4797.39,8/20/2004 0:00,Shipped,3,8,2004,Classic Cars,118,S24_4048,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10292,27,100,4,3832.38,9/8/2004 0:00,Shipped,3,9,2004,Classic Cars,118,S24_4048,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10305,36,100,1,4641.48,10/13/2004 0:00,Shipped,4,10,2004,Classic Cars,118,S24_4048,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10314,38,100,10,4000.26,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,118,S24_4048,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10325,44,100,5,5325.76,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,118,S24_4048,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10336,31,100,5,4618.69,11/20/2004 0:00,Shipped,4,11,2004,Classic Cars,118,S24_4048,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10349,23,100,2,3182.97,12/1/2004 0:00,Shipped,4,12,2004,Classic Cars,118,S24_4048,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10359,22,100,7,2603.04,12/15/2004 0:00,Shipped,4,12,2004,Classic Cars,118,S24_4048,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10371,28,50.32,9,1408.96,1/23/2005 0:00,Shipped,1,1,2005,Classic Cars,118,S24_4048,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10383,21,93.91,4,1972.11,2/22/2005 0:00,Shipped,1,2,2005,Classic Cars,118,S24_4048,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10394,37,100,7,5207.75,3/15/2005 0:00,Shipped,1,3,2005,Classic Cars,118,S24_4048,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10412,31,100,1,4253.2,5/3/2005 0:00,Shipped,2,5,2005,Classic Cars,118,S24_4048,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10103,25,100,15,2873,1/29/2003 0:00,Shipped,1,1,2003,Vintage Cars,97,S24_4258,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10111,26,86.68,3,2253.68,3/25/2003 0:00,Shipped,1,3,2003,Vintage Cars,97,S24_4258,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10126,34,100,15,3576.12,5/28/2003 0:00,Shipped,2,5,2003,Vintage Cars,97,S24_4258,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10139,29,100,4,3276.13,7/16/2003 0:00,Shipped,3,7,2003,Vintage Cars,97,S24_4258,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10149,20,90.57,1,1811.4,9/12/2003 0:00,Shipped,3,9,2003,Vintage Cars,97,S24_4258,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Small
10163,42,91.55,5,3845.1,10/20/2003 0:00,Shipped,4,10,2003,Vintage Cars,97,S24_4258,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10173,22,100,3,2571.14,11/5/2003 0:00,Shipped,4,11,2003,Vintage Cars,97,S24_4258,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10183,47,100,12,5035.11,11/13/2003 0:00,Shipped,4,11,2003,Vintage Cars,97,S24_4258,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Medium
10193,20,100,4,2279,11/21/2003 0:00,Shipped,4,11,2003,Vintage Cars,97,S24_4258,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10206,33,97.39,10,3213.87,12/5/2003 0:00,Shipped,4,12,2003,Vintage Cars,97,S24_4258,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10215,39,90.57,7,3532.23,1/29/2004 0:00,Shipped,1,1,2004,Vintage Cars,97,S24_4258,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Medium
10228,33,100,6,3406.59,3/10/2004 0:00,Shipped,1,3,2004,Vintage Cars,97,S24_4258,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Medium
10244,40,86.68,4,3467.2,4/29/2004 0:00,Shipped,2,4,2004,Vintage Cars,97,S24_4258,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10257,46,78.89,4,3628.94,6/14/2004 0:00,Shipped,2,6,2004,Vintage Cars,97,S24_4258,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10269,48,97.39,2,4674.72,7/16/2004 0:00,Shipped,3,7,2004,Vintage Cars,97,S24_4258,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10280,21,78.89,6,1656.69,8/17/2004 0:00,Shipped,3,8,2004,Vintage Cars,97,S24_4258,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10290,45,100,1,5171.4,9/7/2004 0:00,Shipped,3,9,2004,Vintage Cars,97,S24_4258,Auto-Moto Classics Inc.,6175558428,16780 Pompton St.,,Brickhaven,MA,58339,USA,NA,Taylor,Leslie,Medium
10304,33,100,10,3342.57,10/11/2004 0:00,Shipped,4,10,2004,Vintage Cars,97,S24_4258,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Medium
10312,44,100,7,4884.88,10/21/2004 0:00,Shipped,4,10,2004,Vintage Cars,97,S24_4258,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10324,33,100,3,6267.69,11/5/2004 0:00,Shipped,4,11,2004,Vintage Cars,97,S24_4258,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10333,39,100,1,4424.16,11/18/2004 0:00,Shipped,4,11,2004,Vintage Cars,97,S24_4258,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Medium
10348,39,50.31,2,1962.09,11/1/2004 0:00,Shipped,4,11,2004,Vintage Cars,97,S24_4258,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10358,41,100,6,6847,12/10/2004 0:00,Shipped,4,12,2004,Vintage Cars,97,S24_4258,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10369,40,86.92,3,3476.8,1/20/2005 0:00,Shipped,1,1,2005,Vintage Cars,97,S24_4258,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Medium
10382,33,100,4,4592.61,2/17/2005 0:00,Shipped,1,2,2005,Vintage Cars,97,S24_4258,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10423,28,78.89,4,2208.92,5/30/2005 0:00,In Process,2,5,2005,Vintage Cars,97,S24_4258,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10106,26,63.76,3,1657.76,2/17/2003 0:00,Shipped,1,2,2003,Planes,72,S24_4278,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10120,29,85.49,9,2479.21,4/29/2003 0:00,Shipped,2,4,2003,Planes,72,S24_4278,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10133,46,77.52,4,3565.92,6/27/2003 0:00,Shipped,2,6,2003,Planes,72,S24_4278,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10145,33,84.77,15,2797.41,8/25/2003 0:00,Shipped,3,8,2003,Planes,72,S24_4278,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10168,48,78.25,10,3756,10/28/2003 0:00,Shipped,4,10,2003,Planes,72,S24_4278,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10210,40,71,8,2840,1/12/2004 0:00,Shipped,1,1,2004,Planes,72,S24_4278,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10223,23,74.62,10,1716.26,2/20/2004 0:00,Shipped,1,2,2004,Planes,72,S24_4278,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10235,40,81.14,4,3245.6,4/2/2004 0:00,Shipped,2,4,2004,Planes,72,S24_4278,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10250,37,74.62,5,2760.94,5/11/2004 0:00,Shipped,2,5,2004,Planes,72,S24_4278,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10263,24,75.35,11,1808.4,6/28/2004 0:00,Shipped,2,6,2004,Planes,72,S24_4278,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10275,27,62.31,10,1682.37,7/23/2004 0:00,Shipped,3,7,2004,Planes,72,S24_4278,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10284,21,71,2,1491,8/21/2004 0:00,Shipped,3,8,2004,Planes,72,S24_4278,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10297,23,72.45,5,1666.35,9/16/2004 0:00,Shipped,3,9,2004,Planes,72,S24_4278,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Small
10308,44,83.32,8,3666.08,10/15/2004 0:00,Shipped,4,10,2004,Planes,72,S24_4278,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10317,35,83.32,1,2916.2,11/2/2004 0:00,Shipped,4,11,2004,Planes,72,S24_4278,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10328,43,60.86,4,2616.98,11/12/2004 0:00,Shipped,4,11,2004,Planes,72,S24_4278,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10340,40,84.77,1,3390.8,11/24/2004 0:00,Shipped,4,11,2004,Planes,72,S24_4278,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10353,35,89.9,3,3146.5,12/4/2004 0:00,Shipped,4,12,2004,Planes,72,S24_4278,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10361,25,62.46,1,1561.5,12/17/2004 0:00,Shipped,4,12,2004,Planes,72,S24_4278,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10375,43,100,2,10039.6,2/3/2005 0:00,Shipped,1,2,2005,Planes,72,S24_4278,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Large
10386,50,63.34,8,3167,3/1/2005 0:00,Resolved,1,3,2005,Planes,72,S24_4278,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10398,45,78.25,14,3521.25,3/30/2005 0:00,Shipped,1,3,2005,Planes,72,S24_4278,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10401,52,81.14,4,4219.28,4/3/2005 0:00,On Hold,2,4,2005,Planes,72,S24_4278,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Medium
10416,48,74.62,5,3581.76,5/10/2005 0:00,Shipped,2,5,2005,Planes,72,S24_4278,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10108,31,68.71,10,2130.01,3/3/2003 0:00,Shipped,1,3,2003,Classic Cars,80,S24_4620,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10122,29,71.14,14,2063.06,5/8/2003 0:00,Shipped,2,5,2003,Classic Cars,80,S24_4620,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10135,23,87.31,11,2008.13,7/2/2003 0:00,Shipped,3,7,2003,Classic Cars,80,S24_4620,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10147,31,64.67,11,2004.77,9/5/2003 0:00,Shipped,3,9,2003,Classic Cars,80,S24_4620,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10159,23,67.1,6,1543.3,10/10/2003 0:00,Shipped,4,10,2003,Classic Cars,80,S24_4620,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10169,24,94.58,6,2269.92,11/4/2003 0:00,Shipped,4,11,2003,Classic Cars,80,S24_4620,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10180,28,71.14,1,1991.92,11/11/2003 0:00,Shipped,4,11,2003,Classic Cars,80,S24_4620,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10191,44,66.29,7,2916.76,11/20/2003 0:00,Shipped,4,11,2003,Classic Cars,80,S24_4620,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10211,22,92.16,6,2027.52,1/15/2004 0:00,Shipped,1,1,2004,Classic Cars,80,S24_4620,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10225,46,70.33,13,3235.18,2/22/2004 0:00,Shipped,1,2,2004,Classic Cars,80,S24_4620,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10238,22,93.77,7,2062.94,4/9/2004 0:00,Shipped,2,4,2004,Classic Cars,80,S24_4620,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10252,38,87.31,3,3317.78,5/26/2004 0:00,Shipped,2,5,2004,Classic Cars,80,S24_4620,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10264,47,83.27,1,3913.69,6/30/2004 0:00,Shipped,2,6,2004,Classic Cars,80,S24_4620,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10276,48,75.18,7,3608.64,8/2/2004 0:00,Shipped,3,8,2004,Classic Cars,80,S24_4620,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Medium
10287,40,88.12,16,3524.8,8/30/2004 0:00,Shipped,3,8,2004,Classic Cars,80,S24_4620,"Vida Sport, Ltd",0897-034555,Grenzacherweg 237,,Gensve,,1203,Switzerland,EMEA,Holz,Michael,Medium
10299,32,80.84,1,2586.88,9/30/2004 0:00,Shipped,3,9,2004,Classic Cars,80,S24_4620,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10310,49,97.01,14,4753.49,10/16/2004 0:00,Shipped,4,10,2004,Classic Cars,80,S24_4620,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Medium
10319,43,85.69,2,3684.67,11/3/2004 0:00,Shipped,4,11,2004,Classic Cars,80,S24_4620,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Medium
10331,41,100,2,5715.4,11/17/2004 0:00,Shipped,4,11,2004,Classic Cars,80,S24_4620,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10343,30,100,1,3098.7,11/24/2004 0:00,Shipped,4,11,2004,Classic Cars,80,S24_4620,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10355,28,95.39,9,2670.92,12/7/2004 0:00,Shipped,4,12,2004,Classic Cars,80,S24_4620,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10363,43,100,9,5154.41,1/6/2005 0:00,Shipped,1,1,2005,Classic Cars,80,S24_4620,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10378,41,100,2,4894.17,2/10/2005 0:00,Shipped,1,2,2005,Classic Cars,80,S24_4620,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10390,30,82.42,10,2472.6,3/4/2005 0:00,Shipped,1,3,2005,Classic Cars,80,S24_4620,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10103,31,100,3,3224.31,1/29/2003 0:00,Shipped,1,1,2003,Trucks and Buses,96,S32_1268,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10114,32,100,7,3667.52,4/1/2003 0:00,Shipped,2,4,2003,Trucks and Buses,96,S32_1268,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10126,43,96.31,3,4141.33,5/28/2003 0:00,Shipped,2,5,2003,Trucks and Buses,96,S32_1268,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10140,26,100,3,2829.58,7/24/2003 0:00,Shipped,3,7,2003,Trucks and Buses,96,S32_1268,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10151,27,100,10,3068.55,9/21/2003 0:00,Shipped,3,9,2003,Trucks and Buses,96,S32_1268,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10164,24,100,1,2634.96,10/21/2003 0:00,Resolved,4,10,2003,Trucks and Buses,96,S32_1268,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Small
10175,22,100,8,2436.72,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,96,S32_1268,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10184,46,100,13,4607.36,11/14/2003 0:00,Shipped,4,11,2003,Trucks and Buses,96,S32_1268,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Medium
10194,37,97.27,3,3598.99,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,96,S32_1268,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10207,49,80.9,14,3964.1,12/9/2003 0:00,Shipped,4,12,2003,Trucks and Buses,96,S32_1268,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Medium
10217,21,100,3,2244.9,2/4/2004 0:00,Shipped,1,2,2004,Trucks and Buses,96,S32_1268,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10229,25,100,8,2793,3/11/2004 0:00,Shipped,1,3,2004,Trucks and Buses,96,S32_1268,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10245,37,100,1,4133.64,5/4/2004 0:00,Shipped,2,5,2004,Trucks and Buses,96,S32_1268,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10259,45,86.68,11,3900.6,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,96,S32_1268,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10270,32,85.72,1,2743.04,7/19/2004 0:00,Shipped,3,7,2004,Trucks and Buses,96,S32_1268,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10281,29,82.83,8,2402.07,8/19/2004 0:00,Shipped,3,8,2004,Trucks and Buses,96,S32_1268,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10291,26,83.79,3,2178.54,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,96,S32_1268,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10305,28,100,12,3155.04,10/13/2004 0:00,Shipped,4,10,2004,Trucks and Buses,96,S32_1268,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10313,27,87.64,6,2366.28,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,96,S32_1268,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10324,20,98.18,11,1963.6,11/5/2004 0:00,Shipped,4,11,2004,Trucks and Buses,96,S32_1268,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10335,44,100,1,4746.28,11/19/2004 0:00,Shipped,4,11,2004,Trucks and Buses,96,S32_1268,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10348,42,100,3,6386.94,11/1/2004 0:00,Shipped,4,11,2004,Trucks and Buses,96,S32_1268,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10358,41,100,1,4428,12/10/2004 0:00,Shipped,4,12,2004,Trucks and Buses,96,S32_1268,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10371,26,100,1,4044.04,1/23/2005 0:00,Shipped,1,1,2005,Trucks and Buses,96,S32_1268,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10382,26,100,6,2708.42,2/17/2005 0:00,Shipped,1,2,2005,Trucks and Buses,96,S32_1268,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10411,26,100,1,2904.72,5/1/2005 0:00,Shipped,2,5,2005,Trucks and Buses,96,S32_1268,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Small
10425,41,86.68,11,3553.88,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,96,S32_1268,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10107,20,92.9,8,1858,2/24/2003 0:00,Shipped,1,2,2003,Motorcycles,99,S32_1374,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10120,22,100,6,2461.36,4/29/2003 0:00,Shipped,2,4,2003,Motorcycles,99,S32_1374,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10133,23,100,1,2642.01,6/27/2003 0:00,Shipped,2,6,2003,Motorcycles,99,S32_1374,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10145,33,93.9,12,3098.7,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,99,S32_1374,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10168,28,100,7,3244.36,10/28/2003 0:00,Shipped,4,10,2003,Motorcycles,99,S32_1374,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10188,44,98.89,7,4351.16,11/18/2003 0:00,Shipped,4,11,2003,Motorcycles,99,S32_1374,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10210,46,79.91,5,3675.86,1/12/2004 0:00,Shipped,1,1,2004,Motorcycles,99,S32_1374,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Medium
10223,21,100,7,2475.27,2/20/2004 0:00,Shipped,1,2,2004,Motorcycles,99,S32_1374,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10235,41,100,1,4177.49,4/2/2004 0:00,Shipped,2,4,2004,Motorcycles,99,S32_1374,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10250,31,100,2,3282.28,5/11/2004 0:00,Shipped,2,5,2004,Motorcycles,99,S32_1374,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10263,31,79.91,8,2477.21,6/28/2004 0:00,Shipped,2,6,2004,Motorcycles,99,S32_1374,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10275,23,81.91,7,1883.93,7/23/2004 0:00,Shipped,3,7,2004,Motorcycles,99,S32_1374,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10285,37,98.89,12,3658.93,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,99,S32_1374,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10297,26,100,2,2856.88,9/16/2004 0:00,Shipped,3,9,2004,Motorcycles,99,S32_1374,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Small
10308,24,79.91,5,1917.84,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,99,S32_1374,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10318,47,100,7,5305.36,11/2/2004 0:00,Shipped,4,11,2004,Motorcycles,99,S32_1374,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Medium
10329,45,63.91,11,2875.95,11/15/2004 0:00,Shipped,4,11,2004,Motorcycles,99,S32_1374,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10340,55,100,2,6482.85,11/24/2004 0:00,Shipped,4,11,2004,Motorcycles,99,S32_1374,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10353,46,81.17,5,3733.82,12/4/2004 0:00,Shipped,4,12,2004,Motorcycles,99,S32_1374,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10363,50,100,2,6576.5,1/6/2005 0:00,Shipped,1,1,2005,Motorcycles,99,S32_1374,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10375,37,100,3,6353.27,2/3/2005 0:00,Shipped,1,2,2005,Motorcycles,99,S32_1374,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10387,44,94.9,1,4175.6,3/2/2005 0:00,Shipped,1,3,2005,Motorcycles,99,S32_1374,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10401,49,100,1,4992.61,4/3/2005 0:00,On Hold,2,4,2005,Motorcycles,99,S32_1374,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Medium
10416,45,100,2,4764.6,5/10/2005 0:00,Shipped,2,5,2005,Motorcycles,99,S32_1374,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10108,27,43.45,13,1173.15,3/3/2003 0:00,Shipped,1,3,2003,Motorcycles,40,S32_2206,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10122,31,44.66,17,1384.46,5/8/2003 0:00,Shipped,2,5,2003,Motorcycles,40,S32_2206,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10135,33,40.23,14,1327.59,7/2/2003 0:00,Shipped,3,7,2003,Motorcycles,40,S32_2206,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10145,31,35.8,1,1109.8,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,40,S32_2206,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10159,35,35.4,9,1239,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,40,S32_2206,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10169,26,39.83,9,1035.58,11/4/2003 0:00,Shipped,4,11,2003,Motorcycles,40,S32_2206,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Small
10180,34,45.46,4,1545.64,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,40,S32_2206,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10190,46,32.99,1,1517.54,11/19/2003 0:00,Shipped,4,11,2003,Motorcycles,40,S32_2206,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10211,41,42.24,9,1731.84,1/15/2004 0:00,Shipped,1,1,2004,Motorcycles,40,S32_2206,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10224,43,39.43,2,1695.49,2/21/2004 0:00,Shipped,1,2,2004,Motorcycles,40,S32_2206,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10237,26,40.23,2,1045.98,4/5/2004 0:00,Shipped,2,4,2004,Motorcycles,40,S32_2206,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10252,36,48.28,6,1738.08,5/26/2004 0:00,Shipped,2,5,2004,Motorcycles,40,S32_2206,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10264,20,32.59,4,651.8,6/30/2004 0:00,Shipped,2,6,2004,Motorcycles,40,S32_2206,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10276,27,36.61,10,988.47,8/2/2004 0:00,Shipped,3,8,2004,Motorcycles,40,S32_2206,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Small
10285,37,41.03,1,1518.11,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,40,S32_2206,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10299,24,42.24,4,1013.76,9/30/2004 0:00,Shipped,3,9,2004,Motorcycles,40,S32_2206,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10310,36,43.05,17,1549.8,10/16/2004 0:00,Shipped,4,10,2004,Motorcycles,40,S32_2206,"Toms Spezialitten, Ltd",0221-5554327,Mehrheimerstr. 369,,Koln,,50739,Germany,EMEA,Pfalzheim,Henriette,Small
10319,29,38.22,5,1108.38,11/3/2004 0:00,Shipped,4,11,2004,Motorcycles,40,S32_2206,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Small
10331,28,100,3,4102.56,11/17/2004 0:00,Shipped,4,11,2004,Motorcycles,40,S32_2206,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10343,29,100,5,3713.16,11/24/2004 0:00,Shipped,4,11,2004,Motorcycles,40,S32_2206,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10355,38,39.83,10,1513.54,12/7/2004 0:00,Shipped,4,12,2004,Motorcycles,40,S32_2206,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10364,48,48.28,1,2317.44,1/6/2005 0:00,Shipped,1,1,2005,Motorcycles,40,S32_2206,Marseille Mini Autos,91.24.4555,"12, rue des Bouchers",,Marseille,,13008,France,EMEA,Lebihan,Laurence,Small
10378,40,82.46,1,3298.4,2/10/2005 0:00,Shipped,1,2,2005,Motorcycles,40,S32_2206,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10390,41,44.56,11,1826.96,3/4/2005 0:00,Shipped,1,3,2005,Motorcycles,40,S32_2206,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10403,30,40.23,2,1206.9,4/8/2005 0:00,Shipped,2,4,2005,Motorcycles,40,S32_2206,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10104,35,47.62,11,1666.7,1/31/2003 0:00,Shipped,1,1,2003,Trucks and Buses,54,S32_2509,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10114,28,55.73,2,1560.44,4/1/2003 0:00,Shipped,2,4,2003,Trucks and Buses,54,S32_2509,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Small
10127,45,51.95,13,2337.75,6/3/2003 0:00,Shipped,2,6,2003,Trucks and Buses,54,S32_2509,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10141,24,45.99,7,1103.76,8/1/2003 0:00,Shipped,3,8,2003,Trucks and Buses,54,S32_2509,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10151,41,63.85,5,2617.85,9/21/2003 0:00,Shipped,3,9,2003,Trucks and Buses,54,S32_2509,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10165,48,45.99,14,2207.52,10/22/2003 0:00,Shipped,4,10,2003,Trucks and Buses,54,S32_2509,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10175,50,63.31,3,3165.5,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,54,S32_2509,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10184,33,62.77,8,2071.41,11/14/2003 0:00,Shipped,4,11,2003,Trucks and Buses,54,S32_2509,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Small
10195,32,43.29,8,1385.28,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,54,S32_2509,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10207,27,60.06,9,1621.62,12/9/2003 0:00,Shipped,4,12,2003,Trucks and Buses,54,S32_2509,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Small
10219,35,55.19,4,1931.65,2/10/2004 0:00,Shipped,1,2,2004,Trucks and Buses,54,S32_2509,Signal Collectibles Ltd.,4155554312,2793 Furth Circle,,Brisbane,CA,94217,USA,NA,Taylor,Sue,Small
10229,23,54.11,3,1244.53,3/11/2004 0:00,Shipped,1,3,2004,Trucks and Buses,54,S32_2509,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10246,35,48.7,7,1704.5,5/5/2004 0:00,Shipped,2,5,2004,Trucks and Buses,54,S32_2509,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10259,40,43.83,6,1753.2,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,54,S32_2509,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10271,35,47.62,7,1666.7,7/20/2004 0:00,Shipped,3,7,2004,Trucks and Buses,54,S32_2509,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10281,31,55.19,3,1710.89,8/19/2004 0:00,Shipped,3,8,2004,Trucks and Buses,54,S32_2509,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10292,50,46.53,10,2326.5,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,54,S32_2509,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10305,40,57.9,7,2316,10/13/2004 0:00,Shipped,4,10,2004,Trucks and Buses,54,S32_2509,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10313,38,45.45,1,1727.1,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,54,S32_2509,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10325,38,100,3,8844.12,11/5/2004 0:00,Shipped,4,11,2004,Trucks and Buses,54,S32_2509,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Large
10335,40,60.6,3,2424,11/19/2004 0:00,Shipped,4,11,2004,Trucks and Buses,54,S32_2509,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10349,33,46.53,1,1535.49,12/1/2004 0:00,Shipped,4,12,2004,Trucks and Buses,54,S32_2509,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10359,36,100,3,6358.68,12/15/2004 0:00,Shipped,4,12,2004,Trucks and Buses,54,S32_2509,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10371,20,66.47,2,1329.4,1/23/2005 0:00,Shipped,1,1,2005,Trucks and Buses,54,S32_2509,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10383,32,53.18,5,1701.76,2/22/2005 0:00,Shipped,1,2,2005,Trucks and Buses,54,S32_2509,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10394,36,62.77,3,2259.72,3/15/2005 0:00,Shipped,1,3,2005,Trucks and Buses,54,S32_2509,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10412,19,48.7,7,925.3,5/3/2005 0:00,Shipped,2,5,2005,Trucks and Buses,54,S32_2509,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10425,11,43.83,6,482.13,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,54,S32_2509,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10104,49,65.87,4,3227.63,1/31/2003 0:00,Shipped,1,1,2003,Trains,62,S32_3207,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10116,27,63.38,1,1711.26,4/11/2003 0:00,Shipped,2,4,2003,Trains,62,S32_3207,Royale Belge,(071) 23 67 2555,"Boulevard Tirou, 255",,Charleroi,,B-6000,Belgium,EMEA,Cartrain,Pascale,Small
10127,29,70.84,6,2054.36,6/3/2003 0:00,Shipped,2,6,2003,Trains,62,S32_3207,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Small
10142,42,74.57,16,3131.94,8/8/2003 0:00,Shipped,3,8,2003,Trains,62,S32_3207,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10152,33,50.95,2,1681.35,9/25/2003 0:00,Shipped,3,9,2003,Trains,62,S32_3207,"Australian Gift Network, Co",61-7-3844-6555,31 Duncan St. West End,,South Brisbane,Queensland,4101,Australia,APAC,Calaghan,Tony,Small
10165,44,53.44,7,2351.36,10/22/2003 0:00,Shipped,4,10,2003,Trains,62,S32_3207,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10176,22,64,6,1408,11/6/2003 0:00,Shipped,4,11,2003,Trains,62,S32_3207,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10184,48,50.95,1,2445.6,11/14/2003 0:00,Shipped,4,11,2003,Trains,62,S32_3207,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Small
10195,33,54.68,1,1804.44,11/25/2003 0:00,Shipped,4,11,2003,Trains,62,S32_3207,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10207,45,56.55,2,2544.75,12/9/2003 0:00,Shipped,4,12,2003,Trains,62,S32_3207,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Small
10220,20,52.82,6,1056.4,2/12/2004 0:00,Shipped,1,2,2004,Trains,62,S32_3207,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Small
10230,46,60.9,4,2801.4,3/15/2004 0:00,Shipped,1,3,2004,Trains,62,S32_3207,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Small
10247,40,49.71,6,1988.4,5/5/2004 0:00,Shipped,2,5,2004,Trains,62,S32_3207,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Small
10272,45,64.63,6,2908.35,7/20/2004 0:00,Shipped,3,7,2004,Trains,62,S32_3207,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10282,36,59.65,9,2147.4,8/20/2004 0:00,Shipped,3,8,2004,Trains,62,S32_3207,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10292,31,67.73,3,2099.63,9/8/2004 0:00,Shipped,3,9,2004,Trains,62,S32_3207,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10306,46,50.33,17,2315.18,10/14/2004 0:00,Shipped,4,10,2004,Trains,62,S32_3207,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10314,35,66.49,9,2327.15,10/22/2004 0:00,Shipped,4,10,2004,Trains,62,S32_3207,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10325,28,100,2,5377.4,11/5/2004 0:00,Shipped,4,11,2004,Trains,62,S32_3207,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10336,31,84.71,9,2626.01,11/20/2004 0:00,Shipped,4,11,2004,Trains,62,S32_3207,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Small
10350,27,100,14,4406.4,12/2/2004 0:00,Shipped,4,12,2004,Trains,62,S32_3207,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10359,22,100,1,4301.22,12/15/2004 0:00,Shipped,4,12,2004,Trains,62,S32_3207,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10371,30,99.55,11,2986.5,1/23/2005 0:00,Shipped,1,1,2005,Trains,62,S32_3207,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10383,44,36.07,8,1587.08,2/22/2005 0:00,Shipped,1,2,2005,Trains,62,S32_3207,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10394,30,60.28,4,1808.4,3/15/2005 0:00,Shipped,1,3,2005,Trains,62,S32_3207,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10413,24,49.71,6,1193.04,5/5/2005 0:00,Shipped,2,5,2005,Trains,62,S32_3207,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Small
10103,45,75.63,7,3403.35,1/29/2003 0:00,Shipped,1,1,2003,Trucks and Buses,64,S32_3522,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10113,23,68.52,1,1575.96,3/26/2003 0:00,Shipped,1,3,2003,Trucks and Buses,64,S32_3522,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10126,26,62.7,7,1630.2,5/28/2003 0:00,Shipped,2,5,2003,Trucks and Buses,64,S32_3522,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10140,28,60.76,7,1701.28,7/24/2003 0:00,Shipped,3,7,2003,Trucks and Buses,64,S32_3522,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10150,49,58.18,4,2850.82,9/19/2003 0:00,Shipped,3,9,2003,Trucks and Buses,64,S32_3522,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10164,49,54.94,5,2692.06,10/21/2003 0:00,Resolved,4,10,2003,Trucks and Buses,64,S32_3522,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Small
10175,29,74.98,12,2174.42,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,64,S32_3522,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10183,49,64.64,4,3167.36,11/13/2003 0:00,Shipped,4,11,2003,Trucks and Buses,64,S32_3522,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Medium
10194,39,54.94,7,2142.66,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,64,S32_3522,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10206,36,58.82,2,2117.52,12/5/2003 0:00,Shipped,4,12,2003,Trucks and Buses,64,S32_3522,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10217,39,62.05,7,2419.95,2/4/2004 0:00,Shipped,1,2,2004,Trucks and Buses,64,S32_3522,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10229,30,73.04,12,2191.2,3/11/2004 0:00,Shipped,1,3,2004,Trucks and Buses,64,S32_3522,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10245,44,69.16,5,3043.04,5/4/2004 0:00,Shipped,2,5,2004,Trucks and Buses,64,S32_3522,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10258,20,61.41,2,1228.2,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,64,S32_3522,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10270,21,63.35,5,1330.35,7/19/2004 0:00,Shipped,3,7,2004,Trucks and Buses,64,S32_3522,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10281,36,77.57,12,2792.52,8/19/2004 0:00,Shipped,3,8,2004,Trucks and Buses,64,S32_3522,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10291,32,71.75,7,2296,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,64,S32_3522,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10304,36,73.04,2,2629.44,10/11/2004 0:00,Shipped,4,10,2004,Trucks and Buses,64,S32_3522,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Small
10313,34,56.24,10,1912.16,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,64,S32_3522,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10324,48,100,4,8209.44,11/5/2004 0:00,Shipped,4,11,2004,Trucks and Buses,64,S32_3522,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Large
10333,33,73.69,4,2431.77,11/18/2004 0:00,Shipped,4,11,2004,Trucks and Buses,64,S32_3522,Mini Wheels Co.,6505555787,5557 North Pendale Street,,San Francisco,CA,,USA,NA,Murphy,Julie,Small
10348,31,100,5,3139.99,11/1/2004 0:00,Shipped,4,11,2004,Trucks and Buses,64,S32_3522,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10358,36,100,2,5669.64,12/10/2004 0:00,Shipped,4,12,2004,Trucks and Buses,64,S32_3522,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10370,25,100,3,3160.25,1/20/2005 0:00,Shipped,1,1,2005,Trucks and Buses,64,S32_3522,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10382,48,100,8,6799.68,2/17/2005 0:00,Shipped,1,2,2005,Trucks and Buses,64,S32_3522,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10411,27,69.16,5,1867.32,5/1/2005 0:00,Shipped,2,5,2005,Trucks and Buses,64,S32_3522,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Small
10424,44,61.41,2,2702.04,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,64,S32_3522,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10106,33,72.92,5,2406.36,2/17/2003 0:00,Shipped,1,2,2003,Vintage Cars,68,S32_4289,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10120,29,72.23,11,2094.67,4/29/2003 0:00,Shipped,2,4,2003,Vintage Cars,68,S32_4289,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10133,49,57.1,6,2797.9,6/27/2003 0:00,Shipped,2,6,2003,Vintage Cars,68,S32_4289,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10144,20,81.86,1,1637.2,8/13/2003 0:00,Shipped,3,8,2003,Vintage Cars,68,S32_4289,Royale Belge,(071) 23 67 2555,"Boulevard Tirou, 255",,Charleroi,,B-6000,Belgium,EMEA,Cartrain,Pascale,Small
10168,31,73.61,12,2281.91,10/28/2003 0:00,Shipped,4,10,2003,Vintage Cars,68,S32_4289,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10210,39,59.16,10,2307.24,1/12/2004 0:00,Shipped,1,1,2004,Vintage Cars,68,S32_4289,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10223,20,66.04,12,1320.8,2/20/2004 0:00,Shipped,1,2,2004,Vintage Cars,68,S32_4289,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10235,34,77.73,6,2642.82,4/2/2004 0:00,Shipped,2,4,2004,Vintage Cars,68,S32_4289,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10250,50,61.22,7,3061,5/11/2004 0:00,Shipped,2,5,2004,Vintage Cars,68,S32_4289,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10262,40,79.11,2,3164.4,6/24/2004 0:00,Cancelled,2,6,2004,Vintage Cars,68,S32_4289,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10275,28,63.97,12,1791.16,7/23/2004 0:00,Shipped,3,7,2004,Vintage Cars,68,S32_4289,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10284,50,81.86,4,4093,8/21/2004 0:00,Shipped,3,8,2004,Vintage Cars,68,S32_4289,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Medium
10297,28,79.8,7,2234.4,9/16/2004 0:00,Shipped,3,9,2004,Vintage Cars,68,S32_4289,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Small
10308,46,66.04,10,3037.84,10/15/2004 0:00,Shipped,4,10,2004,Vintage Cars,68,S32_4289,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10316,24,59.16,2,1419.84,11/1/2004 0:00,Shipped,4,11,2004,Vintage Cars,68,S32_4289,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10328,24,81.17,5,1948.08,11/12/2004 0:00,Shipped,4,11,2004,Vintage Cars,68,S32_4289,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10340,39,59.16,3,2307.24,11/24/2004 0:00,Shipped,4,11,2004,Vintage Cars,68,S32_4289,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10353,40,44.51,7,1780.4,12/4/2004 0:00,Shipped,4,12,2004,Vintage Cars,68,S32_4289,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Small
10361,49,72.33,2,3544.17,12/17/2004 0:00,Shipped,4,12,2004,Vintage Cars,68,S32_4289,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10375,44,82.26,4,3619.44,2/3/2005 0:00,Shipped,1,2,2005,Vintage Cars,68,S32_4289,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10388,35,100,8,3918.95,3/3/2005 0:00,Shipped,1,3,2005,Vintage Cars,68,S32_4289,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10398,22,67.41,4,1483.02,3/30/2005 0:00,Shipped,1,3,2005,Vintage Cars,68,S32_4289,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10401,62,77.73,6,4819.26,4/3/2005 0:00,On Hold,2,4,2005,Vintage Cars,68,S32_4289,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Medium
10416,26,61.22,7,1591.72,5/10/2005 0:00,Shipped,2,5,2005,Vintage Cars,68,S32_4289,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10108,31,100,16,3669.78,3/3/2003 0:00,Shipped,1,3,2003,Motorcycles,102,S32_4485,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10121,25,86.74,3,2168.5,5/7/2003 0:00,Shipped,2,5,2003,Motorcycles,102,S32_4485,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10135,30,89.8,17,2694,7/2/2003 0:00,Shipped,3,7,2003,Motorcycles,102,S32_4485,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10145,27,100,4,3251.34,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,102,S32_4485,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10159,23,100,12,2347.15,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,102,S32_4485,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10169,34,100,12,3920.88,11/4/2003 0:00,Shipped,4,11,2003,Motorcycles,102,S32_4485,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10180,22,100,7,2514.6,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,102,S32_4485,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10190,42,85.72,4,3600.24,11/19/2003 0:00,Shipped,4,11,2003,Motorcycles,102,S32_4485,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10211,37,100,12,4040.03,1/15/2004 0:00,Shipped,1,1,2004,Motorcycles,102,S32_4485,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10224,30,100,5,3336.9,2/21/2004 0:00,Shipped,1,2,2004,Motorcycles,102,S32_4485,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Medium
10237,27,100,5,3113.64,4/5/2004 0:00,Shipped,2,4,2004,Motorcycles,102,S32_4485,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10252,25,100,9,2832,5/26/2004 0:00,Shipped,2,5,2004,Motorcycles,102,S32_4485,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Small
10264,34,97.97,7,3330.98,6/30/2004 0:00,Shipped,2,6,2004,Motorcycles,102,S32_4485,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10276,38,100,13,4304.64,8/2/2004 0:00,Shipped,3,8,2004,Motorcycles,102,S32_4485,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Medium
10285,26,100,4,2600.26,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,102,S32_4485,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Small
10299,38,100,7,4382.16,9/30/2004 0:00,Shipped,3,9,2004,Motorcycles,102,S32_4485,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10309,50,84.7,3,4235,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,102,S32_4485,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10319,22,100,8,2626.8,11/3/2004 0:00,Shipped,4,11,2004,Motorcycles,102,S32_4485,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Small
10331,32,100,4,5026.56,11/17/2004 0:00,Shipped,4,11,2004,Motorcycles,102,S32_4485,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10341,31,71.02,4,2201.62,11/24/2004 0:00,Shipped,4,11,2004,Motorcycles,102,S32_4485,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10355,40,100,5,4326.8,12/7/2004 0:00,Shipped,4,12,2004,Motorcycles,102,S32_4485,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10365,22,100,3,3425.18,1/7/2005 0:00,Shipped,1,1,2005,Motorcycles,102,S32_4485,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10375,41,100,15,4701.88,2/3/2005 0:00,Shipped,1,2,2005,Motorcycles,102,S32_4485,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10390,45,48.98,12,2204.1,3/4/2005 0:00,Shipped,1,3,2005,Motorcycles,102,S32_4485,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10403,45,100,5,5189.4,4/8/2005 0:00,Shipped,2,4,2005,Motorcycles,102,S32_4485,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Medium
10106,39,40.15,6,1565.85,2/17/2003 0:00,Shipped,1,2,2003,Vintage Cars,43,S50_1341,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10120,49,50.62,12,2480.38,4/29/2003 0:00,Shipped,2,4,2003,Vintage Cars,43,S50_1341,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10133,27,50.19,7,1355.13,6/27/2003 0:00,Shipped,2,6,2003,Vintage Cars,43,S50_1341,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10143,34,36.66,1,1246.44,8/10/2003 0:00,Shipped,3,8,2003,Vintage Cars,43,S50_1341,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10156,20,41.02,1,820.4,10/8/2003 0:00,Shipped,4,10,2003,Vintage Cars,43,S50_1341,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10168,48,51.93,13,2492.64,10/28/2003 0:00,Shipped,4,10,2003,Vintage Cars,43,S50_1341,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10199,29,38.4,1,1113.6,12/1/2003 0:00,Shipped,4,12,2003,Vintage Cars,43,S50_1341,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Small
10210,43,41.02,11,1763.86,1/12/2004 0:00,Shipped,1,1,2004,Vintage Cars,43,S50_1341,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10223,41,46.26,13,1896.66,2/20/2004 0:00,Shipped,1,2,2004,Vintage Cars,43,S50_1341,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10235,41,35.35,7,1449.35,4/2/2004 0:00,Shipped,2,4,2004,Vintage Cars,43,S50_1341,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10250,36,51.93,8,1869.48,5/11/2004 0:00,Shipped,2,5,2004,Vintage Cars,43,S50_1341,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10262,49,37.97,3,1860.53,6/24/2004 0:00,Cancelled,2,6,2004,Vintage Cars,43,S50_1341,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10275,38,45.39,13,1724.82,7/23/2004 0:00,Shipped,3,7,2004,Vintage Cars,43,S50_1341,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10284,33,51.93,5,1713.69,8/21/2004 0:00,Shipped,3,8,2004,Vintage Cars,43,S50_1341,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10296,26,48.44,1,1259.44,9/15/2004 0:00,Shipped,3,9,2004,Vintage Cars,43,S50_1341,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10308,47,43.64,11,2051.08,10/15/2004 0:00,Shipped,4,10,2004,Vintage Cars,43,S50_1341,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10316,34,47.57,3,1617.38,11/1/2004 0:00,Shipped,4,11,2004,Vintage Cars,43,S50_1341,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10328,34,51.93,7,1765.62,11/12/2004 0:00,Shipped,4,11,2004,Vintage Cars,43,S50_1341,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10340,40,50.62,4,2024.8,11/24/2004 0:00,Shipped,4,11,2004,Vintage Cars,43,S50_1341,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10353,40,82.21,8,3288.4,12/4/2004 0:00,Shipped,4,12,2004,Vintage Cars,43,S50_1341,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10361,33,82.59,3,2725.47,12/17/2004 0:00,Shipped,4,12,2004,Vintage Cars,43,S50_1341,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10375,49,65.8,5,3224.2,2/3/2005 0:00,Shipped,1,2,2005,Vintage Cars,43,S50_1341,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10388,27,100,1,3211.38,3/3/2005 0:00,Shipped,1,3,2005,Vintage Cars,43,S50_1341,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10398,49,36.66,5,1796.34,3/30/2005 0:00,Shipped,1,3,2005,Vintage Cars,43,S50_1341,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10401,56,35.35,7,1979.6,4/3/2005 0:00,On Hold,2,4,2005,Vintage Cars,43,S50_1341,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Small
10416,37,51.93,8,1921.41,5/10/2005 0:00,Shipped,2,5,2005,Vintage Cars,43,S50_1341,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10104,33,100,7,3705.24,1/31/2003 0:00,Shipped,1,1,2003,Trucks and Buses,115,S50_1392,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10115,27,100,3,2843.91,4/4/2003 0:00,Shipped,2,4,2003,Trucks and Buses,115,S50_1392,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Small
10127,46,100,9,6176.42,6/3/2003 0:00,Shipped,2,6,2003,Trucks and Buses,115,S50_1392,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10141,44,100,3,5500.44,8/1/2003 0:00,Shipped,3,8,2003,Trucks and Buses,115,S50_1392,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10151,26,100,1,3220.1,9/21/2003 0:00,Shipped,3,9,2003,Trucks and Buses,115,S50_1392,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10165,48,94.92,10,4556.16,10/22/2003 0:00,Shipped,4,10,2003,Trucks and Buses,115,S50_1392,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10176,23,100,9,3114.89,11/6/2003 0:00,Shipped,4,11,2003,Trucks and Buses,115,S50_1392,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10184,45,100,4,4948.2,11/14/2003 0:00,Shipped,4,11,2003,Trucks and Buses,115,S50_1392,"Iberia Gift Imports, Corp.",(95) 555 82 82,"C/ Romero, 33",,Sevilla,,41101,Spain,EMEA,Roel,Jose Pedro,Medium
10195,49,100,4,5161.17,11/25/2003 0:00,Shipped,4,11,2003,Trucks and Buses,115,S50_1392,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10207,28,94.92,5,2657.76,12/9/2003 0:00,Shipped,4,12,2003,Trucks and Buses,115,S50_1392,Diecast Collectables,6175552555,6251 Ingle Ln.,,Boston,MA,51003,USA,NA,Franco,Valarie,Small
10220,37,100,9,3983.05,2/12/2004 0:00,Shipped,1,2,2004,Trucks and Buses,115,S50_1392,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Medium
10230,34,100,7,3974.94,3/15/2004 0:00,Shipped,1,3,2004,Trucks and Buses,115,S50_1392,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Medium
10246,22,100,3,2928.42,5/5/2004 0:00,Shipped,2,5,2004,Trucks and Buses,115,S50_1392,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10259,29,100,2,3054.57,6/15/2004 0:00,Shipped,2,6,2004,Trucks and Buses,115,S50_1392,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Medium
10271,34,98.39,3,3345.26,7/20/2004 0:00,Shipped,3,7,2004,Trucks and Buses,115,S50_1392,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10282,38,100,12,4310.72,8/20/2004 0:00,Shipped,3,8,2004,Trucks and Buses,115,S50_1392,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10292,41,100,6,4983.14,9/8/2004 0:00,Shipped,3,9,2004,Trucks and Buses,115,S50_1392,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10305,42,100,3,4618.32,10/13/2004 0:00,Shipped,4,10,2004,Trucks and Buses,115,S50_1392,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10314,28,100,12,3403.12,10/22/2004 0:00,Shipped,4,10,2004,Trucks and Buses,115,S50_1392,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Medium
10325,38,100,4,5190.42,11/5/2004 0:00,Shipped,4,11,2004,Trucks and Buses,115,S50_1392,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10336,23,100,8,3141.57,11/20/2004 0:00,Shipped,4,11,2004,Trucks and Buses,115,S50_1392,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10350,31,71.4,8,2213.4,12/2/2004 0:00,Shipped,4,12,2004,Trucks and Buses,115,S50_1392,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10359,46,100,2,4896.7,12/15/2004 0:00,Shipped,4,12,2004,Trucks and Buses,115,S50_1392,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10371,48,56.55,10,2714.4,1/23/2005 0:00,Shipped,1,1,2005,Trucks and Buses,115,S50_1392,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10383,29,100,13,3087.05,2/22/2005 0:00,Shipped,1,2,2005,Trucks and Buses,115,S50_1392,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10395,46,100,4,5692.96,3/17/2005 0:00,Shipped,1,3,2005,Trucks and Buses,115,S50_1392,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10412,26,100,3,3460.86,5/3/2005 0:00,Shipped,2,5,2005,Trucks and Buses,115,S50_1392,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10425,18,100,2,1895.94,5/31/2005 0:00,In Process,2,5,2005,Trucks and Buses,115,S50_1392,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10104,32,53.31,2,1705.92,1/31/2003 0:00,Shipped,1,1,2003,Trains,58,S50_1514,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10117,21,49.21,11,1033.41,4/16/2003 0:00,Shipped,2,4,2003,Trains,58,S50_1514,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10127,46,69.12,4,3179.52,6/3/2003 0:00,Shipped,2,6,2003,Trains,58,S50_1514,Muscle Machine Inc,2125557413,4092 Furth Circle,Suite 400,NYC,NY,10022,USA,NA,Young,Jeff,Medium
10142,42,49.79,14,2091.18,8/8/2003 0:00,Shipped,3,8,2003,Trains,58,S50_1514,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10153,31,57.41,13,1779.71,9/28/2003 0:00,Shipped,3,9,2003,Trains,58,S50_1514,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10165,38,66.78,5,2537.64,10/22/2003 0:00,Shipped,4,10,2003,Trains,58,S50_1514,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10176,38,64.44,4,2448.72,11/6/2003 0:00,Shipped,4,11,2003,Trains,58,S50_1514,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10185,20,48.62,15,972.4,11/14/2003 0:00,Shipped,4,11,2003,Trains,58,S50_1514,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10196,46,62.09,7,2856.14,11/26/2003 0:00,Shipped,4,11,2003,Trains,58,S50_1514,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Small
10208,30,65.61,15,1968.3,1/2/2004 0:00,Shipped,1,1,2004,Trains,58,S50_1514,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10220,30,68.54,4,2056.2,2/12/2004 0:00,Shipped,1,2,2004,Trains,58,S50_1514,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Small
10230,43,52.14,2,2242.02,3/15/2004 0:00,Shipped,1,3,2004,Trains,58,S50_1514,"Blauer See Auto, Co.",+49 69 66 90 2555,Lyonerstr. 34,,Frankfurt,,60528,Germany,EMEA,Keitel,Roland,Small
10247,49,63.85,4,3128.65,5/5/2004 0:00,Shipped,2,5,2004,Trains,58,S50_1514,Suominen Souveniers,+358 9 8045 555,"Software Engineering Center, SEC Oy",,Espoo,,FIN-02271,Finland,EMEA,Suominen,Kalle,Medium
10272,43,56.82,4,2443.26,7/20/2004 0:00,Shipped,3,7,2004,Trains,58,S50_1514,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10282,37,66.78,7,2470.86,8/20/2004 0:00,Shipped,3,8,2004,Trains,58,S50_1514,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10292,35,55.07,1,1927.45,9/8/2004 0:00,Shipped,3,9,2004,Trains,58,S50_1514,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10306,34,60.34,15,2051.56,10/14/2004 0:00,Shipped,4,10,2004,Trains,58,S50_1514,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10314,38,61.51,7,2337.38,10/22/2004 0:00,Shipped,4,10,2004,Trains,58,S50_1514,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10325,44,100,7,5932.96,11/5/2004 0:00,Shipped,4,11,2004,Trains,58,S50_1514,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10337,21,100,6,2296.77,11/21/2004 0:00,Shipped,4,11,2004,Trains,58,S50_1514,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Small
10350,44,100,17,6490.88,12/2/2004 0:00,Shipped,4,12,2004,Trains,58,S50_1514,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10359,25,64.93,4,1623.25,12/15/2004 0:00,Shipped,4,12,2004,Trains,58,S50_1514,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10372,24,58.58,9,1405.92,1/26/2005 0:00,Shipped,1,1,2005,Trains,58,S50_1514,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10383,38,60.06,10,2282.28,2/22/2005 0:00,Shipped,1,2,2005,Trains,58,S50_1514,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10395,45,100,3,8977.05,3/17/2005 0:00,Shipped,1,3,2005,Trains,58,S50_1514,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Large
10413,51,63.85,4,3256.35,5/5/2005 0:00,Shipped,2,5,2005,Trains,58,S50_1514,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10108,34,82.99,14,2821.66,3/3/2003 0:00,Shipped,1,3,2003,Motorcycles,81,S50_4713,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10121,44,74.85,1,3293.4,5/7/2003 0:00,Shipped,2,5,2003,Motorcycles,81,S50_4713,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10135,44,96,15,4224,7/2/2003 0:00,Shipped,3,7,2003,Motorcycles,81,S50_4713,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10145,38,81.36,2,3091.68,8/25/2003 0:00,Shipped,3,8,2003,Motorcycles,81,S50_4713,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Medium
10159,31,71.6,10,2219.6,10/10/2003 0:00,Shipped,4,10,2003,Motorcycles,81,S50_4713,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Small
10169,48,80.55,10,3866.4,11/4/2003 0:00,Shipped,4,11,2003,Motorcycles,81,S50_4713,"Anna's Decorations, Ltd",02 9936 8555,201 Miller Street,Level 15,North Sydney,NSW,2060,Australia,APAC,O'Hara,Anna,Medium
10180,21,93.56,5,1964.76,11/11/2003 0:00,Shipped,4,11,2003,Motorcycles,81,S50_4713,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Small
10190,40,66.72,2,2668.8,11/19/2003 0:00,Shipped,4,11,2003,Motorcycles,81,S50_4713,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10211,40,80.55,10,3222,1/15/2004 0:00,Shipped,1,1,2004,Motorcycles,81,S50_4713,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10224,50,77.29,3,3864.5,2/21/2004 0:00,Shipped,1,2,2004,Motorcycles,81,S50_4713,Daedalus Designs Imports,20.16.1555,"184, chausse de Tournai",,Lille,,59000,France,EMEA,Rance,Martine,Medium
10237,20,68.34,3,1366.8,4/5/2004 0:00,Shipped,2,4,2004,Motorcycles,81,S50_4713,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Small
10252,48,72.41,7,3475.68,5/26/2004 0:00,Shipped,2,5,2004,Motorcycles,81,S50_4713,Auto Canal Petit,(1) 47.55.6555,"25, rue Lauriston",,Paris,,75016,France,EMEA,Perrier,Dominique,Medium
10264,47,89.5,5,4206.5,6/30/2004 0:00,Shipped,2,6,2004,Motorcycles,81,S50_4713,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10276,21,70.78,11,1486.38,8/2/2004 0:00,Shipped,3,8,2004,Motorcycles,81,S50_4713,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Small
10285,39,78.92,2,3077.88,8/27/2004 0:00,Shipped,3,8,2004,Motorcycles,81,S50_4713,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10299,44,80.55,5,3544.2,9/30/2004 0:00,Shipped,3,9,2004,Motorcycles,81,S50_4713,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10309,28,88.68,1,2483.04,10/15/2004 0:00,Shipped,4,10,2004,Motorcycles,81,S50_4713,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Small
10319,45,77.29,6,3478.05,11/3/2004 0:00,Shipped,4,11,2004,Motorcycles,81,S50_4713,Microscale Inc.,2125551957,5290 North Pendale Street,Suite 200,NYC,NY,10022,USA,NA,Kuo,Kee,Medium
10331,20,100,5,3657.8,11/17/2004 0:00,Shipped,4,11,2004,Motorcycles,81,S50_4713,Motor Mint Distributors Inc.,2155559857,11328 Douglas Av.,,Philadelphia,PA,71270,USA,NA,Hernandez,Rosa,Medium
10341,38,100,3,4682.36,11/24/2004 0:00,Shipped,4,11,2004,Motorcycles,81,S50_4713,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10356,26,100,4,3937.7,12/9/2004 0:00,Shipped,4,12,2004,Motorcycles,81,S50_4713,Lyon Souveniers,+33 1 46 62 7555,27 rue du Colonel Pierre Avia,,Paris,,75508,France,EMEA,Da Cunha,Daniel,Medium
10365,44,100,2,4984.32,1/7/2005 0:00,Shipped,1,1,2005,Motorcycles,81,S50_4713,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10375,49,100,8,5406.66,2/3/2005 0:00,Shipped,1,2,2005,Motorcycles,81,S50_4713,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10390,22,100,13,3491.18,3/4/2005 0:00,Shipped,1,3,2005,Motorcycles,81,S50_4713,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10403,31,68.34,3,2118.54,4/8/2005 0:00,Shipped,2,4,2005,Motorcycles,81,S50_4713,"UK Collectables, Ltd.",(171) 555-2282,Berkeley Gardens 12  Brewery,,Liverpool,,WX1 6LT,UK,EMEA,Devon,Elizabeth,Small
10105,41,70.67,5,2897.47,2/11/2003 0:00,Shipped,1,2,2003,Ships,66,S700_1138,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10119,25,76.67,14,1916.75,4/28/2003 0:00,Shipped,2,4,2003,Ships,66,S700_1138,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10129,31,60,5,1860,6/12/2003 0:00,Shipped,2,6,2003,Ships,66,S700_1138,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10142,41,64,2,2624,8/8/2003 0:00,Shipped,3,8,2003,Ships,66,S700_1138,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10153,43,64.67,1,2780.81,9/28/2003 0:00,Shipped,3,9,2003,Ships,66,S700_1138,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10167,43,75.34,12,3239.62,10/23/2003 0:00,Cancelled,4,10,2003,Ships,66,S700_1138,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10177,24,76,3,1824,11/7/2003 0:00,Shipped,4,11,2003,Ships,66,S700_1138,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Small
10185,21,54,3,1134,11/14/2003 0:00,Shipped,4,11,2003,Ships,66,S700_1138,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10197,23,64.67,9,1487.41,11/26/2003 0:00,Shipped,4,11,2003,Ships,66,S700_1138,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10208,38,74.67,3,2837.46,1/2/2004 0:00,Shipped,1,1,2004,Ships,66,S700_1138,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10222,31,62.67,15,1942.77,2/19/2004 0:00,Shipped,1,2,2004,Ships,66,S700_1138,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10233,36,70.67,3,2544.12,3/29/2004 0:00,Shipped,1,3,2004,Ships,66,S700_1138,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Small
10248,36,71.34,6,2568.24,5/7/2004 0:00,Cancelled,2,5,2004,Ships,66,S700_1138,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10261,34,62,4,2108,6/17/2004 0:00,Shipped,2,6,2004,Ships,66,S700_1138,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Small
10273,21,65.34,7,1372.14,7/21/2004 0:00,Shipped,3,7,2004,Ships,66,S700_1138,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10283,45,78.67,9,3540.15,8/20/2004 0:00,Shipped,3,8,2004,Ships,66,S700_1138,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10295,26,75.34,4,1958.84,9/10/2004 0:00,Shipped,3,9,2004,Ships,66,S700_1138,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10306,50,54,3,2700,10/14/2004 0:00,Shipped,4,10,2004,Ships,66,S700_1138,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10315,41,62,2,2542,10/29/2004 0:00,Shipped,4,10,2004,Ships,66,S700_1138,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10326,39,60,1,2340,11/9/2004 0:00,Shipped,4,11,2004,Ships,66,S700_1138,"Volvo Model Replicas, Co",0921-12 3555,Berguvsv�gen  8,,Lule,,S-958 22,Sweden,EMEA,Berglund,Christina,Small
10339,22,100,5,2816.44,11/23/2004 0:00,Shipped,4,11,2004,Ships,66,S700_1138,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10350,46,76.67,11,3526.82,12/2/2004 0:00,Shipped,4,12,2004,Ships,66,S700_1138,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10373,44,100,14,4627.92,1/31/2005 0:00,Shipped,1,1,2005,Ships,66,S700_1138,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10385,25,77.34,1,1933.5,2/28/2005 0:00,Shipped,1,2,2005,Ships,66,S700_1138,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10396,39,66.67,1,2600.13,3/23/2005 0:00,Shipped,1,3,2005,Ships,66,S700_1138,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10414,37,71.34,6,2639.58,5/6/2005 0:00,On Hold,2,5,2005,Ships,66,S700_1138,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10106,31,100,7,3312.97,2/17/2003 0:00,Shipped,1,2,2003,Planes,91,S700_1691,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10120,47,82.21,13,3863.87,4/29/2003 0:00,Shipped,2,4,2003,Planes,91,S700_1691,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10133,24,77.64,8,1863.36,6/27/2003 0:00,Shipped,2,6,2003,Planes,91,S700_1691,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10143,36,100,2,3945.96,8/10/2003 0:00,Shipped,3,8,2003,Planes,91,S700_1691,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10156,48,100,2,4954.08,10/8/2003 0:00,Shipped,4,10,2003,Planes,91,S700_1691,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10168,28,98.65,14,2762.2,10/28/2003 0:00,Shipped,4,10,2003,Planes,91,S700_1691,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Small
10199,48,83.12,2,3989.76,12/1/2003 0:00,Shipped,4,12,2003,Planes,91,S700_1691,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Medium
10210,21,78.55,12,1649.55,1/12/2004 0:00,Shipped,1,1,2004,Planes,91,S700_1691,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10223,25,100,14,2534.75,2/20/2004 0:00,Shipped,1,2,2004,Planes,91,S700_1691,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10235,25,100,8,2580.25,4/2/2004 0:00,Shipped,2,4,2004,Planes,91,S700_1691,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10250,31,91.34,9,2831.54,5/11/2004 0:00,Shipped,2,5,2004,Planes,91,S700_1691,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10262,40,84.03,4,3361.2,6/24/2004 0:00,Cancelled,2,6,2004,Planes,91,S700_1691,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10275,32,89.51,14,2864.32,7/23/2004 0:00,Shipped,3,7,2004,Planes,91,S700_1691,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10284,24,83.12,6,1994.88,8/21/2004 0:00,Shipped,3,8,2004,Planes,91,S700_1691,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10296,42,100,2,4296.6,9/15/2004 0:00,Shipped,3,9,2004,Planes,91,S700_1691,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Medium
10308,21,100,12,2224.95,10/15/2004 0:00,Shipped,4,10,2004,Planes,91,S700_1691,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10316,34,82.21,4,2795.14,11/1/2004 0:00,Shipped,4,11,2004,Planes,91,S700_1691,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10328,27,100,8,2762.1,11/12/2004 0:00,Shipped,4,11,2004,Planes,91,S700_1691,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10340,30,88.6,5,2658,11/24/2004 0:00,Shipped,4,11,2004,Planes,91,S700_1691,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10353,39,100,9,5043.87,12/4/2004 0:00,Shipped,4,12,2004,Planes,91,S700_1691,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10361,20,60.54,4,1210.8,12/17/2004 0:00,Shipped,4,12,2004,Planes,91,S700_1691,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10375,37,81.87,6,3029.19,2/3/2005 0:00,Shipped,1,2,2005,Planes,91,S700_1691,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10388,46,100,2,10066.6,3/3/2005 0:00,Shipped,1,3,2005,Planes,91,S700_1691,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Large
10398,47,87.69,6,4121.43,3/30/2005 0:00,Shipped,1,3,2005,Planes,91,S700_1691,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10401,11,100,8,1135.31,4/3/2005 0:00,On Hold,2,4,2005,Planes,91,S700_1691,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Small
10416,23,91.34,9,2100.82,5/10/2005 0:00,Shipped,2,5,2005,Planes,91,S700_1691,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10105,29,70.15,12,2034.35,2/11/2003 0:00,Shipped,1,2,2003,Ships,86,S700_1938,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10117,38,79.68,6,3027.84,4/16/2003 0:00,Shipped,2,4,2003,Ships,86,S700_1938,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10128,32,97,3,3104,6/6/2003 0:00,Shipped,2,6,2003,Ships,86,S700_1938,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10142,43,84.01,9,3612.43,8/8/2003 0:00,Shipped,3,8,2003,Ships,86,S700_1938,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10153,31,87.48,8,2711.88,9/28/2003 0:00,Shipped,3,9,2003,Ships,86,S700_1938,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10166,29,100,3,3013.97,10/21/2003 0:00,Shipped,4,10,2003,Ships,86,S700_1938,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Medium
10177,31,88.34,10,2738.54,11/7/2003 0:00,Shipped,4,11,2003,Ships,86,S700_1938,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Small
10185,30,94.4,10,2832,11/14/2003 0:00,Shipped,4,11,2003,Ships,86,S700_1938,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10196,50,94.4,2,4720,11/26/2003 0:00,Shipped,4,11,2003,Ships,86,S700_1938,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10208,40,80.55,10,3222,1/2/2004 0:00,Shipped,1,1,2004,Ships,86,S700_1938,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10221,23,97,4,2231,2/18/2004 0:00,Shipped,1,2,2004,Ships,86,S700_1938,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10232,26,88.34,7,2296.84,3/20/2004 0:00,Shipped,1,3,2004,Ships,86,S700_1938,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10248,40,100,13,4157.2,5/7/2004 0:00,Cancelled,2,5,2004,Ships,86,S700_1938,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10273,21,100,14,2146.2,7/21/2004 0:00,Shipped,3,7,2004,Ships,86,S700_1938,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10282,43,86.61,2,3724.23,8/20/2004 0:00,Shipped,3,8,2004,Ships,86,S700_1938,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10293,29,71.89,5,2084.81,9/9/2004 0:00,Shipped,3,9,2004,Ships,86,S700_1938,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10306,38,91.81,10,3488.78,10/14/2004 0:00,Shipped,4,10,2004,Ships,86,S700_1938,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10314,23,76.22,2,1753.06,10/22/2004 0:00,Shipped,4,10,2004,Ships,86,S700_1938,Heintze Collectables,86 21 3555,Smagsloget 45,,Aaarhus,,8200,Denmark,EMEA,Ibsen,Palle,Small
10327,20,100,7,3469.2,11/10/2004 0:00,Resolved,4,11,2004,Ships,86,S700_1938,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10337,36,70.3,9,2530.8,11/21/2004 0:00,Shipped,4,11,2004,Ships,86,S700_1938,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Small
10350,28,100,4,2924.32,12/2/2004 0:00,Shipped,4,12,2004,Ships,86,S700_1938,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10372,44,100,2,4496.8,1/26/2005 0:00,Shipped,1,1,2005,Ships,86,S700_1938,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10384,49,100,1,6397.44,2/23/2005 0:00,Shipped,1,2,2005,Ships,86,S700_1938,Corporate Gift Ideas Co.,6505551386,7734 Strong St.,,San Francisco,CA,,USA,NA,Brown,Julie,Medium
10397,32,80.55,5,2577.6,3/28/2005 0:00,Shipped,1,3,2005,Ships,86,S700_1938,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Small
10414,34,100,13,3533.62,5/6/2005 0:00,On Hold,2,5,2005,Ships,86,S700_1938,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10106,30,100,16,3177.3,2/17/2003 0:00,Shipped,1,2,2003,Ships,90,S700_2047,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10119,29,94.14,7,2730.06,4/28/2003 0:00,Shipped,2,4,2003,Ships,90,S700_2047,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10131,22,85.99,8,1891.78,6/16/2003 0:00,Shipped,2,6,2003,Ships,90,S700_2047,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Small
10143,26,100,11,2612.48,8/10/2003 0:00,Shipped,3,8,2003,Ships,90,S700_2047,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10155,32,91.43,9,2925.76,10/6/2003 0:00,Shipped,4,10,2003,Ships,90,S700_2047,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10167,29,100,5,2940.02,10/23/2003 0:00,Cancelled,4,10,2003,Ships,90,S700_2047,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10178,34,96.86,8,3293.24,11/8/2003 0:00,Shipped,4,11,2003,Ships,90,S700_2047,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10186,24,99.57,5,2389.68,11/14/2003 0:00,Shipped,4,11,2003,Ships,90,S700_2047,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Small
10197,24,90.52,2,2172.48,11/26/2003 0:00,Shipped,4,11,2003,Ships,90,S700_2047,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10209,33,88.71,4,2927.43,1/9/2004 0:00,Shipped,1,1,2004,Ships,90,S700_2047,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Small
10222,26,100,8,2659.54,2/19/2004 0:00,Shipped,1,2,2004,Ships,90,S700_2047,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10249,40,95.95,4,3838,5/8/2004 0:00,Shipped,2,5,2004,Ships,90,S700_2047,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Medium
10262,44,94.14,13,4142.16,6/24/2004 0:00,Cancelled,2,6,2004,Ships,90,S700_2047,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10274,24,90.52,5,2172.48,7/21/2004 0:00,Shipped,3,7,2004,Ships,90,S700_2047,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10283,20,94.14,2,1882.8,8/20/2004 0:00,Shipped,3,8,2004,Ships,90,S700_2047,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10296,34,100,11,3477.86,9/15/2004 0:00,Shipped,3,9,2004,Ships,90,S700_2047,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Medium
10307,34,97.76,5,3323.84,10/14/2004 0:00,Shipped,4,10,2004,Ships,90,S700_2047,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Medium
10316,45,93.24,13,4195.8,11/1/2004 0:00,Shipped,4,11,2004,Ships,90,S700_2047,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10328,41,100,9,4156.58,11/12/2004 0:00,Shipped,4,11,2004,Ships,90,S700_2047,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10339,55,71.25,15,3918.75,11/23/2004 0:00,Shipped,4,11,2004,Ships,90,S700_2047,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10352,23,100,3,2352.67,12/3/2004 0:00,Shipped,4,12,2004,Ships,90,S700_2047,Auto-Moto Classics Inc.,6175558428,16780 Pompton St.,,Brickhaven,MA,58339,USA,NA,Taylor,Leslie,Small
10361,24,45.39,14,1089.36,12/17/2004 0:00,Shipped,4,12,2004,Ships,90,S700_2047,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10373,32,84.41,15,2701.12,1/31/2005 0:00,Shipped,1,1,2005,Ships,90,S700_2047,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10386,29,85.76,13,2487.04,3/1/2005 0:00,Resolved,1,3,2005,Ships,90,S700_2047,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10398,36,100,7,3910.32,3/30/2005 0:00,Shipped,1,3,2005,Ships,90,S700_2047,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10400,46,87.8,5,4038.8,4/1/2005 0:00,Shipped,2,4,2005,Ships,90,S700_2047,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10415,32,95.95,4,3070.4,5/9/2005 0:00,Disputed,2,5,2005,Ships,90,S700_2047,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Medium
10106,34,100,9,3763.46,2/17/2003 0:00,Shipped,1,2,2003,Planes,99,S700_2466,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10120,24,100,15,2584.8,4/29/2003 0:00,Shipped,2,4,2003,Planes,99,S700_2466,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10131,40,100,1,4427.6,6/16/2003 0:00,Shipped,2,6,2003,Planes,99,S700_2466,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10143,26,82.77,4,2152.02,8/10/2003 0:00,Shipped,3,8,2003,Planes,99,S700_2466,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10155,20,100,2,2353.4,10/6/2003 0:00,Shipped,4,10,2003,Planes,99,S700_2466,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10168,31,100,16,3431.39,10/28/2003 0:00,Shipped,4,10,2003,Planes,99,S700_2466,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10178,22,87.75,1,1930.5,11/8/2003 0:00,Shipped,4,11,2003,Planes,99,S700_2466,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Small
10198,42,100,1,4774.56,11/27/2003 0:00,Shipped,4,11,2003,Planes,99,S700_2466,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Medium
10210,26,99.72,14,2592.72,1/12/2004 0:00,Shipped,1,1,2004,Planes,99,S700_2466,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10222,37,87.75,1,3246.75,2/19/2004 0:00,Shipped,1,2,2004,Planes,99,S700_2466,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10235,38,88.75,10,3372.5,4/2/2004 0:00,Shipped,2,4,2004,Planes,99,S700_2466,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10250,35,100,11,3909.15,5/11/2004 0:00,Shipped,2,5,2004,Planes,99,S700_2466,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10262,33,90.75,6,2994.75,6/24/2004 0:00,Cancelled,2,6,2004,Planes,99,S700_2466,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10275,39,100,16,4472.52,7/23/2004 0:00,Shipped,3,7,2004,Planes,99,S700_2466,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10284,45,100,8,4576.95,8/21/2004 0:00,Shipped,3,8,2004,Planes,99,S700_2466,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Medium
10296,24,100,4,2441.04,9/15/2004 0:00,Shipped,3,9,2004,Planes,99,S700_2466,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10308,35,88.75,14,3106.25,10/15/2004 0:00,Shipped,4,10,2004,Planes,99,S700_2466,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10316,23,100,6,2706.41,11/1/2004 0:00,Shipped,4,11,2004,Planes,99,S700_2466,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10328,37,100,10,4021.53,11/12/2004 0:00,Shipped,4,11,2004,Planes,99,S700_2466,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10340,55,87.75,7,4826.25,11/24/2004 0:00,Shipped,4,11,2004,Planes,99,S700_2466,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10352,49,100,2,4935.28,12/3/2004 0:00,Shipped,4,12,2004,Planes,99,S700_2466,Auto-Moto Classics Inc.,6175558428,16780 Pompton St.,,Brickhaven,MA,58339,USA,NA,Taylor,Leslie,Medium
10361,26,100,9,2754.7,12/17/2004 0:00,Shipped,4,12,2004,Planes,99,S700_2466,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10375,33,100,1,3856.71,2/3/2005 0:00,Shipped,1,2,2005,Planes,99,S700_2466,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10386,37,83.84,14,3102.08,3/1/2005 0:00,Resolved,1,3,2005,Planes,99,S700_2466,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10398,22,86.76,8,1908.72,3/30/2005 0:00,Shipped,1,3,2005,Planes,99,S700_2466,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10401,85,88.75,10,7543.75,4/3/2005 0:00,On Hold,2,4,2005,Planes,99,S700_2466,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Large
10416,22,100,11,2457.18,5/10/2005 0:00,Shipped,2,5,2005,Planes,99,S700_2466,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10105,31,65.77,3,2038.87,2/11/2003 0:00,Shipped,1,2,2003,Ships,72,S700_2610,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10119,38,65.77,12,2499.26,4/28/2003 0:00,Shipped,2,4,2003,Ships,72,S700_2610,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10129,45,85.29,3,3838.05,6/12/2003 0:00,Shipped,2,6,2003,Ships,72,S700_2610,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10143,31,85.29,16,2643.99,8/10/2003 0:00,Shipped,3,8,2003,Ships,72,S700_2610,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10154,36,64.33,1,2315.88,10/2/2003 0:00,Shipped,4,10,2003,Ships,72,S700_2610,Boards & Toys Co.,3105552373,4097 Douglas Av.,,Glendale,CA,92561,USA,NA,Young,Leslie,Small
10167,46,70.11,10,3225.06,10/23/2003 0:00,Cancelled,4,10,2003,Ships,72,S700_2610,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10177,32,76.62,1,2451.84,11/7/2003 0:00,Shipped,4,11,2003,Ships,72,S700_2610,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Small
10185,39,57.82,1,2254.98,11/14/2003 0:00,Shipped,4,11,2003,Ships,72,S700_2610,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10197,50,78.79,7,3939.5,11/26/2003 0:00,Shipped,4,11,2003,Ships,72,S700_2610,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10208,46,74.45,1,3424.7,1/2/2004 0:00,Shipped,1,1,2004,Ships,72,S700_2610,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10222,36,80.95,13,2914.2,2/19/2004 0:00,Shipped,1,2,2004,Ships,72,S700_2610,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10233,29,82.4,1,2389.6,3/29/2004 0:00,Shipped,1,3,2004,Ships,72,S700_2610,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Small
10248,32,75.89,4,2428.48,5/7/2004 0:00,Cancelled,2,5,2004,Ships,72,S700_2610,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10261,44,68.67,2,3021.48,6/17/2004 0:00,Shipped,2,6,2004,Ships,72,S700_2610,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10273,42,62.16,5,2610.72,7/21/2004 0:00,Shipped,3,7,2004,Ships,72,S700_2610,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10283,47,65.77,7,3091.19,8/20/2004 0:00,Shipped,3,8,2004,Ships,72,S700_2610,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10295,44,58.55,2,2576.2,9/10/2004 0:00,Shipped,3,9,2004,Ships,72,S700_2610,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10306,43,75.17,1,3232.31,10/14/2004 0:00,Shipped,4,10,2004,Ships,72,S700_2610,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10316,48,74.45,18,3573.6,11/1/2004 0:00,Shipped,4,11,2004,Ships,72,S700_2610,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10327,21,96.31,1,2022.51,11/10/2004 0:00,Resolved,4,11,2004,Ships,72,S700_2610,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10339,50,74.35,9,3717.5,11/23/2004 0:00,Shipped,4,11,2004,Ships,72,S700_2610,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10350,29,75.35,12,2185.15,12/2/2004 0:00,Shipped,4,12,2004,Ships,72,S700_2610,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10373,41,70.33,16,2883.53,1/31/2005 0:00,Shipped,1,1,2005,Ships,72,S700_2610,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10386,37,100,10,5017.57,3/1/2005 0:00,Resolved,1,3,2005,Ships,72,S700_2610,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10397,22,66.5,4,1463,3/28/2005 0:00,Shipped,1,3,2005,Ships,72,S700_2610,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Small
10414,31,75.89,4,2352.59,5/6/2005 0:00,On Hold,2,5,2005,Ships,72,S700_2610,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10103,42,100,6,4460.82,1/29/2003 0:00,Shipped,1,1,2003,Classic Cars,101,S700_2824,Baane Mini Imports,07-98 9555,Erling Skakkes gate 78,,Stavern,,4110,Norway,EMEA,Bergulfsen,Jonas,Medium
10114,42,100,10,4758.18,4/1/2003 0:00,Shipped,2,4,2003,Classic Cars,101,S700_2824,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Medium
10126,45,100,6,4597.2,5/28/2003 0:00,Shipped,2,5,2003,Classic Cars,101,S700_2824,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Medium
10140,36,100,6,4114.8,7/24/2003 0:00,Shipped,3,7,2003,Classic Cars,101,S700_2824,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10150,20,100,3,2104,9/19/2003 0:00,Shipped,3,9,2003,Classic Cars,101,S700_2824,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10164,39,81.93,4,3195.27,10/21/2003 0:00,Resolved,4,10,2003,Classic Cars,101,S700_2824,Mini Auto Werke,7675-3555,Kirchgasse 6,,Graz,,8010,Austria,EMEA,Mendel,Roland,Medium
10175,42,85.98,11,3611.16,11/6/2003 0:00,Shipped,4,11,2003,Classic Cars,101,S700_2824,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10183,23,86.99,3,2000.77,11/13/2003 0:00,Shipped,4,11,2003,Classic Cars,101,S700_2824,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10194,26,89.01,6,2314.26,11/25/2003 0:00,Shipped,4,11,2003,Classic Cars,101,S700_2824,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10206,33,100,1,3871.89,12/5/2003 0:00,Shipped,4,12,2003,Classic Cars,101,S700_2824,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Medium
10217,31,88,6,2728,2/4/2004 0:00,Shipped,1,2,2004,Classic Cars,101,S700_2824,Handji Gifts& Co,+65 224 1555,Village Close - 106 Linden Road Sandown,2nd Floor,Singapore,,69045,Singapore,APAC,Victorino,Wendy,Small
10229,50,100,11,5614,3/11/2004 0:00,Shipped,1,3,2004,Classic Cars,101,S700_2824,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10245,44,100,4,4628.8,5/4/2004 0:00,Shipped,2,5,2004,Classic Cars,101,S700_2824,Super Scale Inc.,2035559545,567 North Pendale Street,,New Haven,CT,97823,USA,NA,Murphy,Leslie,Medium
10258,45,80.92,1,3641.4,6/15/2004 0:00,Shipped,2,6,2004,Classic Cars,101,S700_2824,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Medium
10270,46,88,4,4048,7/19/2004 0:00,Shipped,3,7,2004,Classic Cars,101,S700_2824,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10281,27,85.98,11,2321.46,8/19/2004 0:00,Shipped,3,8,2004,Classic Cars,101,S700_2824,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Small
10291,28,100,6,3256.96,9/8/2004 0:00,Shipped,3,9,2004,Classic Cars,101,S700_2824,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10304,40,100,1,4208,10/11/2004 0:00,Shipped,4,10,2004,Classic Cars,101,S700_2824,Auto Assoc. & Cie.,30.59.8555,"67, avenue de l'Europe",,Versailles,,78000,France,EMEA,Tonini,Daniel,Medium
10313,30,99.13,9,2973.9,10/22/2004 0:00,Shipped,4,10,2004,Classic Cars,101,S700_2824,Canadian Gift Exchange Network,(604) 555-3392,1900 Oak St.,,Vancouver,BC,V3F 2K1,Canada,NA,Tannamuri,Yoshi,Small
10324,34,100,5,4248.3,11/5/2004 0:00,Shipped,4,11,2004,Classic Cars,101,S700_2824,Vitachrome Inc.,2125551500,2678 Kingston Rd.,Suite 101,NYC,NY,10022,USA,NA,Frick,Michael,Medium
10336,46,100,2,9558.8,11/20/2004 0:00,Shipped,4,11,2004,Classic Cars,101,S700_2824,"La Corne D'abondance, Co.",(1) 42.34.2555,"265, boulevard Charonne",,Paris,,75012,France,EMEA,Bertrand,Marie,Large
10348,32,82.83,7,2650.56,11/1/2004 0:00,Shipped,4,11,2004,Classic Cars,101,S700_2824,"Corrida Auto Replicas, Ltd",(91) 555 22 82,"C/ Araquil, 67",,Madrid,,28023,Spain,EMEA,Sommer,Mart�n,Small
10358,27,100,3,3761.37,12/10/2004 0:00,Shipped,4,12,2004,Classic Cars,101,S700_2824,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10371,34,100,3,4301.34,1/23/2005 0:00,Shipped,1,1,2005,Classic Cars,101,S700_2824,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10382,34,54.84,9,1864.56,2/17/2005 0:00,Shipped,1,2,2005,Classic Cars,101,S700_2824,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10411,34,100,4,3576.8,5/1/2005 0:00,Shipped,2,5,2005,Classic Cars,101,S700_2824,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10424,46,80.92,1,3722.32,5/31/2005 0:00,In Process,2,5,2005,Classic Cars,101,S700_2824,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10106,32,100,1,3986.56,2/17/2003 0:00,Shipped,1,2,2003,Planes,118,S700_2834,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10120,24,100,7,3417.12,4/29/2003 0:00,Shipped,2,4,2003,Planes,118,S700_2834,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10133,27,99.67,2,2691.09,6/27/2003 0:00,Shipped,2,6,2003,Planes,118,S700_2834,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10145,20,100,13,2752.6,8/25/2003 0:00,Shipped,3,8,2003,Planes,118,S700_2834,Toys4GrownUps.com,6265557265,78934 Hillside Dr.,,Pasadena,CA,90003,USA,NA,Young,Julie,Small
10168,36,100,8,4527.72,10/28/2003 0:00,Shipped,4,10,2003,Planes,118,S700_2834,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10188,29,100,8,3957.05,11/18/2003 0:00,Shipped,4,11,2003,Planes,118,S700_2834,Herkku Gifts,+47 2267 3215,"Drammen 121, PR 744 Sentrum",,Bergen,,N 5804,Norway,EMEA,Oeztan,Veysel,Medium
10210,25,100,6,2818,1/12/2004 0:00,Shipped,1,1,2004,Planes,118,S700_2834,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10223,29,100,8,3199.86,2/20/2004 0:00,Shipped,1,2,2004,Planes,118,S700_2834,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10235,25,96.11,2,2402.75,4/2/2004 0:00,Shipped,2,4,2004,Planes,118,S700_2834,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10250,44,100,3,6055.72,5/11/2004 0:00,Shipped,2,5,2004,Planes,118,S700_2834,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Medium
10263,47,100,9,5465.16,6/28/2004 0:00,Shipped,2,6,2004,Planes,118,S700_2834,Gift Depot Inc.,2035552570,25593 South Bay Ln.,,Bridgewater,CT,97562,USA,NA,King,Julie,Medium
10275,48,100,8,6378.72,7/23/2004 0:00,Shipped,3,7,2004,Planes,118,S700_2834,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10285,45,100,13,5392.8,8/27/2004 0:00,Shipped,3,8,2004,Planes,118,S700_2834,Marta's Replicas Co.,6175558555,39323 Spinnaker Dr.,,Cambridge,MA,51247,USA,NA,Hernandez,Marta,Medium
10297,35,100,3,3986.5,9/16/2004 0:00,Shipped,3,9,2004,Planes,118,S700_2834,"Clover Collections, Co.",+353 1862 1555,25 Maiden Lane,Floor No. 4,Dublin,,2,Ireland,EMEA,Cassidy,Dean,Medium
10308,31,100,6,4009.23,10/15/2004 0:00,Shipped,4,10,2004,Planes,118,S700_2834,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Medium
10318,50,100,8,7119,11/2/2004 0:00,Shipped,4,11,2004,Planes,118,S700_2834,Diecast Classics Inc.,2155551555,7586 Pompton St.,,Allentown,PA,70267,USA,NA,Yu,Kyung,Large
10328,33,100,11,4072.2,11/12/2004 0:00,Shipped,4,11,2004,Planes,118,S700_2834,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10340,29,100,6,4094.51,11/24/2004 0:00,Shipped,4,11,2004,Planes,118,S700_2834,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10353,48,68.8,4,3302.4,12/4/2004 0:00,Shipped,4,12,2004,Planes,118,S700_2834,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10361,44,72.42,5,3186.48,12/17/2004 0:00,Shipped,4,12,2004,Planes,118,S700_2834,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10375,25,66.73,10,1668.25,2/3/2005 0:00,Shipped,1,2,2005,Planes,118,S700_2834,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10388,50,100,3,7154.5,3/3/2005 0:00,Shipped,1,3,2005,Planes,118,S700_2834,FunGiftIdeas.com,5085552555,1785 First Street,,New Bedford,MA,50553,USA,NA,Benitez,Violeta,Large
10398,23,100,9,2810.83,3/30/2005 0:00,Shipped,1,3,2005,Planes,118,S700_2834,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10401,21,96.11,2,2018.31,4/3/2005 0:00,On Hold,2,4,2005,Planes,118,S700_2834,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Small
10416,41,100,3,5642.83,5/10/2005 0:00,Shipped,2,5,2005,Planes,118,S700_2834,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Medium
10106,44,74.4,8,3273.6,2/17/2003 0:00,Shipped,1,2,2003,Planes,80,S700_3167,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10120,43,76,14,3268,4/29/2003 0:00,Shipped,2,4,2003,Planes,80,S700_3167,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Medium
10143,28,96,3,2688,8/10/2003 0:00,Shipped,3,8,2003,Planes,80,S700_3167,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10155,43,86.4,1,3715.2,10/6/2003 0:00,Shipped,4,10,2003,Planes,80,S700_3167,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10168,48,96,15,4608,10/28/2003 0:00,Shipped,4,10,2003,Planes,80,S700_3167,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10199,38,82.4,3,3131.2,12/1/2003 0:00,Shipped,4,12,2003,Planes,80,S700_3167,West Coast Collectables Co.,3105553722,3675 Furth Circle,,Burbank,CA,94019,USA,NA,Thompson,Steve,Medium
10210,31,86.4,13,2678.4,1/12/2004 0:00,Shipped,1,1,2004,Planes,80,S700_3167,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10223,26,67.2,15,1747.2,2/20/2004 0:00,Shipped,1,2,2004,Planes,80,S700_3167,"Australian Collectors, Co.",03 9520 4555,636 St Kilda Road,Level 3,Melbourne,Victoria,3004,Australia,APAC,Ferguson,Peter,Small
10235,32,92,9,2944,4/2/2004 0:00,Shipped,2,4,2004,Planes,80,S700_3167,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10250,44,67.2,10,2956.8,5/11/2004 0:00,Shipped,2,5,2004,Planes,80,S700_3167,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10262,27,76,5,2052,6/24/2004 0:00,Cancelled,2,6,2004,Planes,80,S700_3167,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10275,43,73.6,15,3164.8,7/23/2004 0:00,Shipped,3,7,2004,Planes,80,S700_3167,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10284,25,69.6,7,1740,8/21/2004 0:00,Shipped,3,8,2004,Planes,80,S700_3167,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10296,22,80.8,3,1777.6,9/15/2004 0:00,Shipped,3,9,2004,Planes,80,S700_3167,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10308,21,87.2,13,1831.2,10/15/2004 0:00,Shipped,4,10,2004,Planes,80,S700_3167,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10316,48,75.2,5,3609.6,11/1/2004 0:00,Shipped,4,11,2004,Planes,80,S700_3167,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10328,33,64,13,2112,11/12/2004 0:00,Shipped,4,11,2004,Planes,80,S700_3167,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10341,34,100,5,3644.12,11/24/2004 0:00,Shipped,4,11,2004,Planes,80,S700_3167,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Medium
10353,43,81.95,6,3523.85,12/4/2004 0:00,Shipped,4,12,2004,Planes,80,S700_3167,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Medium
10361,44,100,10,5001.92,12/17/2004 0:00,Shipped,4,12,2004,Planes,80,S700_3167,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10375,44,100,11,5208.72,2/3/2005 0:00,Shipped,1,2,2005,Planes,80,S700_3167,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10386,32,94.34,17,3018.88,3/1/2005 0:00,Resolved,1,3,2005,Planes,80,S700_3167,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10398,29,65.6,10,1902.4,3/30/2005 0:00,Shipped,1,3,2005,Planes,80,S700_3167,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10401,77,92,9,7084,4/3/2005 0:00,On Hold,2,4,2005,Planes,80,S700_3167,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Large
10416,39,67.2,10,2620.8,5/10/2005 0:00,Shipped,2,5,2005,Planes,80,S700_3167,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10105,39,81.14,6,3164.46,2/11/2003 0:00,Shipped,1,2,2003,Ships,100,S700_3505,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10118,36,100,1,4219.2,4/21/2003 0:00,Shipped,2,4,2003,Ships,100,S700_3505,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10129,42,91.15,6,3828.3,6/12/2003 0:00,Shipped,2,6,2003,Ships,100,S700_3505,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Medium
10142,21,100,3,2334.99,8/8/2003 0:00,Shipped,3,8,2003,Ships,100,S700_3505,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10153,50,88.15,2,4407.5,9/28/2003 0:00,Shipped,3,9,2003,Ships,100,S700_3505,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10167,24,100,13,2812.8,10/23/2003 0:00,Cancelled,4,10,2003,Ships,100,S700_3505,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10177,44,92.16,4,4055.04,11/7/2003 0:00,Shipped,4,11,2003,Ships,100,S700_3505,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Medium
10185,37,100,4,3891.66,11/14/2003 0:00,Shipped,4,11,2003,Ships,100,S700_3505,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Medium
10197,27,92.16,10,2488.32,11/26/2003 0:00,Shipped,4,11,2003,Ships,100,S700_3505,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10208,37,100,4,4447.4,1/2/2004 0:00,Shipped,1,1,2004,Ships,100,S700_3505,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Medium
10222,38,100,16,4187.22,2/19/2004 0:00,Shipped,1,2,2004,Ships,100,S700_3505,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10232,48,96.16,1,4615.68,3/20/2004 0:00,Shipped,1,3,2004,Ships,100,S700_3505,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Medium
10248,30,100,7,3245.4,5/7/2004 0:00,Cancelled,2,5,2004,Ships,100,S700_3505,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10261,25,88.15,5,2203.75,6/17/2004 0:00,Shipped,2,6,2004,Ships,100,S700_3505,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Small
10273,40,86.15,8,3446,7/21/2004 0:00,Shipped,3,7,2004,Ships,100,S700_3505,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Medium
10283,22,88.15,10,1939.3,8/20/2004 0:00,Shipped,3,8,2004,Ships,100,S700_3505,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10295,34,100,5,3473.78,9/10/2004 0:00,Shipped,3,9,2004,Ships,100,S700_3505,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10306,32,90.15,4,2884.8,10/14/2004 0:00,Shipped,4,10,2004,Ships,100,S700_3505,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10315,31,86.15,3,2670.65,10/29/2004 0:00,Shipped,4,10,2004,Ships,100,S700_3505,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10327,43,80,2,3440,11/10/2004 0:00,Resolved,4,11,2004,Ships,100,S700_3505,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10337,31,89.38,1,2770.78,11/21/2004 0:00,Shipped,4,11,2004,Ships,100,S700_3505,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Small
10350,31,77.34,13,2397.54,12/2/2004 0:00,Shipped,4,12,2004,Ships,100,S700_3505,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10373,34,96.34,2,3275.56,1/31/2005 0:00,Shipped,1,1,2005,Ships,100,S700_3505,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10386,45,92.08,2,4143.6,3/1/2005 0:00,Resolved,1,3,2005,Ships,100,S700_3505,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10397,48,100,3,5192.64,3/28/2005 0:00,Shipped,1,3,2005,Ships,100,S700_3505,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10414,28,100,7,3029.04,5/6/2005 0:00,On Hold,2,5,2005,Ships,100,S700_3505,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium
10105,22,100,7,2556.18,2/11/2003 0:00,Shipped,1,2,2003,Ships,99,S700_3962,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10117,45,83.42,1,3753.9,4/16/2003 0:00,Shipped,2,4,2003,Ships,99,S700_3962,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Medium
10129,30,85.41,7,2562.3,6/12/2003 0:00,Shipped,2,6,2003,Ships,99,S700_3962,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10142,38,85.41,4,3245.58,8/8/2003 0:00,Shipped,3,8,2003,Ships,99,S700_3962,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Medium
10153,20,100,3,2204.6,9/28/2003 0:00,Shipped,3,9,2003,Ships,99,S700_3962,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10167,28,100,14,3003,10/23/2003 0:00,Cancelled,4,10,2003,Ships,99,S700_3962,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Medium
10177,24,100,5,2526.48,11/7/2003 0:00,Shipped,4,11,2003,Ships,99,S700_3962,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Small
10185,22,79.45,5,1747.9,11/14/2003 0:00,Shipped,4,11,2003,Ships,99,S700_3962,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10197,35,93.35,11,3267.25,11/26/2003 0:00,Shipped,4,11,2003,Ships,99,S700_3962,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Medium
10208,33,85.41,5,2818.53,1/2/2004 0:00,Shipped,1,1,2004,Ships,99,S700_3962,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10222,31,95.34,17,2955.54,2/19/2004 0:00,Shipped,1,2,2004,Ships,99,S700_3962,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10232,35,82.43,2,2885.05,3/20/2004 0:00,Shipped,1,3,2004,Ships,99,S700_3962,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10248,35,90.37,8,3162.95,5/7/2004 0:00,Cancelled,2,5,2004,Ships,99,S700_3962,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10261,50,81.43,6,4071.5,6/17/2004 0:00,Shipped,2,6,2004,Ships,99,S700_3962,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Medium
10273,26,100,9,2969.46,7/21/2004 0:00,Shipped,3,7,2004,Ships,99,S700_3962,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10283,38,89.38,11,3396.44,8/20/2004 0:00,Shipped,3,8,2004,Ships,99,S700_3962,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Medium
10294,45,100,1,4692.6,9/10/2004 0:00,Shipped,3,9,2004,Ships,99,S700_3962,Online Mini Collectables,6175557555,7635 Spinnaker Dr.,,Brickhaven,MA,58339,USA,NA,Barajas,Miguel,Medium
10306,30,100,5,3515.7,10/14/2004 0:00,Shipped,4,10,2004,Ships,99,S700_3962,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Medium
10315,37,91.37,4,3380.69,10/29/2004 0:00,Shipped,4,10,2004,Ships,99,S700_3962,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Medium
10327,37,86.61,3,3204.57,11/10/2004 0:00,Resolved,4,11,2004,Ships,99,S700_3962,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10337,36,71.89,7,2588.04,11/21/2004 0:00,Shipped,4,11,2004,Ships,99,S700_3962,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Small
10350,25,100,16,2854.75,12/2/2004 0:00,Shipped,4,12,2004,Ships,99,S700_3962,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10373,37,100,8,4025.6,1/31/2005 0:00,Shipped,1,1,2005,Ships,99,S700_3962,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10386,30,95.48,3,2864.4,3/1/2005 0:00,Resolved,1,3,2005,Ships,99,S700_3962,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10397,36,100,2,3789.72,3/28/2005 0:00,Shipped,1,3,2005,Ships,99,S700_3962,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10414,27,90.37,8,2439.99,5/6/2005 0:00,On Hold,2,5,2005,Ships,99,S700_3962,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Small
10106,48,61.44,10,2949.12,2/17/2003 0:00,Shipped,1,2,2003,Planes,74,S700_4002,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10119,26,59.22,1,1539.72,4/28/2003 0:00,Shipped,2,4,2003,Planes,74,S700_4002,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10131,26,85.13,2,2213.38,6/16/2003 0:00,Shipped,2,6,2003,Planes,74,S700_4002,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Small
10143,34,85.87,5,2919.58,8/10/2003 0:00,Shipped,3,8,2003,Planes,74,S700_4002,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10155,44,85.87,3,3778.28,10/6/2003 0:00,Shipped,4,10,2003,Planes,74,S700_4002,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Medium
10168,39,82.91,17,3233.49,10/28/2003 0:00,Shipped,4,10,2003,Planes,74,S700_4002,Technics Stores Inc.,6505556809,9408 Furth Circle,,Burlingame,CA,94217,USA,NA,Hirano,Juri,Medium
10178,45,76.25,2,3431.25,11/8/2003 0:00,Shipped,4,11,2003,Planes,74,S700_4002,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Medium
10198,40,63.67,2,2546.8,11/27/2003 0:00,Shipped,4,11,2003,Planes,74,S700_4002,Cruz & Sons Co.,+63 2 555 3587,15 McCallum Street - NatWest Center #13-03,,Makati City,,1227 MM,Philippines,Japan,Cruz,Arnold,Small
10210,42,70.33,15,2953.86,1/12/2004 0:00,Shipped,1,1,2004,Planes,74,S700_4002,Osaka Souveniers Co.,+81 06 6342 5555,"Dojima Avanza 4F, 1-6-20 Dojima, Kita-ku",,Osaka,Osaka,530-0003,Japan,Japan,Kentary,Mory,Small
10222,43,74.03,2,3183.29,2/19/2004 0:00,Shipped,1,2,2004,Planes,74,S700_4002,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Medium
10235,34,72.55,11,2466.7,4/2/2004 0:00,Shipped,2,4,2004,Planes,74,S700_4002,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10250,38,62.19,12,2363.22,5/11/2004 0:00,Shipped,2,5,2004,Planes,74,S700_4002,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10262,35,71.07,7,2487.45,6/24/2004 0:00,Cancelled,2,6,2004,Planes,74,S700_4002,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10275,31,72.55,17,2249.05,7/23/2004 0:00,Shipped,3,7,2004,Planes,74,S700_4002,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10284,32,64.41,9,2061.12,8/21/2004 0:00,Shipped,3,8,2004,Planes,74,S700_4002,"Norway Gifts By Mail, Co.",+47 2212 1555,"Drammensveien 126 A, PB 744 Sentrum",,Oslo,,N 0106,Norway,EMEA,Klaeboe,Jan,Small
10296,47,86.62,5,4071.14,9/15/2004 0:00,Shipped,3,9,2004,Planes,74,S700_4002,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Medium
10308,39,68.11,15,2656.29,10/15/2004 0:00,Shipped,4,10,2004,Planes,74,S700_4002,Mini Classics,9145554562,3758 North Pendale Street,,White Plains,NY,24067,USA,NA,Frick,Steve,Small
10316,44,62.19,7,2736.36,11/1/2004 0:00,Shipped,4,11,2004,Planes,74,S700_4002,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10328,39,85.87,12,3348.93,11/12/2004 0:00,Shipped,4,11,2004,Planes,74,S700_4002,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Medium
10339,50,57.86,8,2893,11/23/2004 0:00,Shipped,4,11,2004,Planes,74,S700_4002,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10352,22,75.51,1,1661.22,12/3/2004 0:00,Shipped,4,12,2004,Planes,74,S700_4002,Auto-Moto Classics Inc.,6175558428,16780 Pompton St.,,Brickhaven,MA,58339,USA,NA,Taylor,Leslie,Small
10361,35,100,11,4277.35,12/17/2004 0:00,Shipped,4,12,2004,Planes,74,S700_4002,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Medium
10373,45,55.62,17,2502.9,1/31/2005 0:00,Shipped,1,1,2005,Planes,74,S700_4002,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10386,44,86.4,15,3801.6,3/1/2005 0:00,Resolved,1,3,2005,Planes,74,S700_4002,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10398,36,87.36,12,3144.96,3/30/2005 0:00,Shipped,1,3,2005,Planes,74,S700_4002,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Medium
10401,28,72.55,11,2031.4,4/3/2005 0:00,On Hold,2,4,2005,Planes,74,S700_4002,Tekni Collectables Inc.,2015559350,7476 Moss Rd.,,Newark,NJ,94019,USA,NA,Brown,William,Small
10416,43,62.19,12,2674.17,5/10/2005 0:00,Shipped,2,5,2005,Planes,74,S700_4002,L'ordine Souveniers,0522-556555,Strada Provinciale 124,,Reggio Emilia,,42100,Italy,EMEA,Moroni,Maurizio,Small
10106,48,52.64,15,2526.72,2/17/2003 0:00,Shipped,1,2,2003,Planes,49,S72_1253,Rovelli Gifts,035-640555,Via Ludovico il Moro 22,,Bergamo,,24100,Italy,EMEA,Rovelli,Giovanni,Small
10119,28,48.17,6,1348.76,4/28/2003 0:00,Shipped,2,4,2003,Planes,49,S72_1253,Salzburg Collectables,6562-9555,Geislweg 14,,Salzburg,,5020,Austria,EMEA,Pipps,Georg,Small
10131,21,41.71,7,875.91,6/16/2003 0:00,Shipped,2,6,2003,Planes,49,S72_1253,Gift Ideas Corp.,2035554407,2440 Pompton St.,,Glendale,CT,97561,USA,NA,Lewis,Dan,Small
10143,37,50.65,10,1874.05,8/10/2003 0:00,Shipped,3,8,2003,Planes,49,S72_1253,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10155,34,49.16,8,1671.44,10/6/2003 0:00,Shipped,4,10,2003,Planes,49,S72_1253,"Toys of Finland, Co.",90-224 8555,Keskuskatu 45,,Helsinki,,21240,Finland,EMEA,Karttunen,Matti,Small
10167,40,41.71,4,1668.4,10/23/2003 0:00,Cancelled,4,10,2003,Planes,49,S72_1253,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10178,45,51.15,7,2301.75,11/8/2003 0:00,Shipped,4,11,2003,Planes,49,S72_1253,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Small
10186,28,52.14,4,1459.92,11/14/2003 0:00,Shipped,4,11,2003,Planes,49,S72_1253,"Double Decker Gift Stores, Ltd",(171) 555-7555,120 Hanover Sq.,,London,,WA1 1DP,UK,EMEA,Hardy,Thomas,Small
10197,29,41.71,1,1209.59,11/26/2003 0:00,Shipped,4,11,2003,Planes,49,S72_1253,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10209,48,44.69,3,2145.12,1/9/2004 0:00,Shipped,1,1,2004,Planes,49,S72_1253,"Men 'R' US Retailers, Ltd.",2155554369,6047 Douglas Av.,,Los Angeles,CA,,USA,NA,Chandler,Michael,Small
10222,31,45.69,7,1416.39,2/19/2004 0:00,Shipped,1,2,2004,Planes,49,S72_1253,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10249,32,57.61,3,1843.52,5/8/2004 0:00,Shipped,2,5,2004,Planes,49,S72_1253,Cambridge Collectables Co.,6175555555,4658 Baden Av.,,Cambridge,MA,51247,USA,NA,Tseng,Kyung,Small
10262,21,57.11,12,1199.31,6/24/2004 0:00,Cancelled,2,6,2004,Planes,49,S72_1253,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10274,32,58.6,4,1875.2,7/21/2004 0:00,Shipped,3,7,2004,Planes,49,S72_1253,Collectables For Less Inc.,6175558555,7825 Douglas Av.,,Brickhaven,MA,58339,USA,NA,Nelson,Allen,Small
10283,43,57.61,1,2477.23,8/20/2004 0:00,Shipped,3,8,2004,Planes,49,S72_1253,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10296,21,45.19,10,948.99,9/15/2004 0:00,Shipped,3,9,2004,Planes,49,S72_1253,"Bavarian Collectables Imports, Co.",+49 89 61 08 9555,Hansastr. 15,,Munich,,80686,Germany,EMEA,Donnermeyer,Michael,Small
10307,34,53.63,4,1823.42,10/14/2004 0:00,Shipped,4,10,2004,Planes,49,S72_1253,"Classic Gift Ideas, Inc",2155554695,782 First Street,,Philadelphia,PA,71270,USA,NA,Cervantes,Francisca,Small
10316,34,43.7,12,1485.8,11/1/2004 0:00,Shipped,4,11,2004,Planes,49,S72_1253,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10329,44,86.13,8,3789.72,11/15/2004 0:00,Shipped,4,11,2004,Planes,49,S72_1253,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Medium
10339,27,76.31,6,2060.37,11/23/2004 0:00,Shipped,4,11,2004,Planes,49,S72_1253,"Tokyo Collectables, Ltd",+81 3 3584 0555,2-2-8 Roppongi,,Minato-ku,Tokyo,106-0032,Japan,Japan,Shimamura,Akiko,Small
10352,49,52.64,4,2579.36,12/3/2004 0:00,Shipped,4,12,2004,Planes,49,S72_1253,Auto-Moto Classics Inc.,6175558428,16780 Pompton St.,,Brickhaven,MA,58339,USA,NA,Taylor,Leslie,Small
10361,23,95.2,12,2189.6,12/17/2004 0:00,Shipped,4,12,2004,Planes,49,S72_1253,Souveniers And Things Co.,+61 2 9495 8555,"Monitor Money Building, 815 Pacific Hwy",Level 6,Chatswood,NSW,2067,Australia,APAC,Huxley,Adrian,Small
10373,25,64.97,9,1624.25,1/31/2005 0:00,Shipped,1,1,2005,Planes,49,S72_1253,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Small
10386,50,87.15,16,4357.5,3/1/2005 0:00,Resolved,1,3,2005,Planes,49,S72_1253,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10398,34,40.22,1,1367.48,3/30/2005 0:00,Shipped,1,3,2005,Planes,49,S72_1253,Reims Collectables,26.47.1555,59 rue de l'Abbaye,,Reims,,51100,France,EMEA,Henriot,Paul,Small
10400,20,56.12,4,1122.4,4/1/2005 0:00,Shipped,2,4,2005,Planes,49,S72_1253,The Sharp Gifts Warehouse,4085553659,3086 Ingle Ln.,,San Jose,CA,94217,USA,NA,Frick,Sue,Small
10415,42,57.61,3,2419.62,5/9/2005 0:00,Disputed,2,5,2005,Planes,49,S72_1253,"Australian Collectables, Ltd",61-9-3844-6555,7 Allen Street,,Glen Waverly,Victoria,3150,Australia,APAC,Connery,Sean,Small
10105,25,56.78,8,1419.5,2/11/2003 0:00,Shipped,1,2,2003,Ships,54,S72_3212,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Small
10117,50,43.68,2,2184,4/16/2003 0:00,Shipped,2,4,2003,Ships,54,S72_3212,"Dragon Souveniers, Ltd.",+65 221 7555,"Bronz Sok., Bronz Apt. 3/6 Tesvikiye",,Singapore,,79903,Singapore,Japan,Natividad,Eric,Small
10129,32,64.97,8,2079.04,6/12/2003 0:00,Shipped,2,6,2003,Ships,54,S72_3212,"Stylish Desk Decors, Co.",(171) 555-0297,35 King George,,London,,WX3 6FW,UK,EMEA,Brown,Ann,Small
10142,39,44.23,5,1724.97,8/8/2003 0:00,Shipped,3,8,2003,Ships,54,S72_3212,Mini Gifts Distributors Ltd.,4155551450,5677 Strong St.,,San Rafael,CA,97562,USA,NA,Nelson,Valarie,Small
10153,50,60.06,4,3003,9/28/2003 0:00,Shipped,3,9,2003,Ships,54,S72_3212,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10167,38,48.59,15,1846.42,10/23/2003 0:00,Cancelled,4,10,2003,Ships,54,S72_3212,Scandinavian Gift Ideas,0695-34 6555,?kergatan 24,,Boras,,S-844 67,Sweden,EMEA,Larsson,Maria,Small
10177,40,50.23,6,2009.2,11/7/2003 0:00,Shipped,4,11,2003,Ships,54,S72_3212,CAF Imports,+34 913 728 555,"Merchants House, 27-30 Merchant's Quay",,Madrid,,28023,Spain,EMEA,Fernandez,Jesus,Small
10185,28,64.43,6,1804.04,11/14/2003 0:00,Shipped,4,11,2003,Ships,54,S72_3212,Mini Creations Ltd.,5085559555,4575 Hillside Dr.,,New Bedford,MA,50553,USA,NA,Tam,Wing C,Small
10197,42,50.23,12,2109.66,11/26/2003 0:00,Shipped,4,11,2003,Ships,54,S72_3212,Enaco Distributors,(93) 203 4555,"Rambla de Catalu�a, 23",,Barcelona,,8022,Spain,EMEA,Saavedra,Eduardo,Small
10208,42,63.88,6,2682.96,1/2/2004 0:00,Shipped,1,1,2004,Ships,54,S72_3212,"Saveley & Henriot, Co.",78.32.5555,"2, rue du Commerce",,Lyon,,69004,France,EMEA,Saveley,Mary,Small
10222,36,63.34,18,2280.24,2/19/2004 0:00,Shipped,1,2,2004,Ships,54,S72_3212,Collectable Mini Designs Co.,7605558146,361 Furth Circle,,San Diego,CA,91217,USA,NA,Thompson,Valarie,Small
10232,24,49.69,3,1192.56,3/20/2004 0:00,Shipped,1,3,2004,Ships,54,S72_3212,giftsbymail.co.uk,(198) 555-8888,Garden House Crowther Way,,Cowes,Isle of Wight,PO31 7PJ,UK,EMEA,Bennett,Helen,Small
10248,23,65.52,9,1506.96,5/7/2004 0:00,Cancelled,2,5,2004,Ships,54,S72_3212,Land of Toys Inc.,2125557818,897 Long Airport Avenue,,NYC,NY,10022,USA,NA,Yu,Kwai,Small
10261,29,50.78,7,1472.62,6/17/2004 0:00,Shipped,2,6,2004,Ships,54,S72_3212,Quebec Home Shopping Network,(514) 555-8054,43 rue St. Laurent,,Montreal,Quebec,H1J 1C3,Canada,NA,Fresnisre,Jean,Small
10273,37,45.86,10,1696.82,7/21/2004 0:00,Shipped,3,7,2004,Ships,54,S72_3212,Petit Auto,(02) 5554 67,Rue Joseph-Bens 532,,Bruxelles,,B-1180,Belgium,EMEA,Dewey,Catherine,Small
10283,33,51.32,12,1693.56,8/20/2004 0:00,Shipped,3,8,2004,Ships,54,S72_3212,"Royal Canadian Collectables, Ltd.",(604) 555-4555,23 Tsawassen Blvd.,,Tsawassen,BC,T2F 8M4,Canada,NA,Lincoln,Elizabeth,Small
10293,32,60.06,1,1921.92,9/9/2004 0:00,Shipped,3,9,2004,Ships,54,S72_3212,Amica Models & Co.,011-4988555,Via Monte Bianco 34,,Torino,,10100,Italy,EMEA,Accorti,Paolo,Small
10306,35,59.51,6,2082.85,10/14/2004 0:00,Shipped,4,10,2004,Ships,54,S72_3212,"AV Stores, Co.",(171) 555-1555,Fauntleroy Circus,,Manchester,,EC2 5NT,UK,EMEA,Ashworth,Victoria,Small
10315,40,55.69,5,2227.6,10/29/2004 0:00,Shipped,4,10,2004,Ships,54,S72_3212,La Rochelle Gifts,40.67.8555,"67, rue des Cinquante Otages",,Nantes,,44000,France,EMEA,Labrune,Janine,Small
10327,37,86.74,4,3209.38,11/10/2004 0:00,Resolved,4,11,2004,Ships,54,S72_3212,Danish Wholesale Imports,31 12 3555,Vinb'ltet 34,,Kobenhavn,,1734,Denmark,EMEA,Petersen,Jytte,Medium
10337,42,97.16,5,4080.72,11/21/2004 0:00,Shipped,4,11,2004,Ships,54,S72_3212,Classic Legends Inc.,2125558493,5905 Pompton St.,Suite 750,NYC,NY,10022,USA,NA,Hernandez,Maria,Medium
10350,20,100,15,2244.4,12/2/2004 0:00,Shipped,4,12,2004,Ships,54,S72_3212,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Small
10373,29,100,1,3978.51,1/31/2005 0:00,Shipped,1,1,2005,Ships,54,S72_3212,"Oulu Toy Supplies, Inc.",981-443655,Torikatu 38,,Oulu,,90110,Finland,EMEA,Koskitalo,Pirkko,Medium
10386,43,100,4,5417.57,3/1/2005 0:00,Resolved,1,3,2005,Ships,54,S72_3212,Euro Shopping Channel,(91) 555 94 44,"C/ Moralzarzal, 86",,Madrid,,28034,Spain,EMEA,Freyre,Diego,Medium
10397,34,62.24,1,2116.16,3/28/2005 0:00,Shipped,1,3,2005,Ships,54,S72_3212,Alpha Cognac,61.77.6555,1 rue Alsace-Lorraine,,Toulouse,,31000,France,EMEA,Roulet,Annette,Small
10414,47,65.52,9,3079.44,5/6/2005 0:00,On Hold,2,5,2005,Ships,54,S72_3212,Gifts4AllAges.com,6175559555,8616 Spinnaker Dr.,,Boston,MA,51003,USA,NA,Yoshido,Juri,Medium

"""
df = pd.read_csv(StringIO(data))
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
df['YEAR'] = df['ORDERDATE'].dt.year
df['MONTH'] = df['ORDERDATE'].dt.month
sales_trend = df.groupby(['YEAR', 'MONTH'])['SALES'].sum().reset_index()

# Define plotting functions
def plot_sales_trend():
        
    plt.figure(figsize=(14, 7))
    plt.plot(pd.to_datetime(sales_trend[['YEAR', 'MONTH']].assign(DAY=1)), sales_trend['SALES'], marker='o')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.tight_layout()

    plt.show()
    pass

def plot_quantity_vs_price():        
    plt.figure(figsize=(10, 6))
    plt.scatter(df['QUANTITYORDERED'], df['PRICEEACH'], alpha=0.5)
    plt.title('Relationship between Quantity Ordered and Price Each')
    plt.xlabel('Quantity Ordered')
    plt.ylabel('Price Each')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    pass

def plot_total_sales_by_country():
        
    country_sales = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    country_sales.plot(kind='bar')
    plt.title('Total Sales by Country')
    plt.xlabel('Country')
    plt.ylabel('Total Sales')
    plt.tight_layout()

    plt.show()
    pass

def plot_price_distribution():        
    plt.figure(figsize=(10, 6))
    plt.hist(df['PRICEEACH'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Price Distribution')
    plt.xlabel('Price Each')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()

    plt.show()
    pass

def plot_quantity_ordered_by_product_line():        

    product_line_quantity = df.groupby('PRODUCTLINE')['QUANTITYORDERED'].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    product_line_quantity.plot(kind='bar', color='coral', edgecolor='black')
    plt.title('Quantity Ordered by Product Line')
    plt.xlabel('Product Line')
    plt.ylabel('Total Quantity Ordered')
    plt.tight_layout()
    plt.show()
    pass

def plot_total_orders_by_country():
    orders_by_country = df.groupby('COUNTRY')['ORDERNUMBER'].nunique().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    orders_by_country.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Total Number of Orders by Country')
    plt.ylabel('') 
    plt.tight_layout()
    plt.show()
    pass

def plot_average_price_each_by_product_line():
    avg_price_product_line = df.groupby('PRODUCTLINE')['PRICEEACH'].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    avg_price_product_line.plot(kind='barh', color='lightgreen', edgecolor='black')
    plt.title('Average Price Each by Product Line')
    plt.xlabel('Average Price Each')
    plt.ylabel('Product Line')
    plt.tight_layout()
    plt.show()
    pass

def plot_sales_vs_msrp():

    plt.figure(figsize=(10, 6))
    plt.scatter(df['MSRP'], df['SALES'], alpha=0.5, color='orange')
    plt.title('Sales vs. MSRP')
    plt.xlabel('MSRP')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    pass

# Function to show the plot on the canvas
def show_plot(fig):
    for widget in frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def show_statistics():
    # Calculate statistics for the 'SALES' column
    mean_sales = df['SALES'].mean()
    median_sales = df['SALES'].median()
    mode_sales = df['SALES'].mode()[0]  # mode() returns a Series, get the first value
    std_dev_sales = df['SALES'].std()

    # Create a new popup window
    stats_window = tk.Toplevel(root)
    stats_window.title('Statistical Data')
    
    # Add labels to display the statistics
    tk.Label(stats_window, text=f'Mean: {mean_sales:.2f}', font=('Sans', '10')).pack(pady=2)
    tk.Label(stats_window, text=f'Median: {median_sales:.2f}', font=('Sans', '10')).pack(pady=2)
    tk.Label(stats_window, text=f'Mode: {mode_sales:.2f}', font=('Sans', '10')).pack(pady=2)
    tk.Label(stats_window, text=f'Standard Deviation: {std_dev_sales:.2f}', font=('Sans', '10')).pack(pady=2)
    
    # Button to close the statistics window
    ttk.Button(stats_window, text='Close', command=stats_window.destroy).pack(pady=10)


root = tk.Tk()
root.title('Data Visualization')
root.configure(bg='cyan')

frame = tk.Frame(root, bg='lime') 
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

style = ttk.Style()
style.configure('TButton', font=('Sans', '10', 'bold'), borderwidth='4')
style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

stats_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Statistics', menu=stats_menu)
stats_menu.add_command(label='Show Statistics', command=show_statistics)

buttons = [
    ('Show Sales Trend', plot_sales_trend),
    ('Show Quantity vs Price', plot_quantity_vs_price),
    ('Show Total Sales by Country', plot_total_sales_by_country),
    ('Show Price Distribution', plot_price_distribution),
    ('Show Quantity Ordered by Product Line', plot_quantity_ordered_by_product_line),
    ('Show Total Orders by Country', plot_total_orders_by_country),
    ('Show Average Price Each by Product Line', plot_average_price_each_by_product_line),
    ('Show Sales vs MSRP', plot_sales_vs_msrp)
]

for btn_text, btn_command in buttons:
    button = ttk.Button(root, text=btn_text, command=btn_command, style='TButton')
    button.pack(side=tk.LEFT, padx=5, pady=5, ipadx=10, ipady=5)

root.mainloop()




