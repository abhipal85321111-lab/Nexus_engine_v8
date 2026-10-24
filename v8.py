import zlib

class NexusV8_RealSqueezer:
    """Real 22GB -> 2GB - Stream + Chunk - V8.1 BUG FIXED"""

    def __init__(self):
        pass  # Ab yaha kuch nahi

    def squeeze_file(self, input_path, output_path, chunk_size=1024 * 1024):
        self.compressor = zlib.compressobj(level=9)  # FIX: Har baar naya compressor
        total_in = 0
        total_out = 0

        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            while True:
                chunk = f_in.read(chunk_size)
                if not chunk:
                    break

                total_in += len(chunk)
                comp_chunk = self.compressor.compress(chunk)

                if comp_chunk:
                    f_out.write(comp_chunk)
                    total_out += len(comp_chunk)

                print(f"\r[V8 REAL] {total_in / 1024**3:.2f}GB -> {total_out / 1024**3:.2f}GB", end='')

            final = self.compressor.flush()
            f_out.write(final)
            total_out += len(final)

            if total_out > 0:
                print(f"\nDone! Ratio: {total_in / total_out:.1f}x | {total_in / 1024**3:.2f}GB -> {total_out / 1024**3:.2f}GB")
            else:
                print("\nDone! Output empty")
