# VL64 Encoder/Decoder

This script provides a utility for encoding and decoding VL64.

## Usage

### Encoding
To encode into VL64, use the `--encode` flag:

```bash
python main.py --encode <value_to_encode>
```

#### Example

```bash
python3 main.py --encode 17
Encoded: QD
```

### Decoding
To decode from VL64 into plain text, use the `--decode` flag:

```bash
python main.py --decode <value_to_decode>
```

#### Example

```bash
python3 main.py --decode QD
QD = 17
```