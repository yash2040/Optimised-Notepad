# Results of test files

1. For very random 1MB test file, it was able to compress to 566KB.
   Compression Ratio: 43.4%.
2. For 2MB test file, containing latin text, it was able to compress to 471KB.
   Compression Ratio: 76.4%.
3. For 516KB of a test file (it was a log file of on of the project having some repeated text), it was able to
   compess to 113KB.
   Compression Ratio: 78.1%.

# Analysis

For commonly use files, containing relevant information the editor can achieve compression of about 70% to 75%.
For random content with no proper meaning, it can achieve compression of about 40% to 50%.