package app;

public class SessionCipher {
    public byte[] seal(byte[] plain) throws Exception {
        // BUG: weak_cipher — DES is the algorithm named at the factory call
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("DES/ECB/PKCS5Padding");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, new javax.crypto.spec.SecretKeySpec(KEY, "DES"));
        return cipher.doFinal(plain);
    }

    private static final byte[] KEY = "k8bytes!".getBytes(java.nio.charset.StandardCharsets.US_ASCII);
}
