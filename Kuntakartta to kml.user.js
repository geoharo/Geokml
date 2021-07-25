// ==UserScript==
// @name        Kuntakartta to kml
// @namespace   Geocache.fi Kuntakartta to kml
// @include     *://www.geocache.fi/stat/other/jakauma.php*
// @exclude     *://www.geocache.fi/stat/other/jakauma.php?kuntalista*
// @version     3.0
// @grant       none
// @license     MIT
// @copyright   2017, geoharo (https://openuserjs.org/users/geoharo)
// @updateURL   https://openuserjs.org/meta/geoharo/Kuntakartta_to_kml.meta.js
// ==/UserScript==


//FILESAVER
/*a local copy of FileSaver By Eli Grey, http://eligrey.com:

/*
* FileSaver.js
* A saveAs() FileSaver implementation.
*
* By Eli Grey, http://eligrey.com
*
* License : https://github.com/eligrey/FileSaver.js/blob/master/LICENSE.md (MIT)
* source  : http://purl.eligrey.com/github/FileSaver.js
*/

// The one and only way of getting global scope in all environments
// https://stackoverflow.com/q/3277182/1008999
var _global = typeof window === 'object' && window.window === window
  ? window : typeof self === 'object' && self.self === self
  ? self : typeof global === 'object' && global.global === global
  ? global
  : this

function bom (blob, opts) {
  if (typeof opts === 'undefined') opts = { autoBom: false }
  else if (typeof opts !== 'object') {
    console.warn('Deprecated: Expected third argument to be a object')
    opts = { autoBom: !opts }
  }

  // prepend BOM for UTF-8 XML and text/* types (including HTML)
  // note: your browser will automatically convert UTF-16 U+FEFF to EF BB BF
  if (opts.autoBom && /^\s*(?:text\/\S*|application\/xml|\S*\/\S*\+xml)\s*;.*charset\s*=\s*utf-8/i.test(blob.type)) {
    return new Blob([String.fromCharCode(0xFEFF), blob], { type: blob.type })
  }
  return blob
}

function download (url, name, opts) {
  var xhr = new XMLHttpRequest()
  xhr.open('GET', url)
  xhr.responseType = 'blob'
  xhr.onload = function () {
    saveAs(xhr.response, name, opts)
  }
  xhr.onerror = function () {
    console.error('could not download file')
  }
  xhr.send()
}

function corsEnabled (url) {
  var xhr = new XMLHttpRequest()
  // use sync to avoid popup blocker
  xhr.open('HEAD', url, false)
  try {
    xhr.send()
  } catch (e) {}
  return xhr.status >= 200 && xhr.status <= 299
}

// `a.click()` doesn't work for all browsers (#465)
function click (node) {
  try {
    node.dispatchEvent(new MouseEvent('click'))
  } catch (e) {
    var evt = document.createEvent('MouseEvents')
    evt.initMouseEvent('click', true, true, window, 0, 0, 0, 80,
                          20, false, false, false, false, 0, null)
    node.dispatchEvent(evt)
  }
}

var saveAs = _global.saveAs || (
  // probably in some web worker
  (typeof window !== 'object' || window !== _global)
    ? function saveAs () { /* noop */ }

  // Use download attribute first if possible (#193 Lumia mobile)
  : 'download' in HTMLAnchorElement.prototype
  ? function saveAs (blob, name, opts) {
    var URL = _global.URL || _global.webkitURL
    var a = document.createElement('a')
    name = name || blob.name || 'download'

    a.download = name
    a.rel = 'noopener' // tabnabbing

    // TODO: detect chrome extensions & packaged apps
    // a.target = '_blank'

    if (typeof blob === 'string') {
      // Support regular links
      a.href = blob
      if (a.origin !== location.origin) {
        corsEnabled(a.href)
          ? download(blob, name, opts)
          : click(a, a.target = '_blank')
      } else {
        click(a)
      }
    } else {
      // Support blobs
      a.href = URL.createObjectURL(blob)
      setTimeout(function () { URL.revokeObjectURL(a.href) }, 4E4) // 40s
      setTimeout(function () { click(a) }, 0)
    }
  }

  // Use msSaveOrOpenBlob as a second approach
  : 'msSaveOrOpenBlob' in navigator
  ? function saveAs (blob, name, opts) {
    name = name || blob.name || 'download'

    if (typeof blob === 'string') {
      if (corsEnabled(blob)) {
        download(blob, name, opts)
      } else {
        var a = document.createElement('a')
        a.href = blob
        a.target = '_blank'
        setTimeout(function () { click(a) })
      }
    } else {
      navigator.msSaveOrOpenBlob(bom(blob, opts), name)
    }
  }

  // Fallback to using FileReader and a popup
  : function saveAs (blob, name, opts, popup) {
    // Open a popup immediately do go around popup blocker
    // Mostly only available on user interaction and the fileReader is async so...
    popup = popup || open('', '_blank')
    if (popup) {
      popup.document.title =
      popup.document.body.innerText = 'downloading...'
    }

    if (typeof blob === 'string') return download(blob, name, opts)

    var force = blob.type === 'application/octet-stream'
    var isSafari = /constructor/i.test(_global.HTMLElement) || _global.safari
    var isChromeIOS = /CriOS\/[\d]+/.test(navigator.userAgent)

    if ((isChromeIOS || (force && isSafari)) && typeof FileReader !== 'undefined') {
      // Safari doesn't allow downloading of blob URLs
      var reader = new FileReader()
      reader.onloadend = function () {
        var url = reader.result
        url = isChromeIOS ? url : url.replace(/^data:[^;]*;/, 'data:attachment/file;')
        if (popup) popup.location.href = url
        else location = url
        popup = null // reverse-tabnabbing #460
      }
      reader.readAsDataURL(blob)
    } else {
      var URL = _global.URL || _global.webkitURL
      var url = URL.createObjectURL(blob)
      if (popup) popup.location = url
      else location.href = url
      popup = null // reverse-tabnabbing #460
      setTimeout(function () { URL.revokeObjectURL(url) }, 4E4) // 40s
    }
  }
)

_global.saveAs = saveAs.saveAs = saveAs

if (typeof module !== 'undefined') {
  module.exports = saveAs;
}






//KUNTAKARTTA TO KML

if (confirm('Luodaanko Kuntakartta.kml?')) {
  try {
    luokml();
	}
	catch (e) {
    console.log("Error", e.stack);
    console.log("Error", e.name);
    console.log("Error", e.message);
	}
}

function luokml() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "https://raw.githubusercontent.com/geoharo/Geokml/master/Kuntarajat.kml", false); // false for synchronous request //Noudetaan blank-kuntarajat.kml
    xmlHttp.send(null);
    var kml = xmlHttp.responseText;


    var data = [];
    var stats = [];
    var findcount = 0;
    var yhtcolumn = 0;
    var i, ii, otsikot, url;

    var jakaumataulukko = document.querySelector('table[class="border sortable"]');
    if (jakaumataulukko) {
      console.log("Löytötaulukko paikkakunnittain löydetty");
      
      var tr = jakaumataulukko.querySelectorAll("tr");
        //console.log(tr.length-1 + " kuntaa");
        for (i = 0; i < tr.length; i++) {
            if (tr[i].querySelector("th")) { //OTSIKKORIVI
                if (typeof otsikot === 'undefined') {
                    otsikot = [];
                    otsikot.push("URL");
                    var th = tr[i].querySelectorAll("th");
                    for (ii = 0; ii < th.length; ii++) {
                        if (th[ii].querySelector("b")) { //jos boldattu
                            otsikot.push(th[ii].querySelector("b").innerHTML);
                        }
                        else if(th[ii].querySelector("img") === null){ //jos ei ole kuva
                            otsikot.push(th[ii].innerText);
                        }
                        else { //kuvat
                            otsikot.push(th[ii].querySelector("img").getAttribute("alt"));
                        }
                        if (otsikot[ii] === "Yht."){
                            yhtcolumn = ii;
                            //console.log(yhtcolumn + "YHTCOL");
                        }
                        //console.log(otsikot[ii]); //Otsikkojen tulostus
                    }
                }
            }else{ //KUNTARIVI
                
                stats = [];
                var td = tr[i].querySelectorAll("td");
                //console.log(td.innerHTML);  
              	
                for (ii = 0; ii < td.length; ii++) {
                  if (ii == 0){
                    var linkki = td[ii].querySelector('a');
                    if (linkki !== null) {
                      //console.log("Linkki löytyy");                      
                      url =  "(https://www.geocache.fi" + linkki.getAttribute('href') + ")";
                      stats.push(url);
                    };
                  };
                    
                  stats.push(td[ii].textContent);
                  //console.log(td[ii].textContent); //Solusisällön tulostus
                }
                data.push(stats); //Kuntadatat talteen
            }
        }
        
      	console.log("Löytötaulukko paikkakunnittain luettu");
      
      //Jakaumataulukko käsitelty
        var re;
        var regex;
        var oldkmlstr;
        var CDATA;
        var newkmlstr;
        var COLOR;
        var kunta;

			  for (i = 0; i < data.length - 1; i++) {
            url = data[i][0];
            kunta = data[i][1];
            console.log(i + ": " + kunta);
            CDATA = kunta + " " + url + " Yht. " + data[i][yhtcolumn] + " //";
            if (data[i][yhtcolumn] != "0" && data[i][yhtcolumn] != "0%") {//Kunnasta on löytynyt vähintään yksi kätkö
                COLOR = "#poly-00D079-1000-5"; //vihreä
                findcount = findcount + 1;
                for (ii = 2; ii < yhtcolumn; ii++) {
                    if (data[i][ii] != "0" && data[i][ii] != "0%") {//append kätkötyypeittäin
                        CDATA = CDATA + " " + otsikot[ii] + " " + data[i][ii] + " /";
                    }
                }
            }
            else { //Kunnasta ei ole löytynyt yhtään kätköä
                COLOR = "#poly-DB4436-1000-64"; //punainen
            }
            //console.log(i + " " + data[i][0] + ": " + CDATA); //Tulosta kunta ja CDDATA
            re = "<name>" + kunta + "<[^]*?<\/styleUrl>"; //Haetaan kml:stä kunnan nimellä //[^] 'multiple line .'
            regex = new RegExp(re, 'g');
            oldkmlstr = kml.match(regex)[0];
            newkmlstr = oldkmlstr.replace("CDATA[]", "CDATA[" + CDATA + "]").replace("<styleUrl>", "<styleUrl>" + COLOR);
            kml = kml.replace(oldkmlstr, newkmlstr);

        }
        var pvm = new Date().toJSON().slice(0,10).split('-').reverse().join('.');
        kml = kml.replace("<name>Kuntarajat</name>","<name>Kuntakartta " + pvm + "</name>");
      
      	console.log("Kml käsitelty");
      
      //EXPORT KUNTAKARTTA.KML
        var blob = new Blob([kml], {
            type: "text/plain;charset=utf-8"
        });
        saveAs(blob, "Kuntakartta.kml");
        
      	console.log("Kml tallennettu");

    }else{
        alert("Geocache.fi -sivu on muuttunut, scripti ei löytänyt jakaumataulukkoa.");
    }

}