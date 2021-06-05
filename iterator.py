import os, re
from main import regex_search
if __name__ == '__main__':

    path = "Directory"
    txt_file = [f for f in os.listdir(path) if f.endswith('.txt')]
    REGEXES = [(re.compile(r'[⒜ⓐ𝐚𝒂𝓪𝕒𝖆𝖺𝗮𝘢𝙖𝚊ａᵃₐ𝑎𝒶𝔞]'), 'a'),
               (re.compile(r'[⒝ⓑ𝐛𝒃𝓫𝕓𝖇𝖻𝗯𝘣𝙗𝚋ｂᵇ𝑏𝒷𝔟]'), 'b'),
               (re.compile(r'[⒞ⓒ𝐜𝒄𝓬𝕔𝖈𝖼𝗰𝘤𝙘𝚌ｃᶜ𝑐𝒸𝔠]'), 'c'),
               (re.compile(r'[⒟ⓓ𝐝𝒅𝓭𝕕𝖉𝖽𝗱𝘥𝙙𝚍ｄᵈ𝑑𝒹𝔡]'), 'd'),
               (re.compile(r'[⒠ⓔ𝐞𝒆𝓮𝕖𝖊𝖾𝗲𝘦𝙚𝚎ｅᵉₑℯ𝑒𝔢]'), 'e'),
               (re.compile(r'[⒡ⓕ𝐟𝒇𝓯𝕗𝖋𝖿𝗳𝘧𝙛𝚏ｆᶠ𝑓𝒻𝔣]'), 'f'),
               (re.compile(r'[⒢ⓖ𝐠𝒈𝓰𝕘𝖌𝗀𝗴𝘨𝙜𝚐ｇᵍℊ𝑔𝔤]'), 'g'),
               (re.compile(r'[⒣ⓗ𝐡𝒉𝓱𝕙𝖍𝗁𝗵𝘩𝙝𝚑ｈʰₕℎ𝒽𝔥]'), 'h'),
               (re.compile(r'[⒤ⓘ𝐢𝒊𝓲𝕚𝖎𝗂𝗶𝘪𝙞𝚒ｉᶦᵢ𝑖𝒾𝔦]'), 'i'),
               (re.compile(r'[⒥ⓙ𝐣𝒋𝓳𝕛𝖏𝗃𝗷𝘫𝙟𝚓ｊʲⱼ𝑗𝒿𝔧]'), 'j'),
               (re.compile(r'[⒦ⓚ𝐤𝒌𝓴𝕜𝖐𝗄𝗸𝘬𝙠𝚔ｋᵏₖ𝑘𝓀𝔨]'), 'k'),
               (re.compile(r'[⒧ⓛ𝐥𝒍𝓵𝕝𝖑𝗅𝗹𝘭𝙡𝚕ｌˡₗ𝑙𝓁𝔩]'), 'l'),
               (re.compile(r'[⒨ⓜ𝐦𝒎𝓶𝕞𝖒𝗆𝗺𝘮𝙢𝚖ｍᵐₘ𝑚𝓂𝔪]'), 'm'),
               (re.compile(r'[⒩ⓝ𝐧𝒏𝓷𝕟𝖓𝗇𝗻𝘯𝙣𝚗ｎⁿₙ𝑛𝓃𝔫]'), 'n'),
               (re.compile(r'[⒪ⓞ𝐨𝒐𝓸𝕠𝖔𝗈𝗼𝘰𝙤𝚘ｏᵒₒℴ𝑜𝔬]'), 'o'),
               (re.compile(r'[⒫ⓟ𝐩𝒑𝓹𝕡𝖕𝗉𝗽𝘱𝙥𝚙ｐᵖₚ𝑝𝓅𝔭]'), 'p'),
               (re.compile(r'[⒬ⓠ𝐪𝒒𝓺𝕢𝖖𝗊𝗾𝘲𝙦𝚚ｑ𝑞𝓆𝔮]'), 'q'),
               (re.compile(r'[⒭ⓡ𝐫𝒓𝓻𝕣𝖗𝗋𝗿𝘳𝙧𝚛ｒʳᵣ𝑟𝓇𝔯]'), 'r'),
               (re.compile(r'[⒮ⓢ𝐬𝒔𝓼𝕤𝖘𝗌𝘀𝘴𝙨𝚜ｓˢₛ𝑠𝓈𝔰]'), 's'),
               (re.compile(r'[⒯ⓣ𝐭𝒕𝓽𝕥𝖙𝗍𝘁𝘵𝙩𝚝ｔᵗₜ𝑡𝓉𝔱]'), 't'),
               (re.compile(r'[⒰ⓤ𝐮𝒖𝓾𝕦𝖚𝗎𝘂𝘶𝙪𝚞ｕᵘᵤ𝑢𝓊𝔲]'), 'u'),
               (re.compile(r'[⒱ⓥ𝐯𝒗𝓿𝕧𝖛𝗏𝘃𝘷𝙫𝚟ｖᵛᵥ𝑣𝓋𝔳]'), 'v'),
               (re.compile(r'[⒲ⓦ𝐰𝒘𝔀𝕨𝖜𝗐𝘄𝘸𝙬𝚠ｗʷ𝑤𝓌𝔴]'), 'w'),
               (re.compile(r'[⒳ⓧ𝐱𝒙𝔁𝕩𝖝𝗑𝘅𝘹𝙭𝚡ｘˣₓ𝑥𝓍𝔵]'), 'x'),
               (re.compile(r'[⒴ⓨ𝐲𝒚𝔂𝕪𝖞𝗒𝘆𝘺𝙮𝚢ｙʸ𝑦𝓎𝔶]'), 'y'),
               (re.compile(r'[⒵ⓩ𝐳𝒛𝔃𝕫𝖟𝗓𝘇𝘻𝙯𝚣ｚᶻ𝑧𝓏𝔷]'), 'z'),
               (re.compile(r'[🄐Ⓐ𝐀𝑨𝓐𝔸𝕬𝖠𝗔𝘈𝘼𝙰🄰🅐🅰Ａᴀᴬ𝐴𝒜𝔄]'), 'A'),
               (re.compile(r'[🄑Ⓑ𝐁𝑩𝓑𝔹𝕭𝖡𝗕𝘉𝘽𝙱🄱🅑🅱Ｂʙᴮℬ𝐵𝔅]'), 'B'),
               (re.compile(r'[🄒Ⓒ𝐂𝑪𝓒ℂ𝕮𝖢𝗖𝘊𝘾𝙲🄲🅒🅲Ｃᴄℭ𝐶𝒞]'), 'C'),
               (re.compile(r'[🄓Ⓓ𝐃𝑫𝓓𝔻𝕯𝖣𝗗𝘋𝘿𝙳🄳🅓🅳Ｄᴅᴰ𝐷𝒟𝔇]'), 'D'),
               (re.compile(r'[🄔Ⓔ𝐄𝑬𝓔𝔼𝕰𝖤𝗘𝘌𝙀𝙴🄴🅔🅴Ｅᴇᴱℰ𝐸𝔈]'), 'E'),
               (re.compile(r'[🄕Ⓕ𝐅𝑭𝓕𝔽𝕱𝖥𝗙𝘍𝙁𝙵🄵🅕🅵Ｆꜰℱ𝐹𝔉]'), 'F'),
               (re.compile(r'[🄖Ⓖ𝐆𝑮𝓖𝔾𝕲𝖦𝗚𝘎𝙂𝙶🄶🅖🅶Ｇɢᴳ𝐺𝒢𝔊]'), 'G'),
               (re.compile(r'[🄗Ⓗ𝐇𝑯𝓗ℍ𝕳𝖧𝗛𝘏𝙃𝙷🄷🅗🅷Ｈʜᴴℋℌ𝐻]'), 'H'),
               (re.compile(r'[🄘Ⓘ𝐈𝑰𝓘𝕀𝕴𝖨𝗜𝘐𝙄𝙸🄸🅘🅸Ｉɪᴵℐℑ𝐼]'), 'I'),
               (re.compile(r'[🄙Ⓙ𝐉𝑱𝓙𝕁𝕵𝖩𝗝𝘑𝙅𝙹🄹🅙🅹Ｊᴊᴶ𝐽𝒥𝔍]'), 'J'),
               (re.compile(r'[🄚Ⓚ𝐊𝑲𝓚𝕂𝕶𝖪𝗞𝘒𝙆𝙺🄺🅚🅺Ｋᴋᴷ𝐾𝒦𝔎]'), 'K'),
               (re.compile(r'[🄛Ⓛ𝐋𝑳𝓛𝕃𝕷𝖫𝗟𝘓𝙇𝙻🄻🅛🅻Ｌʟᴸℒ𝐿𝔏]'), 'L'),
               (re.compile(r'[🄜Ⓜ𝐌𝑴𝓜𝕄𝕸𝖬𝗠𝘔𝙈𝙼🄼🅜🅼Ｍᴍᴹℳ𝑀𝔐]'), 'M'),
               (re.compile(r'[🄝Ⓝ𝐍𝑵𝓝ℕ𝕹𝖭𝗡𝘕𝙉𝙽🄽🅝🅽Ｎɴᴺ𝑁𝒩𝔑]'), 'N'),
               (re.compile(r'[🄞Ⓞ𝐎𝑶𝓞𝕆𝕺𝖮𝗢𝘖𝙊𝙾🄾🅞🅾Ｏᴏᴼ𝑂𝒪𝔒]'), 'O'),
               (re.compile(r'[🄟Ⓟ𝐏𝑷𝓟ℙ𝕻𝖯𝗣𝘗𝙋𝙿🄿🅟🅿Ｐᴘᴾ𝑃𝒫𝔓]'), 'P'),
               (re.compile(r'[🄠Ⓠ𝐐𝑸𝓠ℚ𝕼𝖰𝗤𝘘𝙌𝚀🅀🅠🆀Ｑ𝑄𝒬𝔔]'), 'Q'),
               (re.compile(r'[🄡Ⓡ𝐑𝑹𝓡ℝ𝕽𝖱𝗥𝘙𝙍𝚁🅁🅡🆁Ｒʀᴿℛℜ𝑅]'), 'R'),
               (re.compile(r'[🄢Ⓢ𝐒𝑺𝓢𝕊𝕾𝖲𝗦𝘚𝙎𝚂🅂🅢🆂Ｓ𝑆𝒮𝔖]'), 'S'),
               (re.compile(r'[🄣Ⓣ𝐓𝑻𝓣𝕋𝕿𝖳𝗧𝘛𝙏𝚃🅃🅣🆃Ｔᴛᵀ𝑇𝒯𝔗]'), 'T'),
               (re.compile(r'[🄤Ⓤ𝐔𝑼𝓤𝕌𝖀𝖴𝗨𝘜𝙐𝚄🅄🅤🆄Ｕᴜᵁ𝑈𝒰𝔘]'), 'U'),
               (re.compile(r'[🄥Ⓥ𝐕𝑽𝓥𝕍𝖁𝖵𝗩𝘝𝙑𝚅🅅🅥🆅Ｖᴠⱽ𝑉𝒱𝔙]'), 'V'),
               (re.compile(r'[🄦Ⓦ𝐖𝑾𝓦𝕎𝖂𝖶𝗪𝘞𝙒𝚆🅆🅦🆆Ｗᴡ𝑊𝒲𝔚]'), 'W'),
               (re.compile(r'[🄧Ⓧ𝐗𝑿𝓧𝕏𝖃𝖷𝗫𝘟𝙓𝚇🅇🅧🆇Ｘ𝑋𝒳𝔛]'), 'X'),
               (re.compile(r'[🄨Ⓨ𝐘𝒀𝓨𝕐𝖄𝖸𝗬𝘠𝙔𝚈🅈🅨🆈Ｙʏ𝑌𝒴𝔜]'), 'Y'),
               (re.compile(r'[🄩Ⓩ𝐙𝒁𝓩ℤ𝖅𝖹𝗭𝘡𝙕𝚉🅉🅩🆉Ｚℨ𝑍𝒵ᴢ]'), 'Z')]
    for i in range(len(txt_file)):
        regex_search(os.path.join(path, txt_file[i]), os.path.join(path, 'temp.txt'), REGEXES)
        os.remove(os.path.join(path, txt_file[i]))
        os.rename(os.path.join(path, 'temp.txt'), os.path.join(path, txt_file[i]))

