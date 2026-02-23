from splitter import split_text

text = """And this heat, this energy, it's always on,
it's clean, and it actually holds our whole world together."""

chunks = split_text(text)

for i, chunk in enumerate(chunks, 1):
    print(f"[{i}] {chunk}")

