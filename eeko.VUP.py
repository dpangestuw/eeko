import base64; import zlib; _0x1 = '=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'; exec(zlib.decompress(base64.b64decode(_0x1[::-1])))
