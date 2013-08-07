import default
import ass
import os
import os.path
apps = [("Back", default.MenuProxy("mainMenu"))]
for i in os.listdir("../apps"):
  apps.append((i, default.LaunchMenu(default.MenuProxy("mainMenu"), os.path.join("..","apps", i, "launch"), os.path.join("..", "apps", i, "launch.rb"))))
mainMenu = default.ChoiceMenu(default.ExitMenu(), [
  ("Exit", default.ExitMenu()),
  ("Applications", False, apps),
  ("Accounts", default.MenuProxy("accountsMenu"))
  ])
accountsMenu = ass.AccountsMenu(mainMenu)