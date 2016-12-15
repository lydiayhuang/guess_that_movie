import random
import requests

def random_movie_id():
    movie_ids = ["tt0068646","tt0099685","tt0110912","tt0114814","tt0078788","tt0117951","tt0137523","tt0108052","tt0118749","tt0105236","tt0111161","tt0073195","tt0075314","tt0119488","tt0088763","tt0071562","tt0116282","tt0175880","tt0086250","tt0265666","tt0246578","tt0091763","tt0113277","tt0169547","tt0118715","tt0081398","tt1235166","tt0407887","tt0129387","tt0110413","tt0317248","tt0087843","tt0120735","tt0120382","tt0114709","tt0078748","tt0128445","tt0133093","tt0468569","tt0114369","tt0119217","tt0090605","tt0077416","tt0070047","tt0073486","tt0112641","tt0108399","tt0401792","tt0172495","tt0082971","tt0100150","tt0120601","tt0095016","tt0034583","tt1250777","tt0482571","tt0209144","tt0361748","tt0092991","tt0107290","tt0120689","tt0067116","tt0105695","tt0120706","tt0071315","tt0780504","tt0083907","tt0109830","tt0104348","tt0084787","tt0033467","tt0090756","tt0092005","tt0081505","tt0070917","tt0338013","tt0093779","tt0139239","tt0372784","tt0066921","tt0093058","tt0167260","tt0103064","tt0120363","tt0120815","tt0112851","tt0097576","tt0387564","tt0097937","tt0310793","tt0328107","tt0181875","tt0146882","tt1853728","tt0050083","tt0095953","tt0181689","tt0167261","tt0058150","tt1285016",
"tt0144084","tt0119654","tt0477348","tt0080339","tt0469494","tt0102138","tt0360717","tt0088247","tt0120737","tt0266697","tt0102926","tt0090863","tt0480025","tt0038650","tt0206634","tt0107207","tt0120586","tt0114746","tt0072890","tt0094226","tt0075860","tt0060196","tt0993846","tt0257044","tt1049413","tt0110632","tt0120780","tt0258463","tt0082010","tt0475276","tt0110148","tt0114660","tt0449059","tt0106519","tt0381061","tt0066999","tt0087363","tt0064115","tt0240772","tt0245712","tt0443453","tt0145660","tt0103776","tt0159097","tt0289043","tt0362270","tt0180093","tt0064505","tt0067128","tt0292644","tt0443706","tt0425112","tt0190590","tt0103873","tt0109686","tt0061852","tt0440963","tt0111149","tt0116367","tt0031381","tt0163651","tt1010048","tt0047296","tt0208092","tt0095705","tt0077975","tt0120188","tt0780536","tt0435761","tt1060277","tt0077402","tt0110932","tt0456912","tt0167404","tt0081070","tt0467406","tt0063442","tt0373469","tt0119396","tt0375063","tt0099487","tt0120863","tt0395169","tt0203119","tt0117802","tt0211915","tt1132620","tt0095765","tt0051201","tt1375666","tt0053604","tt0212338","tt0086197","tt0264464","tt0076666","tt0357413","tt0147612","tt0478311","tt1136608","tt0361596",
"tt0796366","tt1424432","tt1899353","tt0393109","tt0405094","tt0118147","tt0107048","tt0074119","tt0217869","tt0457430","tt0970179","tt0448134","tt0923752","tt0117318","tt0829482","tt0379786","tt0063350","tt0118655","tt0463854","tt0096257","tt0280609","tt0097165","tt0113161","tt0307987","tt0087332","tt0119008","tt0062622","tt0092099","tt1022603","tt0221073","tt0088847","tt0119229","tt0061578","tt0056592","tt0067185","tt1185616","tt1723811","tt0378194","tt0325980","tt0115734","tt0080684","tt0322802","tt0367089","tt0074958","tt0064116","tt0093870","tt0061418","tt0158983","tt0072271","tt0364725","tt1189073","tt1839492","tt0375912","tt0128442","tt0078346","tt0088993","tt0074860","tt0064665","tt0079470","tt0093822","tt1182345","tt0109445","tt1127180","tt0088846","tt0372183","tt0111495","tt0399146","tt1119646","tt0446029","tt0063462","tt1313092","tt0110074","tt0116695","tt0111257","tt0061512","tt0102685","tt1156398","tt1179947","tt0375679","tt0061722","tt1403865","tt0106489","tt1139797","tt0119822","tt0082096","tt1019452","tt0091064","tt1125849","tt0120338","tt0266543","tt0106977","tt0076759","tt0054997","tt0058461","tt0069995","tt0432283","tt0884328","tt0097351","tt1318514","tt1210166",
"tt0493430","tt0964517","tt1935179","tt1614989","tt1245492","tt2267998","tt2015381","tt2265171","tt1392190","tt0435625","tt0342172","tt0421715","tt0096895","tt0162661","tt0041959","tt0316654","tt0274309","tt0185937","tt1855199","tt0910970","tt1966604","tt0091886","tt0290334","tt0145487","tt0053125","tt0454848","tt0119094","tt1490017","tt0266308","tt1229238","tt0117060","tt0369339","tt1631867","tt1706620","tt0120611","tt1655442","tt0104036","tt0427312","tt0120201","tt0388888","tt0387898","tt0091251","tt1436045","tt0452623","tt1192628","tt0111507","tt0436613","tt0276919","tt0082085","tt1183919","tt0305206","tt0824747","tt0112573","tt0101889","tt0100935","tt0421082","tt1226774","tt0118887","tt0364569","tt0947798","tt0353969","tt0067992","tt1024648","tt2103281","tt0072251","tt1306980","tt0125439","tt2278388","tt0421238","tt1704573","tt0338751","tt1606259","tt0058182","tt2076220","tt1748122","tt1232207","tt0177789","tt0202559","tt0094737","tt1259014","tt0066214","tt0465538","tt0119116","tt0278504","tt0365748","tt0076752","tt1305806","tt0092699","tt0089218","tt0048545","tt0139654","tt0460989","tt1196204","tt0292963","tt0043014","tt0298203","tt0317705","tt0098253","tt0217505","tt0103772",
"tt3544112","tt0075005","tt1399683","tt0099423","tt0118564","tt0077745","tt0252866","tt0163651","tt0252299","tt0050825","tt0416315","tt1341167","tt0097202","tt0098258","tt0140352","tt0099785","tt0099348","tt0307901","tt0063522","tt0064276","tt1587707","tt0212720","tt0100802","tt2053463","tt1726669","tt2125666","tt0854678","tt0062138","tt0096874","tt0187738","tt0113627","tt0084516","tt1340800","tt0049730","tt1714206","tt0068473","tt0057076","tt0181288","tt0108394","tt0198781","tt0454876","tt1920945","tt0088000","tt0083658","tt0057115","tt0077838","tt0105323","tt0095631","tt0083190","tt0080678","tt0075148","tt0052357","tt0067866","tt1788391","tt0085407","tt0978762","tt0055928","tt0113189","tt1213663","tt0126886","tt0079116","tt0049902","tt1259521","tt1045658","tt1979320","tt0319343","tt0096754","tt1454468","tt1798709","tt1535109","tt0115736","tt0468489","tt0408306","tt0181865","tt2872718","tt1877832","tt2737310","tt1095217","tt0120623","tt2582802","tt1130884","tt2488496","tt0104684","tt1817273","tt0116483","tt0079417","tt0185014","tt0407304","tt0109831","tt0083866","tt0113987","tt0121766","tt0106308","tt0091474","tt1584016","tt0084805","tt0101507","tt0097216","tt0101410","tt0109508","tt0095159",
"tt0090180","tt0081573","tt0270288","tt0120663","tt0070510","tt0190332","tt0092563","tt0055895","tt0848228","tt1853739","tt0074256","tt0119177","tt0114558","tt1386588","tt0411272","tt0094746","tt0120324","tt0117665","tt0498380","tt0054215","tt0104940","tt0892769","tt0143145","tt1193138","tt0499549","tt0470705","tt0434409","tt0032599","tt0887912","tt0099939","tt0268126","tt0118804","tt0419677","tt0272338","tt0311113","tt0096969","tt0049406","tt0105665","tt0290673","tt0403358","tt0103759","tt1189340","tt0493464","tt0388795","tt0065214","tt0104257","tt1016268","tt0093773","tt0113247","tt0234215","tt1663202","tt1431045","tt0118799","tt1157605","tt1020530","tt0110308","tt0411477","tt0298845","tt0032910","tt1017460","tt0095158","tt0086979","tt2980592","tt2446600","tt0152930","tt0274812","tt0333766","tt0870111","tt0362225","tt2294449","tt0315733","tt0101516","tt0085859","tt0075686","tt0097493","tt0057012","tt1091722","tt0071360","tt0409459","tt1139328","tt1038988","tt0409904","tt1232776","tt0117666","tt0098635","tt0303353","tt0091042","tt1045772","tt0816692","tt0053221","tt0041546","tt1024715","tt1457767","tt0082089","tt0080437","tt2345737","tt0203009","tt1289406","tt0208874","tt0286112",
"tt0096163","tt0117039","tt0082694","tt0073312","tt1120985","tt0076723","tt0099700","tt0094291","tt0073812","tt0929425","tt0085794","tt0093223","tt0478304","tt0093409","tt0420223","tt1972663","tt0110475","tt1204342","tt0479468","tt1446714","tt0071230","tt1606392","tt0112818","tt0338564","tt1216487","tt0202677","tt0056172","tt0889583","tt1012804","tt0097733","tt0106856","tt0783233","tt0116922","tt0089885","tt0032138","tt0371746","tt1568346","tt1255953","tt1675434","tt0031679","tt1242422","tt1540133","tt0101414","tt0383574","tt0038355","tt0086190","tt0398286","tt1282140","tt0449467","tt0033870","tt0107206","tt0163988","tt0042041","tt0118842","tt0145653","tt0368794","tt0100157","tt0093437","tt0155267","tt0903624","tt0096438","tt0040897","tt0335266","tt0117381","tt0166924","tt0358273","tt0078966","tt0272207","tt0464141","tt2053425","tt1478338","tt0053198","tt0986233","tt0296042","tt0120903","tt1450321","tt1034419","tt1345836","tt1276104","tt0167190","tt0765429","tt0408236","tt0075675","tt0469021","tt1270798","tt0115964","tt0091538","tt0134847","tt0383028","tt0840361","tt0489247","tt0317919","tt0064757","tt0109040","tt0891527","tt0988045","tt0464154","tt0109707","tt2802144","tt1865505",
"tt2395427","tt3076658","tt0362269","tt0065780","tt0112346","tt0114478","tt0068611","tt0086879","tt1832382","tt0790636","tt1843866","tt0112864","tt0116361","tt0317910","tt1321865","tt1320244","tt0107554","tt0059578","tt0382932","tt0116378","tt0118971","tt0054331","tt0105151","tt0427944","tt1931533","tt1790885","tt1074638","tt2567712","tt1109624","tt2382396","tt0280491","tt0243133","tt0245429","tt1560970","tt1906426","tt0473705","tt1082886","tt0095031","tt1512685","tt0097428","tt1116184","tt1464580","tt1568911","tt2059255","tt0092965","tt0108358","tt0268380","tt0356721","tt0112288","tt0087469","tt0401711","tt1226229","tt0117571","tt0368447","tt1232829","tt0093605","tt1300854","tt0287467","tt1663662","tt0465602","tt0029870","tt1084950","tt1323594","tt1077258","tt0119951","tt2101441","tt0120885","tt1615147","tt0352248","tt0082340","tt0087884","tt1392214","tt2494362","tt0070909","tt3460252","tt3170832","tt2582782","tt3799694","tt1895587","tt1226271","tt0093105","tt0069762","tt3311384","tt0094336","tt0131325","tt0066995","tt0078718","tt0070328","tt1205489","tt0103939","tt1542344","tt0099871","tt0265086","tt0985694","tt0983193","tt0120755","tt0038733","tt1764183","tt0178868","tt0076786",
"tt0074285","tt0118929","tt0054698","tt0146309","tt0945513","tt3040964","tt5213534","tt0111503","tt0114594","tt0171580","tt0099763","tt0118789","tt0363163","tt0091954","tt0120915","tt0107507","tt0086200","tt0112819","tt0455590","tt0108122","tt0090329","tt0165854","tt0162222","tt0210065","tt0099674","tt0109506","tt0765443","tt1170358","tt0079522","tt0116778","tt0165798","tt0830515","tt0104815","tt0090728","tt0070735","tt0112384","tt1959490","tt0907657","tt3553976","tt0399295","tt0104691","tt1091191","tt0113497","tt0472043","tt0403702","tt0355702","tt0372588","tt0088680","tt0125664","tt1740707","tt0119802","tt0110005","tt0265343","tt0120255","tt0123755","tt0115751","tt0085894","tt2562232","tt0086960","tt0298130","tt0113540","tt0102015","tt0078788","tt0299117","tt0424136","tt0386032","tt0071746","tt0808417","tt0230600","tt0096928","tt0196229","tt0462504","tt0047396","tt0078841","tt0120669","tt2911666","tt0040746","tt0070034","tt0105793","tt0088258","tt0302886","tt2784678","tt0042192","tt0079871","tt2545118","tt3659388","tt1313104","tt3850214","tt2080374","tt0083944","tt0887883","tt0087800","tt0062512","tt1172570","tt1814836","tt0073802","tt0101540","tt0097441","tt0299977","tt0074156","tt0069089",
"tt0285823","tt0074486","tt1465522","tt0060315","tt0045152","tt0298744","tt0129167","tt0119698","tt2381249","tt0103639","tt3235888","tt2820852","tt3395184","tt3397884","tt0099077","tt0266987","tt0373074","tt1625346","tt0060176","tt0070334","tt1800241","tt0122690","tt0079501","tt0052311","tt1937390","tt0368909","tt0025464","tt1065073","tt0086425","tt1560747","tt1646971","tt3416742","tt0098213","tt2397619","tt0430922","tt0108525","tt0080120","tt0118826","tt0104431","tt0309593","tt0070379","tt0119164","tt0083929","tt0462538","tt1190536","tt0404030","tt0093640","tt0838221","tt1408101","tt0100685","tt1951264","tt0039628","tt0319061","tt0122933","tt0052618","tt0088286","tt1596343","tt0084434","tt0327056","tt0367555","tt2124908","tt1777551","tt1124035","tt0079817","tt0081633","tt0102175","tt1489167","tt0069097","tt0034583","tt0101452","tt0374900","tt0093565","tt1242460","tt1322269","tt0120888","tt0102510","tt1605783","tt0107818","tt0442933","tt0104073","tt0800369","tt1054606","tt0313542","tt0070640","tt0095647","tt1456635","tt1392170","tt0195714","tt0089155","tt0325710","tt0110357","tt0070707","tt0047478","tt2870648","tt1570728","tt3464902","tt0088944","tt1637725","tt0405422","tt0058331","tt0059742"]
    return random.choice(movie_ids)


def random_movie_data():
    id = random_movie_id()
    url_base = "http://www.omdbapi.com/"
    query_string_data = {'i': id, 'r': 'json'}
    r = requests.get(url_base, params=query_string_data)
    return {k: r.json()[k] for k in ('Actors', 'Director',
                                     'Plot', 'Year', 'Title')}
