# VHS Tape - AWS Credentials Clipboard Updater Demo
# https://github.com/charmbracelet/vhs

Output docs/demo.gif

Set Shell "zsh"
Set FontSize 16
Set Width 800
Set Height 500
Set Theme "Catppuccin Mocha"
Set Padding 20

# Title
Type "# AWS Credentials Clipboard Updater Demo"
Enter
Sleep 1s

# Show help
Type "awscreds --help"
Enter
Sleep 2s

# Clear and show update command
Type "clear"
Enter
Sleep 500ms

Type "# Update profile from clipboard"
Enter
Sleep 500ms

Type "awscreds update --profile dev"
Enter
Sleep 2s

# Show list command
Type "# List all profiles"
Enter
Sleep 500ms

Type "awscreds list"
Enter
Sleep 2s

# Show delete command
Type "# Delete a profile"
Enter
Sleep 500ms

Type "awscreds delete --profile old-profile"
Enter
Sleep 2s

# End
Type "# Done! Simple AWS credential management"
Enter
Sleep 2s
