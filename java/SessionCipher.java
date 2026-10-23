package app;

public class SessionCipher {
    public byte[] seal(byte[] plain) throws Exception {
        // BUG: weak_cipher — DES is the algorithm named at the factory call
        return javax.crypto.Cipher.getInstance("DES/ECB/PKCS5Padding").doFinal(plain);
    }
}
