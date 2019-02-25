# Ceaser Cipher
    
    - Caser used to encrypt a maeeage usign a very simple algorithm, which could be easily decrypt if you know the key.
    - He take each latter of the alphabet and replace it with a letter a certain distance away  from the latter. When
    he got to the end, He would warp back around to the begining.

## Ceaser Cipher Decoding
    
    - To decode we have to following
        `(cipher letter index - key + total number of letters) mod (total number of letters)`
        `(cipher letter index - key) mod (total number of letters)`
