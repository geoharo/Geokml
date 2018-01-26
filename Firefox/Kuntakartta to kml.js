// ==UserScript==
// @name        Kuntakartta to kml
// @namespace   Geocache.fi Kuntakartta to kml
// @include     *://www.geocache.fi/stat/other/jakauma.php*
// @exclude     *://www.geocache.fi/stat/other/jakauma.php?kuntalista*
// @version     1.0.1
// @grant       none
// ==/UserScript==








/* FileSaver.js
 * A saveAs() FileSaver implementation.
 * 1.3.5
 * 2018-01-22 15:49:54
 *
 * By Eli Grey, https://eligrey.com
 * License: MIT
 *   See https://github.com/eligrey/FileSaver.js/blob/master/LICENSE.md
 */

/*global self */
/*jslint bitwise: true, indent: 4, laxbreak: true, laxcomma: true, smarttabs: true, plusplus: true */

/*! @source http://purl.eligrey.com/github/FileSaver.js/blob/master/src/FileSaver.js */

var saveAs = saveAs || (function(view) {
	"use strict";
	// IE <10 is explicitly unsupported
	if (typeof view === "undefined" || typeof navigator !== "undefined" && /MSIE [1-9]\./.test(navigator.userAgent)) {
		return;
	}
	var
		  doc = view.document
		  // only get URL when necessary in case Blob.js hasn't overridden it yet
		, get_URL = function() {
			return view.URL || view.webkitURL || view;
		}
		, save_link = doc.createElementNS("http://www.w3.org/1999/xhtml", "a")
		, can_use_save_link = "download" in save_link
		, click = function(node) {
			var event = new MouseEvent("click");
			node.dispatchEvent(event);
		}
		, is_safari = /constructor/i.test(view.HTMLElement) || view.safari
		, is_chrome_ios =/CriOS\/[\d]+/.test(navigator.userAgent)
		, throw_outside = function(ex) {
			(view.setImmediate || view.setTimeout)(function() {
				throw ex;
			}, 0);
		}
		, force_saveable_type = "application/octet-stream"
		// the Blob API is fundamentally broken as there is no "downloadfinished" event to subscribe to
		, arbitrary_revoke_timeout = 1000 * 40 // in ms
		, revoke = function(file) {
			var revoker = function() {
				if (typeof file === "string") { // file is an object URL
					get_URL().revokeObjectURL(file);
				} else { // file is a File
					file.remove();
				}
			};
			setTimeout(revoker, arbitrary_revoke_timeout);
		}
		, dispatch = function(filesaver, event_types, event) {
			event_types = [].concat(event_types);
			var i = event_types.length;
			while (i--) {
				var listener = filesaver["on" + event_types[i]];
				if (typeof listener === "function") {
					try {
						listener.call(filesaver, event || filesaver);
					} catch (ex) {
						throw_outside(ex);
					}
				}
			}
		}
		, auto_bom = function(blob) {
			// prepend BOM for UTF-8 XML and text/* types (including HTML)
			// note: your browser will automatically convert UTF-16 U+FEFF to EF BB BF
			if (/^\s*(?:text\/\S*|application\/xml|\S*\/\S*\+xml)\s*;.*charset\s*=\s*utf-8/i.test(blob.type)) {
				return new Blob([String.fromCharCode(0xFEFF), blob], {type: blob.type});
			}
			return blob;
		}
		, FileSaver = function(blob, name, no_auto_bom) {
			if (!no_auto_bom) {
				blob = auto_bom(blob);
			}
			// First try a.download, then web filesystem, then object URLs
			var
				  filesaver = this
				, type = blob.type
				, force = type === force_saveable_type
				, object_url
				, dispatch_all = function() {
					dispatch(filesaver, "writestart progress write writeend".split(" "));
				}
				// on any filesys errors revert to saving with object URLs
				, fs_error = function() {
					if ((is_chrome_ios || (force && is_safari)) && view.FileReader) {
						// Safari doesn't allow downloading of blob urls
						var reader = new FileReader();
						reader.onloadend = function() {
							var url = is_chrome_ios ? reader.result : reader.result.replace(/^data:[^;]*;/, 'data:attachment/file;');
							var popup = view.open(url, '_blank');
							if(!popup) view.location.href = url;
							url=undefined; // release reference before dispatching
							filesaver.readyState = filesaver.DONE;
							dispatch_all();
						};
						reader.readAsDataURL(blob);
						filesaver.readyState = filesaver.INIT;
						return;
					}
					// don't create more object URLs than needed
					if (!object_url) {
						object_url = get_URL().createObjectURL(blob);
					}
					if (force) {
						view.location.href = object_url;
					} else {
						var opened = view.open(object_url, "_blank");
						if (!opened) {
							// Apple does not allow window.open, see https://developer.apple.com/library/safari/documentation/Tools/Conceptual/SafariExtensionGuide/WorkingwithWindowsandTabs/WorkingwithWindowsandTabs.html
							view.location.href = object_url;
						}
					}
					filesaver.readyState = filesaver.DONE;
					dispatch_all();
					revoke(object_url);
				}
			;
			filesaver.readyState = filesaver.INIT;

			if (can_use_save_link) {
				object_url = get_URL().createObjectURL(blob);
				setTimeout(function() {
					save_link.href = object_url;
					save_link.download = name;
					click(save_link);
					dispatch_all();
					revoke(object_url);
					filesaver.readyState = filesaver.DONE;
				});
				return;
			}

			fs_error();
		}
		, FS_proto = FileSaver.prototype
		, saveAs = function(blob, name, no_auto_bom) {
			return new FileSaver(blob, name || blob.name || "download", no_auto_bom);
		}
	;
	// IE 10+ (native saveAs)
	if (typeof navigator !== "undefined" && navigator.msSaveOrOpenBlob) {
		return function(blob, name, no_auto_bom) {
			name = name || blob.name || "download";

			if (!no_auto_bom) {
				blob = auto_bom(blob);
			}
			return navigator.msSaveOrOpenBlob(blob, name);
		};
	}

	FS_proto.abort = function(){};
	FS_proto.readyState = FS_proto.INIT = 0;
	FS_proto.WRITING = 1;
	FS_proto.DONE = 2;

	FS_proto.error =
	FS_proto.onwritestart =
	FS_proto.onprogress =
	FS_proto.onwrite =
	FS_proto.onabort =
	FS_proto.onerror =
	FS_proto.onwriteend =
		null;

	return saveAs;
}(
	   typeof self !== "undefined" && self
	|| typeof window !== "undefined" && window
	|| this
));





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