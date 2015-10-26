on run argv
  tell application "App Store" to activate

  tell application "System Events" to tell process "App Store"
    set frontmost to true
    -- Logout before executing a new login
    if name of menu item 12 of menu "Store" of menu bar 1 is not equal to "Sign Out" then
      click menu item 12 of menu "Store" of menu bar 1
      delay 1
      -- Type account email
      keystroke item 1 of argv
      keystroke tab
      delay 1
      -- Type account password
      keystroke item 2 of argv
      -- Press the return key
      keystroke return
      delay 3
      keystroke return
    end if
  end tell

  tell application "App Store" to quit
end run
