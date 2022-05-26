# cake_a_bake game programme
#
# programme map:
#
#
# declared imports
#
# dclared data structres
#
# declared functions
#
# imported libraries:
#
import random
#
import time,os,sys
#
#
# text image arrays:
#
pic0=("""
\u001b[34;1m                                                                                                    
                                      :```  ```                                                     
                                    `.-:://////..-`                    `` ````                      
                                   .-+/+so+/++o/+.``               ``.-:ossss:`                     
                       .-..:.`    `/sso/-````.:+//:`            `/:/ooosydhhyy+-.                   
                     ./oooo/+s/` .+sss:        ///+- ..  ` ``  .:o/o+:-..-:sdhysy`                  
                   ./+/-..../so. `+ss+         :/+++/ysooooo::-.:++o/       /yoo/`                  
                  .o++`     `...` oos:        `//+oydyo/:+osoy/.-+oos.       ohhs-                  
                  .++:   `.-+ssss.+ss+       `:/ososs.     -osy+``+sho       .hhs/. ``              
                  -//:`  `.-:--ss/.+ss:`  ``.:s+osso:       -hys: -ohd:      .syoo-`` `             
                  .://:`      .sss.`/o+/:::+o+/+ooso:        yss.  oyhs`   `.oyyo/.````             
                   `-/++:-..--oys:` `..::-::--:/`/sys.      .hyy.  :sys/:+oosoo+-.``````            
                    `.///+++/---`           ``..`./yys:`  `.sdh/`   +hyyyss+:-.```                  
                       .. ` ````           `.osho. .+syy++oshy- `    :/-.    `                      
                                           +oosss`` .--:::+:.```  `                                 
                                           .//+sy/` `  ``    `://:`                                 
                      ``--. `.-///+os/:``:` -++soo/`      ..:s+//++`                                
                      :-+o+oyyoso++shyso/-  `:+ssso.   ` `:sdy///::                                 
                       +sooo+/--.`.-oyos+. ```:ooss+`  `/+sooo/-:.`                                 
                       :sooo.       `yss+` `/-:oo+os/ `/sss+so::-  ``--`                            
                       `oooo+`     ./hdd:  . ` -ysssyssssoo+/::-`-/+oo+//-.````                     
                        :yyyy:-:+o+oyhdh+/-``  .osoyyyyyhss:`--``:/+o++ssooss++-                    
                       ..oyyyyhhhyo+++syysso-   :oosyyyyyso.`  `.:::o` ``.::/++`                    
                       ``/yyhds:.``    .shyhh`` `:osyyyyy//.`   -----`      ```                     
                   ``` ``:ydddh`        /dddh. ./ossyyys:`  ```.+::/+ooo//:-.                       
                  ``     /yhhhd/     `./ydddy`.`+yysyys.`    `./:-::-/+osyyy+`                      
                    `   `.-oyhhy..:+syhhhhhhy:..oso+sy-       -/:::`    `...`                       
                     `  `` .oosyso++++so++:-./:-ss+/o+`       :/++:.``                              
                       `    -+ssyo:.``` `  ``` `oo+/++       --++++oyyso/:-````                     
                             .-.o:.             .-::-`         ``..:oyyyysy+                        
                      `       `   . `                               `:--:-:::```                    
                                                                            .`        \u001b[0m""")
pic1=("""
\u001b[34;1m 
 ` `` ` ` `  ` ` ` `      ` `` ` ` `  ` ` ` `  ` `
 ` `  `   ` ```-:/+ossyo`      ` ` `  ` ` `      `
 `  `   ` `-+yhhdddddd+.+/.-...-..```  ``   `    `
 ``  `  `/yhdddddddddds`-o/:-.--.-::--.``   `     
`      .shdddddddddddddo..:/:.-..-../:/:.` `    ` 
` `  `-yddddddddddddddddho:--::/::::::--//o/:.` ` 
` ` -++ddddhyyhhhhhmdyso+//++o//////////+ydh//+`` 
` ``s:odddd+/so//+dMN+:::::/dmh//+oy+///:hdd+:/+` 
`  `s:sdddy:smmdydMNo:::::::smNhymNNh::::sddo::o `
   `:+yddd/:/+sdNNNms+/::::/omNNNms+/::::odd+/o. `
`` ` .sddy::::+mMmydmmo::/dNMmhdNm+::::::+dd+:. ``
`    `/dd+:::/mMm+:/+o/+++hds/:/dmh/:::::+dy` `   
` `   /dy::::/oy/::::+/::::/+/::/+:::::::+d+ `  ` 
      /do:://::::::::::::::::::::::::::::yd: `    
 `    /hy++//o+:::::::::::::::::::::::::o+d``     
 `    :o.:```.y/:::/shhyyhhy/::::::::::/o-h `  ` `
      -:`.--:o/::::+NNMMMMMNo:::::::::++`.s `     
 ` `  ..  `-oo/:::::/++++++/::::::::+o- `./  ` ` `
` `   `. ` ` `:+yo/:::::::::::::/oys-``` `.` `    
` `      `  ``+ddmdhyso+/::/+sydmdddds`    ` `  ` 
`      ` ``.oddhmdhhhhhhddddhdmdhhhhhds```    ` ` 
` `    ` .sdhhhmdhhhhhhhhhhdmdhhhhhhdd:```  ` ` ` 
 ` ````-sdhhhhdmhhhhhhhhhdmdhhhhhhdm+```` ` `  ` `
 `  `:ydhhhhhhmhhhhhhhhmmdhhhhhhdmdm/ ` ` `       
 ` `odhhhhhhdmmhhhhhhmmdhhhhhhdmdhhhh`` ` `  ` ` `
  :oooyhhhdhoydhhhhdhhyhdhhhdmdhhhhhm. `       `  
` o+:::/mh+.`dhhhhhh/::/yddmdhhhhhhhm/ `      ``  
` `/+++o/`  `mhhhhhds+++ydhhhhhhhhhhdo `        ` 
` ` `..`    `mhhhhhhhhhhhhhhhhhhhhhhdo ` `        
` `   ``   ``mhhhhhhhhhhhhhhhhhhhhhhdo```       ` 
 `  ` ` `   `dhhhhhhhhhhhhhhhhhhhhhhd+``` ` `  ` `
        `   `ohddhhdhhhhhhhhhhdhhhdds.``` ` `  `  
             +oosyyyyyhs++yhyyyyssos/``         ` 
` `    `     oyddddddhh- `+yhddddhyy/      `      
`   `  ` ` `-dmdddddddN+ `smddddddmmo`   `   `  ` 
         ` `oddddddddddd`.mdddddddddd. `   `  ` ` 
 `    ` ` ````-://++++/-``:+++++//:-`     ` ` `  `
 `  ` ` ` ``   `      ` ` `  ` ` ``` `  ` `    ` `
 ` `  ` ` `  ` ` ` `  ` ` `  ` ` ` `    ` `    ` `
 ` `` ` `   `` ` `    ` `   `  ` ` `    ` `    ` \u001b[0m""")

pic2=("""
\u001b[35;1m                                                                                
                                               .                                
                                               o/. ` o+                         
                                           `-/+oo+o/+sy                         
                                         `:+:.``./.:osy./os+`                   
                                        `o+/``:.`-/-`+dds:--..                  
                                        o/`:`--..-:-/+ody/+:`                   
                                       -o`./``-+:+/+osshm++/`                   
                                       :+`.`-+++shyyyysyy..-:.                  
                                       .s.::shhhyhyo-:oy-`-s/.                  
                                    .:+shhsooos//++osso-`:s.                    
                                 ``-+oyhdmmNNmddmNdy::-``d`                     
                               `.-:-..-oddooydy-oo-/---` s-                     
                              `.-..`--o/.----yy--:`-`.-. `o/`                   
                          `./-::..`.--s`  ..-:do-..```.:-  :s:                  
                         `/hs:--.``:..+.`  /+--yy:`...-.-..``/o/.               
                        ./hNo-/-``.:.-:o.  `o/..+ds. `.//:-..` .+o:`            
                       .-+md/:+/..`./--:d+  `+o/--+yo-  `.://+:. `:s:           
                       .-sN/hhos:...-:::omy.  -os+--:+o/-``.:+oy+  `/o          
                      `:.+Ns/dsyo-.``:oooodd/` `-/oo+/--/:-..-/+-  `.s.         
                   `:ohdo/od/yddho/:://yyyydds:`-``-/++oo/:.-`.````::y.         
                 `-smdhmmmmdhyss:+hs+oosodyymmdhs-`.``.::://+/:..`--/oso`       
                  .+sdNmhhhyydyysshhys+/:o//osy+syo+..---.--/::-//+..-:ho       
                  `+hyymdddhys++oosshhhyyyyydhysoo++/+sssso+/::---:.:+hs-       
                   .d+:/os+hmhdmyso/:--------//-:-----......---:/syhhym`        
                    :d+o+oyo+///ooos+/o++::-:/-.-/+o+++oo////+-/yyyo:o+         
                     /y//oho:.``-oy:-:::+shsoosss+//:/sso+++//+sms. -o          
                      .s:+yo/.``.+hd+-...omhh+:-:``  `+hmh+-.-:hs. `s`          
                       -s:shs-`..osd...  :dmmms.```  //om+` ./ys/  s:           
                        /o+dh/-..+yd.``.`:yyNmo`    ./..d` .:hh/` +/            
                         o/ydo:-.:hd`..``/s+sy+     -` .+ `-hyo/`-o             
                  ``  ```-oomy:`.-hm-``` -o:ss/ `` `:` -. .sdyo-.s`             
                ````....``+/mm+`.`sd/````.+:oy-`  `:-  .  -ddy/.s.              
                ```..--:/:/+yms.`.oms/.  :/:/s````-/`    `+Nso.+/               
          ```````.--:::::/:o+Ny-.`omd/```:/:+o.` `-o..   :hmo/-o`               
           ``.....-::/:://+s:Ns-``omNy``.o/:+/.`..+o`.` `/mds`s.                
             ``..---/////++y+Nh:.`ohMy:-.++/+s.``-ho-:- `oNh:./                 
                  ```.-::/+yyNN/`.ydNd:`.sdsoy...:ms++/ :hmo--                  
                       ```.-:+ho+sdyNN+-+ymhyh..-+dsss-:osy+-`                  
                             ``...``:syo/++oyy+/+osooo:.                        
                                          ``..`                
       \u001b[0m
         """)

pic3=("""
\u001b[33;1m
                                                                      `.`       
       -/+oo++o++/:.                                                :o++s-      
      :h-``    `.-:oo-                                             :y.  :h`     
      h:   -:..`    .y+                                           `h-    d-     
     .m`   ss/+o+.   `d-                                          .m     s+     
     -d    y:   :h.   oo         `````             `.-::--.`      -d     +s     
     /s    d-   `d-   +s     `-+o++++oo/.`       -oo/::-:/+oo:`   -d     /y     
     oo   `d-`.:y/   `h-    /s/.      `-+s/    .so.         `+y-  .d     :h     
     s+    /++/:`   .y/   `so`           `os` `h:             .h: `m`    :h     
     y/          `:ss.    +s  -s+`   `/+`  os s+  /yo`   +y+`  .d. y:    :h     
     h:         `:/oso-   m. `dsNo   sdhh  `d:m` .msM/  -Nsm:   oo /y    /s     
     h:              .os..m`  yNN:   oNMs   osm  `yNd.  `hNh`   :h `d.   s+     
     h-   /yooo/`      -h:m`  `..     --`   /yd.  ```  ` ```    :y  /y  `d.     
     h-   oo  `+y       -dm.    -yhs.       s+y/     /dmd/      s+   os-oo      
     h-   y/   -d`       dyo    yMMMy      .d.-d`    yMMMo     :h`    -/:`      
     h:   h+-:/s:       -d.h-   /NMd-     .y:  +s`   `oy+`   `/y.     +oo+`     
     h:   -:::-`      .+y- -y:   --`    ./s-    /s:`      `./s+`     `d.`so     
     h:          `.-/oo:`   .+o/-.`..-/oo:`      .+o+/://+o+:`        +s:s+     
     so///++++++oo+/-.        `:/+++/:-`            .---.`             -:-      
     `....``````                                                                
    \u001b[0m
      """)


pic4=("""
\u001b[32;1m
                                                          -::::                                     
                                                         /-. ./-.                                   
                                                         /-/-+:--                                   
        -`                                                 .+:/                                     
        o+                                                 +--o`           .::--.                   
       --.+`                            -/::-             /:-.-+           -/ ``:/`                 
       /  .+                          `/-` ./            .y....+:           -/   .o                 
       -. ./                          +.  `o             s:-----o.          -/    /-                
        -/:                          /.   `o            :/....``.o.-.     `::     ./                
        ::+                          o     -+.  `.+o:::-o//::::::+ydds...::.      +`                
        -/o                          +`     .++/shs/`         `....-:/+-o//.`   `:-                 
    `---:+/.                         .+`  `-/:-.:-..`      `:/-....-::.:+.o-::.::`                  
 `..+./.:+:o:.`                       `+-::``/-.``.-/-    `+.        `-/- o`  -+.            ::/    
/.-:--: .///-//::.`                   `/:`  +`     ` +-   +`            o`./-``:+:       `  /..+    
+..:-----------+++/:.                -o`    /     `s.`o   o     :/      :-  ...--:/`   `/:::--o::::/
 .o/-:.--.---..-.-o.`               -+    ` -:.`   ``+-   o`    -:     `o`    `.-/++    :/.- :-``.-/
  +.+:-:-:-:-:---o:.``             `o  `: ..-`/+//+++. `` `s-`       `/+`  .`  `o`/::   `+-:/.oo.`  
  `+/---:--:----h/-.-o             o`   -+`                 :++/////+/.   `.`  -+   +  `+:/``::/`   
`/:s::. ``` ` `+o::s`s            -+     `s.                   `:-`        .  -y    + :+/.          
`o.`++:::::::::`  .o-.::-         s`     -://`            `:. -: `/:        `//o    o++:            
  -:::----------:+o/.::::::---`  `o      `/:///-          -:: :-  `+     `:sd+om.  `o/`             
                        `--:-:/+/o/        `  `-/:::.`     `   .::-``-:+ymNNNNNN/  `s               
                             ```.++:::`          ``s::+hyyyyyyyho:::omNNNNNNNNNNo .-o               
                                 ::  `/`    `      `/dmNNNNNNNNNmssymNNNNNNNNNNNo:-`+               
                                 -/   `/  .:.::      +NNNNNdddmdmNmmNmmmmmNNNNNN-`:o.               
                                 `+    /  --.-+      `dNNNNhmdddddddddmdhdNNNNNh  `o                
                                  o` `:.   `..`       dNNNNmmmmmmmmmmmmmmmNNNNN-  /-                
                                  //:-`       `    ``-NNNdhhdmNNNmNNNNmmNNNNNNo   o                 
                                  `s` --    -+:/:-+:+dNy:.``.:shyo+++ooydNdods``:-s`                
                                   .o -:    +-  `.-:+d/     `:.`     .  `/s//  /. :-                
                                    ::      -+      /-              -o-::--`   +` `o                
                                     o/:-    .      o               :/````     `:--+:               
                                     /- /`          o               `o:---:.        :/`             
                                    -o``/`          +-              :+.    +      `:-/o/.``         
                                  `o/.-.             :+.``        ./:`/---:.-:`   -:  .+.::/-       
`````````                         .+:/:.`..````       `.-:::::::::-`    `   .-`````.-:-....`+:      
````````                              `.--.--:::::::::://:///::::////://::::::::------...-.--`   \u001b[0m""")

pic5=("""
\u001b[31;1m
                                            -ossym`                                                 
                                           +d::`h/                                                  
                                           .y:  o/                                                  
                                            .d  -h                                                  
                                             d:  m`                                                 
                                             +h  d-                                                 
                                             `N- y+                                                 
                                              ys oy                                                 
                                              :N`:m                                                 
                                               m/`N`                                                
                                               oh m-                                                
                                               .N`y+                                                
                                                m:os                                                
                                                ss:d`-/++/-`                                        
                                           -+yysyd-My/-..-/yy-                                      
                                         :hy:`   y-y `-     .ho                                     
                                        sh-   --`+:do/`      `h+                                    
                                       sy`    .:/oyo`         -N`                                   
                                      -m`         `           `N.    `                              
                                      so                      `N. :ooos:`                           
                            ``        oy                      om:+m-  :yoosoo+/:-.`                 
                           +sos`    ``:N/                    :y/:-. -`  `  `..-:/+oo+/:.`           
                          -d` +s.-+oooooy+`                 :o`     `  .+o/:.`      `-:+ss+-`       
        /so:      ``..:/++yh. -+++:`    `/s.            `.-sy///-`        .:---`         `:oyo/++/- 
       `N`.h+:/ossssoo+/:-.           `/++ods/---```./+o+//:-`             `        ``       -/-.:N.
 `.:/+osm-.-+/-.`                        .:.`..-://++-`                   ``````` `o:+-          `N.
/hs/-.   `.        ```````        ``` `.o/-h`  `````````..--:::/+//++//+/////::.-..` `+          oh 
dy/-     `.-::::/+/+++++/o+//+++:://:::o`  s::://////:---..``                                   /m. 
 hs//:---.....``` `                          `      ````````````````..`..`.....`..`...````     `M.  
  d+ `.---::////o++o++++//+:://///+++++//++:/+:/++:/++////::::::/::://::/:///+/://::/::::--d:.``M   
  m/                                  `           `:.              `                       d.  `M   
  h/                /s         `                  `++             /d`            ``        y:  `N   
  os        --      ``         oo                                  `    ``       so        +o  -m   
  -m`       ++                 ``                         /s.           s+       ``        .y  :m   
   m/.`````       ````................`````````````       `.            ``                 `d  :m   
  `N+/+++///////////////::--:::::::::////+++++++ooo++++++////////////////++++++oooooooo+++/+N  /d   
  .N`                                                                                      `N  /d   
   yo...-------.....`````````````````````...`   `````  `..........................--:::::://N  /d   
   -N:-----:::::///+++++++++++++++/////////+h  .s/::y.+/::::::://///////::::::::::-----:--.`N. +d   
   /d     ``              ``               `N  :s   :/` `          .`          -`     -y.   m- +m   
   .N`   .y/       `      os         -/     +o:s/      `y:         s:         `+-           h+ /m   
    h+            /y.                .:      `--        `````....----:::////////////+++++++/hs /N   
    :m```       ```.`...--:::////++++++++++++++++++++////+///:::::----...........```        +s /N   
    yy::////////////::::--....```                                                           +s :M   
    sy                   ``````````````........................`````          `......--:::/:ss :M   
    .N+////::///+:..   +o++++/////////////::::::::::::::::::::::://////////o+s+::::----.````s+ -M   
     +m.`````````//s: /s                                             `     `-`              s/ .M`  
     .M-           /+ s:    `ss               .`          `-`        oo           `         y- `M.  
      m:      ..   /: y-     :-   -:         -os          +o:        ``          o+:        h. `M-  
      +d     `oo   // y-          oo         `-.  `       `.        `/o.         .:.        d. `M-  
      -N`          `o:y.                         .s-                .so-                    h: `N:  
       d/            --             ``````````````.````              ``                     o/  y+` 
      /hs++++++++++++++++++ooo+++o+oooooooooooo+++++++++++++++++++++++++////////:::--------/o. .++h/
      m+.```````````````````````````````````````````````````````````.........----::::::::::-...:.-oN
      ./oossssssoooooossssssssssoooooossssssssssssoooo+++oooooossssssssssssssssoooooooo+++++++++oo+-
                        `-- -....---...-.::.`.-. .....`  `....:.:-:.--.-:--`                        
                        `-- -.-:..-.--.-....-.:-.---... `..::-.----.-:.----`                        \u001b[0m""")

pic6=("""
\u001b[31;1m
                                      /:s`       /++       `/s-                                     
                                     .o s+      :/.h-     `o./y`                                    
                                    .yo.os`    :h:-y/    `+s-:y-                                    
                                    `omNd-     -smNy`     /hNN/                                     
                                    `yyso:     -hsos.     +yyoo        \u001b[0m                              
 \u001b[33;1m        
                                     /` /s      +  y-     -- .h`                                    
                                     /` oh      +  d/     .- .m.                                    
                                     /` ss      o `d:     -: -h.                                    
                                     /. ++      o  y-     ./ .h                                     
                                     /- +s      s``h:     .+ -d`                                    
                                     // oo      h+.y/`    .s -y`                                    
                                    `+/ o+     -///+hyo-  -y /s`                                    
                              ``````-y/ os://+// :/ oh/so/sy`/s-..``                                
                      ``.-:+++++/+::odo oy/+ys.  o` `y/ +dyh`:dsso++oo++/:-````                     
                 `-+/+yo/:--..      -yo ody:`  -o/   so  ohh -y`     ```..--:+hsy/`                 
              `/yhs+-odhh:          `oo`hN/   :y/    s/  .dd`+d.          :++/h/dho.`               
             .yy:.+oo+s+hy/         `:hyhhdo++hd/   :d: `ohhyyy`         `/dsm+/dod. ``             
             hy` `odhm/yhyy       `o//.`  `-:-`-oyydy+yyh+. ``      syyo`  -::ss++:   .+            
             oNh+-`.-.o/:/`    `.:+yomy:            `-ohmd/     ./+o++yhh-          `-/+            
             :Myohmdhs+:.     `+h+ys:h+y.         -oo+s/oyy/    .hshh-ysyo      .-----./            
             :M+  .-/shdhdyyo/::hhyhhhys`         .ohdd+hhho     .//+ysoy/-----.`    ://            
             :M+      ```.:++osyoo+yhyysooo+/+:.---/++shsso::://:://///-.```         -o+            
             :Md+.....--:/++o/-````...--:::::++///:/:///::--.`.```                   .so            
             :N/oooo+/o+/-.:/+so.                                                    -o/            
             +N. ````  .:::-.``:s-                                      ........    `/++            
             /m`    `:yho/-:oy/`:s`                                  .:-.``````.-...-`/o            
             :h`   :hy:`     -s+.o/`               `..-.`          `:-   `-:/-.` ```  so            
             :m. `+m+`        `+o:s-            `-//-...-:.       `/.  `oho+ooyys:    y/            
             -mo/oy-           `h//+:`        .+/-       `-:.````-:`  `yd-     ./hy.  y+            
             `+--.`             /d`-++.`  `.://.  `-:/oo/-` ..---.    od/        `od- do            
             `+                 `d/ `-/:////-`  `/o/----/yyo-`       -do           +d:hs            
           `.:o                  /y- ``.       -hs`       `/ss:```.-/d+             /dNo            
      `:+/+o+/+                   oy+y++//:-`.+o:          `-+h//://hs               :Ns```.`       
   .+yys:.   `+                   `sm:   ```-/+/`       `:--.       /h-              .m+    ```-`   
 -ydo-       `y/::--.`            `/y`          .-://:/:-`          `/y`   `..-::-/+o+m+         `` 
.h+`          y` ``..--:::::------:h+        +ssyosd:/dsdmhy:        -myoosysoo/:.`` `h/           `
hh            s`                  .N:        :odNmmh-:mydmdo-        /d`             `d+            
mm.          -s`                  `hs        .-:::sy.-o+:...`        sd`              h:          . 
/mms-        .++++:::-.`           /y-```...::osyo/m...:ydo/---.``  .y/      `..-::/+ys-        `-: 
 .sNmho:`      ``..-/osoos++oo+////:sysos+oo+s/`` .m-:o `::-:oossyshdd+/////+oo::--```      `..::-` 
   -odMNh+/:.`.`       ``..----.-:++/o++++ydh-    -myhm   -yooo////::-..```            `..--/:--`   
     `-+oosyyyso++:-.``````             `.+s.     .h./m`   `//`                ``...--::----``      
          .-:+ooyhyyhysyyhyso+/::--..````-yy:`    -h`:s      /o. ``......----:/::--::-.```          
               ``.-://oyyyssoyhhhddhyssoooyhhs:`  /h+oh      ./ho/:::::://::--..```                 
                         ```.--:-:++o++/++oo+syy: /yosd`    `ooo-......``                           
                                          ``` `/ysoy`+s`  `:so.                                     
                                                `/yy /o `/yo.                                       
                                                  `: /y/ys-                                         
                                                     :hy-                                            \u001b[0m""")
pic7=""" \u001b[34;1m                                                                             
                                                                    .`          
        `.-/o/.                                                  `:+o::.`       
        :-/:soo+-`                                             ./ooo+`::-`      
       .:.: oooooo/.                                        `-+ooooo- :.:.      
       `: ..:ooooooo+:.                                   ./oo+ooooo .. :`      
        -. `/soooo++ooo+-`                             `-/oo+/+oooo//` .-       
      `.:`--o+ooooo/:+ooo+:.                         ./+ooo/:+oooos./:-`:..`    
     :-.---/`:oooooo/-/+oo-/+-`                   `:+o/.+/-:+ooooos``/-/-.-/    
     ..-:` `.-soooooo/.-//`oooo+.              `-/ooooo.-.:+ooooooo:.` `-/..    
    `.-:.`` ./+soooooo/-..:+o+:oo+`           .oooo-/+:.`:+oooooos//-``..:--`   
    .:.  `-: `+yo+:::::-.-.-:::oooo....`````--ooooo::..-:-::::-:os+` -:`  .-.   
    .-- .:-`  `sso/+ooo-::.`-+ooooo.```    `/.sooo+/.`-/+/-oooo+s:   ..:- -:-   
     -.  `:+`  /oooooo::o/:-.-/ooo/```     :-./oo+:..:/+oo:-+oooo`   //`  .:    
     ``  `:-:  .soooo/:+oo//::+oo/.``     `::.-+oo+://+ooo+/+ooo/   -:-`  `     
           `.`  +ooooooooo+//oos/-.``     `-/.-:+soo++ooooooooos`   .`          
                .ooooooooooooso:--.``    `:/-..-:/ossoooooooooo+                
                 /oooooooosso/:--..`    `:+.`...--/++ooosoooooo`                
                 `ssssssoo+/:---...```  `:/``.....--:////oooos:                 
                  ///:::::-........````  `./```......-----:///:                 
                 .............``````    ```:``````````......--/`                
                 :...-`....````````     .:.```````````````.:.-.:                
                `:---/``..-://+//:.``  `/+/..-:::////:-.```+-:..-               
                .://+/`-+syyhhhyyyo-```.s+/-/ossyyyhyyyyo:`o+:.`:               
                ./+ss:+hhhhhhyyyysso:.-/so+-osyhyyyyhyyyyy.+:-.-`               
                `++oy:yhyyhhyyhhyys++-::o+-.+shhhyyyysssyy--/:-:                
                 ////-yyyhyhhhhhhhh++.-:o/..+ohhhhyysooyys.`+:-:                
                 :/+:-syhhhhhhhhhhyo:.-shs../+oyhhysssyhho.`+/--                
                 `ss`./yyyyyhhyysyy+.:syyyo.-:+osyyyyyhhy/-`:o+`                
                 ./.``:+ssyssyyss+-``ssyyhy+``.-:oyyyyys+:-.`:/.                
                 `/.```.-/+ossy+:.` /oyyhyhy/````./sooo++/-`` -`                
                  `--.````-//sh/-.``oohydyhso.``.//.-:/s//-``..                 
                    +:-.```-://----/s+ysdssoo:---/-` ``/+:.:/`                  
                    //+++++-`````-/+syyyyyyyy+:---.``:+o+/::.                   
                    `.:/+/ss/````.-/++osssso/:.````.+/+///-`                    
                        +/+.::```.-::/ooo+:.``` ```:` /-:.                      
                        /+o-`/.....:-://+/:..`...-:+ :/./.                      
                        :o:/:ooooo+o++o++o+o/++o++:/----:                       
                        .o:-+ss+/::+:s--/:-s:/:+://+.`.-:                       
                        .:--/oy+s:+-o++:s/oo+++/oss/...:-                       
                        :::...-:ooo+s+ysyosos+soo/-``.-:-                       
                        -+/.````.--:/ooooo+++/:.`   `.-/-                       
                         -/..`````..-:///::--.``   `.-/:                        
                          .--..`````.-::::.````   `.-:.                         
                            .--.```  `.--.`    ``.---                           
                              `..`````````````.---``                            
                                 ``.-----------.`                               
                                         ``              \u001b[0m"""  
pic8="""\u001b[33;1m
                                     ```                                        
                          ````................```                               
                      ``............................``                          
                  ``...................................``                       
                `.........................................``                    
              `..............................................`                  
            `..................................................`                
          `...............:+:..................++-..............`               
         `-..............:dmd-................ommo..............-.`             
        .-----...........smmmo...............-mmmm-...........----.`            
       .-------..........hmmmy.............../mmmN/..........-------`           
      .-----------.......dmmmh.............../Nmmm/........----------`          
     `-------------......hmmmy...............:mmmm:.....--------------          
     -----------------.-.ommm+...............-dmmd-....---------------.         
    .::-------------------hmy-................/dd+.--------------------         
    -::::------------------:--................-::------------------::::`        
   `::::::--------------------------------------------------------:::::.        
   `::::::::::-------------------------------------------------::::::::-        
   `:::::::::::::-------------------------------------------:::::::::::-        
   `//::::::::::::::::--------------------------------:::::::::::::::::-        
    :///::::::::::odd:::--------------------------::::hds:::::::::::///.        
    -/////::::::+dmm/:::::::::---------------::::::::::dmmo::::::://///`        
    `////////:::+oomh/:::::::::::::::::::::::::::::::/hmo+o::::///////:         
     ://////////:/:+ddo/:::::::::::::::::::::::::::/ymh/:::///////////`         
     `///////////////ohdyo/::::::::::::::::::::/+shdy+///////////////.          
      ./++/////////////+shddhsoo++///////++osyhdhyo///////////////++-           
       ./++++//////////////+osyhhhhhhhhhhhhyys++///////////////++++:            
        `/++++++++/////////////////+++++//////////////////++++++++-             
         `:+++++++++++++///////////////////////////++++++++++++o+.              
           .+oooo++++++++++++++++++++++++++++++++++++++++++ooo+:`               
            `-+oooooooo++++++++++++++++++++++++++++++oooooooo/.                 
              `-+ooooooooooooooooooooooooooooooooooooooooo+:.                   
                 ./+osoooooooooooooooooooooooooooooooooo+-`                     
                   `.:+ossssssssssooooooooossssssssoo+:.`                       
                     ``.-/+oossssssssssssssssssoo+/:-..````                     
                    ````...--://++oooosssoooo++/::---..````                     
                      ````...---::://////////:::---...````                      
                        `````.....-----------.....``````                        
                              ````````````````````                    \u001b[0m"""         
#

# 
#
# Riddles for ingredients, mixing, cooking lists:
#
ingredients_choice_riddles = ["White and fine this you’ll find is what you need", "They keep to the beat, going around and around", "Slippery and soft I’ll run with heat", "Shrivelled and soft I was picked from aloft", "I’ll turn you around and make you sit down","We go together and hold the rest together too"]
mixings_choice_riddles = ["I’ll mix them well and they’ll come clean", "Use me and use me again, for an extra taste you’ll remember", "I’m round and sound and whip them all together", "I let you look yet could cause a smash when carelessly handling that mixed up hash"]
cooking_choice_riddles = ["Boring I am but you’re in for a treat if you put me on heat", "You’ll need to rehearse to use me at last", "I’ll cook your food but you’ll need to react when your food begins to glow", "Use me and I’ll go around and around with most of your mix lying on the ground"]
#
step_names = ["Ingredients", "Mixing", "Cooking"]
#
step_index = 0
#
user_pick = [0]
#
user_choices = [0,0,0]
#
correct_choices=["A", "1", "W"]
#
user_name = " "
#
user_play = " "
#
#
# functions:
#
def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
#
def typing_input(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value  
#
def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
#
def titlescreen():
    
    print("""
    \u001b[31;1m
                                                             _____   
           _____       _____         ______   _______    _____\    \  
       _____\    \_   /      |_      |\     \  \      \  /    / |    | 
    \u001b[32;1m  /     /|     | /         \      \\     \  |     /|/    /  /___/| 
     /     / /____/||     /\    \      \|     |/     //|    |__ |___|/ 
    |     | |____|/ |    |  |    \      |     |_____// |       \       
    \u001b[33;1m|     |  _____  |     \/      \     |     |\     \ |     __/ __    
    |\     \|\    \ |\      /\     \   /     /|\|     ||\    \  /  \   
    | \_____\|    | | \_____\ \_____\ /_____/ |/_____/|| \____\/    |  
    \u001b[34;1m| |     /____/| | |     | |     ||     | / |    | || |    |____/|  
     \|_____|    ||  \|_____|\|_____||_____|/  |____|/  \|____|   | |  
            |____|/                                           |___|/   
    
    \u001b[35;1m
​
                             _____                                     
                           /      |_                                   
                          /         \                                  
    \u001b[36;1m                    |     /\    \                                 
                         |    |  |    \                                
                         |     \/      \                               
    \u001b[31;1m                     |\      /\     \                              
                         | \_____\ \_____\                             
                         | |     | |     |                             
    \u001b[32;1m                      \|_____|\|_____|                                                                                 
    
    
                                                                _____
    ______  ______      _____         ______   _______    _____\    \  
    \u001b[33;1m\     \|\     \   /      |_      |\     \  \      \  /    / |    | 
     |     |\|     | /         \      \\     \  |     /|/    /  /___/| 
     |     |/____ / |     /\    \      \|     |/     //|    |__ |___|/ 
    \u001b[34;1m |     |\     \ |    |  |    \      |     |_____// |       \       
     |     | |     ||     \/      \     |     |\     \ |     __/ __    
     |     | |     ||\      /\     \   /     /|\|     ||\    \  /  \   
    \u001b[35;1m/_____/|/_____/|| \_____\ \_____\ /_____/ |/_____/|| \____\/    |  
    |    |||     | || |     | |     ||     | / |    | || |    |____/|  
    |____|/|_____|/  \|_____|\|_____||_____|/  |____|/  \|____|   | |  
                                                              |___|/   
    \u001b[0m                                                """)

def screen_choice_display():
    global ingredients_choice_riddles, step_names, step_index, mixings_choice_riddles, cooking_choice_riddles
    step_index == 0
    if step_index == 0:
        print("Solve these riddles and choose your step wisely! \n")
        print("First off: {} \n A for: {} \n B for: {} \n C for: {} \n D for: {} \n E for: {} \n F for: {} ".format(step_names[0], ingredients_choice_riddles[0], ingredients_choice_riddles[1], ingredients_choice_riddles[2], ingredients_choice_riddles[3], ingredients_choice_riddles[4],ingredients_choice_riddles[5]))
        user_input()
    if step_index == 1:
        print("Now for... {} \n 1 for: {} \n 2 for: {} \n 3 for: {} \n 4 for: {}".format(step_names[1], mixings_choice_riddles[0], mixings_choice_riddles[1], mixings_choice_riddles[2], mixings_choice_riddles[3]))
        user_input()
    if step_index == 2:
        print("And finally: {} \n W for: {} \n X for: {} \n Y for: {} \n Z for: {} ".format(step_names[2], cooking_choice_riddles[0], cooking_choice_riddles[1], cooking_choice_riddles[2], cooking_choice_riddles[3]))
        user_input()
    else:
        print("")

def user_input():
    global user_pick, user_choices, step_names, step_index

    if step_index == 0:
        print("\nPlease make your choice of {} ".format(step_names[0]))
        user_pick = input()
        user_pick = user_pick.upper()
        user_choices[0] = user_pick
        if user_pick == "A" or user_pick=="B" or user_pick=="C" or user_pick=="D" or user_pick=="E" or user_pick=="F": 
            step_index += 1 
            screen_choice_display()
        else:
            typing_print("\nWrong input. Please make your choice of {} ".format(step_names[0]))
            screen_choice_display()
        
    if step_index == 1:
        print("\nPlease make your choice of {} ".format(step_names[1]))
        user_pick = input()
        user_choices[1] = user_pick
        if user_pick == "1" or user_pick=="2" or user_pick=="3" or user_pick=="4": 
            step_index += 1 
            screen_choice_display()
        else:
            typing_print("\nWrong input. Please make your choice of {} ".format(step_names[1]))
            screen_choice_display()

    if step_index == 2:
        print("\nPlease make your choice of {} ".format(step_names[2]))
        user_pick = input()
        user_pick = user_pick.upper()
        user_choices[2] = user_pick
        if user_pick == "W" or user_pick=="X" or user_pick=="Y" or user_pick=="Z": 
            step_index += 1 
            screen_choice_display()
        else:
            typing_print("\nWrong input. Please make your choice of {} ".format(step_names[2]))
            screen_choice_display()

def orange(): #functions for giving to friend
    clear_screen()
    global user_choices, correct_choices
    give_cake=typing_print("Do you want to test this cake on your friend? Y/N ") 
    give_cake=input().upper()
    if give_cake=="Y":
        if user_choices==correct_choices:
            typing_print(random.choice(friend_good))
            print(pic8)
        if user_choices!=correct_choices:
            typing_print(random.choice(friend_bad))
            print(pic7)
    elif give_cake=="N":
        typing_print("He he he, as you wish!!!")
    else: 
        typing_print("Please choose Y/N \n")
        orange()
    time.sleep(3)
    clear_screen()
#
friend_good= ["Great Idea, your friend is very happy!", "Friend's opinion: That was the best cake in my life! <3"]
friend_bad=["Noooo, the cake was bad!!! You've killed your friend!", "Boooo! Your friend turned into a zombie"]
# 
pic_list_good=[pic2,pic5,pic6]
pic_list_bad=[pic4,pic3,pic1]
# 
titlescreen()
time.sleep(3)
clear_screen()
typing_print("Hello and welcome to \u001b[31;1mC\u001b[32;1mA\u001b[33;1mK\u001b[34;1mE\u001b[35;1m\u001b[1m-\u001b[36;1mA\u001b[35;1m\u001b[1m-\u001b[31;1mB\u001b[32;1mA\u001b[33;1mK\u001b[34;1mE\u001b[0m! \n")
time.sleep(1)
typing_print("May I know your name?\n")
user_name=input()
typing_print(f"It is lovely to have you on the show, {user_name}! \n")
typing_print("Would you like to play? Y/N ")
user_play =input().upper()
while not user_play=="Y" and not user_play=="N":
    typing_print("Could you repeat that? ")
    user_play=input().upper()
if user_play =="Y":
    typing_print("Let me give you a brief explanation of the show. \n")
    time.sleep(1)
    typing_print("Your goal is to bake a nice cake. ")
    time.sleep(1)
    typing_print("You will be presented with different ingredients, mixing methods, and cooking methods. \n")
    time.sleep(1)
    typing_print("You will have to find the right combination BUT ")
    time.sleep(1)
    typing_print("your options are presented in riddles! \n")
    time.sleep(1)
    typing_print("Sounds good? ")
    time.sleep(1)
    typing_print("Let's get started!\n")
    time.sleep(1)
else:
    typing_print(f"\nNo hard feelings, {user_name}, have a lovely day!")
    print(pic0)
    exit()
screen_choice_display() # calling the screen_choice_display
orange()
good_msgs = [ f"Your cake smells lovely {user_name}! Well done! ", 
f"So delightful! Thank you {user_name}, that is a delicious cake! ", 
"What a lovely smell! I'm sure this cake will taste amazing! ", 
"This cake is truly like a little slice of heaven! ",
"This might be the best cake I've ever had! ",
"You know what they say! A balanced diet is a cookie in each hand! ",
"Incredible! The flavour. The presentation. Simply delicious! ",
"This cake is better than my grandma's! ",
"This cake is making me drooling! Let's dig in! ",
"9 out of 10 people loves cake. And the 10th person is always lying! "]
bad_msgs = [ f"What have you done {user_name}? You've created a monster!!! ",
"Now that didn't go as planned. Your cake turned into a monster! ",
"Talk about unintended consequences! Your cake is now attacking the audience! ",
"What is that creature? It's a monster! Run for your lives!!! ",
"Wait. That's not a cake. That's a monster!! ",
"That went terribly wrong! The cake is a monster! ",
"What's that? A cake moster? What a bummer! ",
"Oh no! That's disappointing. You didn't bake a cake, you baked a monster! ",
"What is that growling? It's coming from the kitchen. Oh no, it's a monster! RUN!!! ",
f"{user_name} are you sure you put a cake in the oven? It doesn't look like it. It reminds me more of a monster! "]
if user_choices == correct_choices:
    typing_print(random.choice(good_msgs))
    print(random.choice(pic_list_good))
else:
    typing_print(random.choice(bad_msgs))
    print(random.choice(pic_list_bad))


