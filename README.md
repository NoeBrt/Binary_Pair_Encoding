# Binary Pair Encoding : Corpus Vocabulary Trainer and Segmenter

A Python CLI tool to train a vocabulary model and segment text based on learned patterns using Byte Pair Encoding (BPE).

## Features

- Trains a vocabulary model using a corpus.
- Segments new text using the trained vocabulary.
- Configurable number of training iterations.
- Supports input from both direct text and `.txt` files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/vocabulary-trainer.git
   cd vocabulary-trainer
   ```
2. Install required dependencies:
   ```bash
   pip install numpy tqdm
   ```

## Usage

### Training the Model

To train the model, provide the input text directly or as a path to a `.txt` file:

```bash
# Direct text
python bpe.py "low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new" --iterations 10

# Text from a .txt file
python bpe.py "path/to/your/file.txt" --iterations 10
```

The vocabulary will be displayed after training.

### Segmenting Text

To segment a new text after training, provide the text directly or as a path to a `.txt` file:

```bash
# Direct text
python bpe.py "low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new" --segment "the new low is newer but lowest"

# Text from a .txt file
python bpe.py "path/to/your/file.txt" --segment "path/to/your/segment_file.txt"
```

### Example Output

#### Training
```plaintext
------------ Start Training -----------
Training: 100%|████████████████████████| 10/10 [00:00<00:00, 100.00it/s]
------------ End of Training -----------
Vocabulary:
['_' 'l' 'o' 'w' ... 'lo' 'ow' 'we']
```

#### Segmenting
```plaintext
Segmented Text:
[['th', 'e'], ['new'], ['lo', 'w'], ['is'], ['new', 'er'], ['but'], ['lo', 'we', 'st']]
```

## Arguments

- `text`: The input text for training, or the path to a `.txt` file.
- `--segment`: Text to segment using the trained vocabulary, or the path to a `.txt` file containing the text to segment.
- `--iterations`: (Optional) Number of training iterations. Default is 10.

## License

This project is licensed under the MIT License.
```

This version reflects the correct script name (`bpe.py`) and describes how to use it for both training and segmenting text with the option to input direct text or `.txt` files.
