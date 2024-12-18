import re
adress="saiidie12   )klnl)- "

print(bool(re.match(r"^[A-ZA-z0-9\s\-,()]{3,50}$", adress)))

