// ==UserScript==
// @name        Kuntakartta to kml
// @namespace   Geocache.fi Kuntakartta to kml
// @include     *://www.geocache.fi/stat/other/jakauma.php*
// @exclude     *://www.geocache.fi/stat/other/jakauma.php?kuntalista*
// @require     https://raw.githubusercontent.com/eligrey/FileSaver.js/master/FileSaver.js
// @version     1
// @grant       none
// ==/UserScript==

if (confirm('Luodaanko Kuntakartta.kml?')) {
  createkml();
}

function createkml(){
  var now = new Date();
  var date = now.toLocaleDateString();

  var data = [];
  var stats = [];
  var findcount = 0;
  var jakaumataulukko = document.querySelectorAll("tbody");
  for(i = 0; i < jakaumataulukko.length; i++) {
      if (jakaumataulukko[i].innerHTML.indexOf("<tr><th valign=\"top\" align=\"center\"><b>Sija</b></th>") === 0){
        jakaumataulukko = jakaumataulukko[i];
        break;
      }
  }
  var tr = jakaumataulukko.querySelectorAll("tr");
  for (i = 0; i < tr.length; i++){
    if (tr[i].querySelector("th")){
      if (typeof sarakkeet === 'undefined'){
        sarakkeet = [];
        var th = tr[i].querySelectorAll("th");
        for (ii = 0; ii < th.length; ii++){
          if (th[ii].querySelector("b")){
            sarakkeet.push(th[ii].querySelector("b").innerHTML);
          } else {
            sarakkeet.push(th[ii].querySelector("img").getAttribute("alt"));
          }
        }
      }
    } else {
      stats = [];
      var td = tr[i].querySelectorAll("td");
      for (ii = 0; ii < td.length; ii++){
        stats.push(td[ii].textContent);
      }
      data.push(stats);
    }
  }

  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", "https://raw.githubusercontent.com/geoharo/Geokml/master/Firefox/Kuntarajat2017.kml", false ); // false for synchronous request
  xmlHttp.send(null);
  var kml = xmlHttp.responseText;
  
  var re;
  var original;
  var replacement;
  var PAYLOAD;
  var COLOR;

  for (i = 0; i < data.length; i++){
    PAYLOAD = data[i][0] + data[i][1] + " Yht. " + data[i][15] + " //";
    if (data[i][15] != "0" && data[i][15] != "0%"){
      COLOR = "#poly-009D57-1-0";
      findcount = findcount + 1;      
      for (ii = 2; ii < 15; ii++){
        if (data[i][ii] != "0" && data[i][ii] != "0%"){
          PAYLOAD = PAYLOAD + " " + sarakkeet[ii] + " " + data[i][ii] + " /";
        }
      }
    } else {
      COLOR = "#poly-DB4436-1-64";
    }
    re = "<name>" + data[i][1] + "</name>[^]*<\/styleUrl>";
    original = new RegExp(re, 'g');
    replacement = kml.match(original).toString().replace("CDATA[]","CDATA[" + PAYLOAD + "]").replace("<styleUrl>","<styleUrl>" + COLOR);
    kml = kml.replace(original,replacement).replace("Kuntakartta 2017","Kuntakartta " + date);    
  }
  var blob = new Blob([kml], {type: "text/plain;charset=utf-8"});
  saveAs(blob, "Kuntakartta.kml");
}