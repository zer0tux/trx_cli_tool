# trx_cli_tool
Tool for pack\unpack trx firmware ASUS or etc

The `extract_trx` function extracts the firmware from the trx file and writes it to the `image.bin` file, and outputs the firmware header information to the `header.txt` file in the specified folder.

The `pack_trx` function packs the firmware from the specified `input_dir` folder with the `image.bin` file into trx format and writes it to the specified `output_file` file. Both of these functions can be used to work with ASUS router firmware.
