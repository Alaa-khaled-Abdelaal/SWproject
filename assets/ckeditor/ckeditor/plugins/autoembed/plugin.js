﻿
(function(){function m(a,g){var b=a.editable().findOne('a[data-cke-autoembed="'+g+'"]'),c=a.lang.autoembed,d;if(b&&b.data("cke-saved-href")){var b=b.data("cke-saved-href"),e=CKEDITOR.plugins.autoEmbed.getWidgetDefinition(a,b);if(e){var f="function"==typeof e.defaults?e.defaults():e.defaults,f=CKEDITOR.dom.element.createFromHtml(e.template.output(f)),h,k=a.widgets.wrapElement(f,e.name),l=new CKEDITOR.dom.documentFragment(k.getDocument());l.append(k);(h=a.widgets.initOn(f,e))?(d=a.showNotification(c.embeddingInProgress,
"info"),h.loadContent(b,{noNotifications:!0,callback:function(){var b=a.editable().findOne('a[data-cke-autoembed="'+g+'"]');if(b){var c=a.getSelection(),e=a.createRange(),f=a.editable();a.fire("saveSnapshot");a.fire("lockSnapshot",{dontUpdate:!0});var j=c.createBookmarks(!1)[0],i=j.startNode,h=j.endNode||i;CKEDITOR.env.ie&&(9>CKEDITOR.env.version&&!j.endNode&&i.equals(b.getNext()))&&b.append(i);e.setStartBefore(b);e.setEndAfter(b);f.insertElement(k,e);f.contains(i)&&f.contains(h)?c.selectBookmarks([j]):
(i.remove(),h.remove());a.fire("unlockSnapshot")}d.hide();a.widgets.finalizeCreation(l)},errorCallback:function(){d.hide();a.widgets.destroy(h,!0);a.showNotification(c.embeddingFailed,"info")}})):a.widgets.finalizeCreation(l)}else window.console&&window.console.log("[CKEDITOR.plugins.autoEmbed] Incorrect config.autoEmbed_widget value. No widget definition found.")}}var n=/^<a[^>]+href="([^"]+)"[^>]*>([^<]+)<\/a>$/i;CKEDITOR.plugins.add("autoembed",{requires:"autolink,undo",lang:"cs,de,en,it,ku,nb,pl,pt-br,tr,zh",
init:function(a){var g=1,b;a.on("paste",function(c){if(c.data.dataTransfer.getTransferType(a)==CKEDITOR.DATA_TRANSFER_INTERNAL)b=0;else{var d=c.data.dataValue.match(n);if(b=null!=d&&decodeURI(d[1])==decodeURI(d[2]))c.data.dataValue='<a data-cke-autoembed="'+ ++g+'"'+c.data.dataValue.substr(2)}},null,null,20);a.on("afterPaste",function(){b&&m(a,g)})}});CKEDITOR.plugins.autoEmbed={getWidgetDefinition:function(a,g){var b=a.config.autoEmbed_widget||"embed,embedSemantic",c,d=a.widgets.registered;if("string"==
typeof b)for(b=b.split(",");c=b.shift();){if(d[c])return d[c]}else if("function"==typeof b)return d[b(g)];return null}}})();