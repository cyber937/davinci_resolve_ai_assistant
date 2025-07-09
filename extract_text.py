from pdfminer.high_level import extract_text

# 読み込むPDFファイル名
pdf_path = "DaVinci_Resolve_20_Reference_Manual.pdf"

# テキストを抽出
print("Extracting text from PDF...")
text = extract_text(pdf_path)

# テキストファイルに保存
output_path = "resolve_manual.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Text extraction complete. Saved to {output_path}")