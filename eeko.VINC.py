import base64; import zlib; _0x1 = '==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'; exec(zlib.decompress(base64.b64decode(_0x1[::-1])))
