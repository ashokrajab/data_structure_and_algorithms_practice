class Codec:
    def __init__(self):
        self.encodeMap ={}
        self.decodeMap ={}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap:
            h = str(len(self.encodeMap) +1)
            self.encodeMap[longUrl] = h
            self.decodeMap[h] = longUrl
            return h
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))