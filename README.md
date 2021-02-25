# mrc_insar_common
InSAR common util functions

```bash
pip install MRC-InSAR-Common
```

## Usage

```python
def test_read_write_float():
    dummy_float = np.random.normal(size=[500,500]).astype('>f4')
    data_reader.writeBin(fileName='/tmp/dummy.bin', data=dummy_float, dataType='float')

    dummy_float_read_crop = data_reader.readBin(fileName='/tmp/dummy.bin', width=500, dataType='float', crop=[50,50,100,100])

    assert np.array_equal(dummy_float[50:50+100, 50:50+100], dummy_float_read_crop)



def test_read_write_floatComplex():
    dummy_float = np.random.normal(size=[500,500]).astype('>c8')
    data_reader.writeBin(fileName='/tmp/dummy.bin', data=dummy_float, dataType='floatComplex')

    dummy_float_read_crop = data_reader.readBin(fileName='/tmp/dummy.bin', width=500, dataType='floatComplex', crop=[50,50,100,100])

    assert np.array_equal(dummy_float[50:50+100, 50:50+100], dummy_float_read_crop)



def test_read_write_shortComplex():
    dummy_float = np.random.normal(size=[500,500]).astype(np.complex).view(np.float).astype('>i2').astype(np.float).view(np.complex).reshape(500,500)
    data_reader.writeBin(fileName='/tmp/dummy.bin', data=dummy_float, dataType='shortComplex')

    dummy_float_read_crop = data_reader.readBin(fileName='/tmp/dummy.bin', width=500, dataType='shortComplex', crop=[50,50,100,100])

    assert np.array_equal(dummy_float[50:50+100, 50:50+100], dummy_float_read_crop)

```

## Test
```bash
python -m pytest
```

