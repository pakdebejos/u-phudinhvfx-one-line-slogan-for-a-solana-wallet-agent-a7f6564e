"""One Wallet, One Agent, Zero Missed Moves: an entry for the make.fun bounty "One-Line Slogan for a Solana Wallet Agent".

The program writes the entry text - one line, 107 characters -
to entry.txt (107 characters, inside the 1-140 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "One wallet, one agent, zero missed moves, your Solana sidekick that watches the chain so you don't have to."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
