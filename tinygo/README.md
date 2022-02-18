brew tap tinygo-org/tools
brew install tinygo
tinygo version

brew tap tasanakorn/homebrew-esp32
brew install xtensa-esp32-elf

cd ~/Downloads/basicblinky.zip\ Contents

# must include target or tries to compile for host -> undefined symbols
# must be in right spot in cmdline
tinygo build -o main -target esp32c3 ./main.go

# reset to boot mode
# kill Arduino IDE so port is free
tinygo flash -target esp32c3

# restart board


looks like no wifi support yet https://github.com/tinygo-org/tinygo/pull/2138


lots of doc issues for tinygo
