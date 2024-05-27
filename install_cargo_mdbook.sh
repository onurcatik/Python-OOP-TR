#!/bin/bash

command_exists() {
    command -v "$1" &> /dev/null
}

if ! command_exists brew; then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

if ! command_exists rustc; then
    echo "Rust not found. Installing Rust..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source $HOME/.cargo/env
else
    echo "Rust is already installed."
fi

echo "Updating Cargo..."
cargo install-update -a

if ! command_exists mdbook; then
    echo "mdBook not found. Installing mdBook..."
    cargo install mdbook
else
    echo "mdBook is already installed."
fi

echo "Installation complete."
