// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00105 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    static final class FormData {
        private final String payload;
        FormData(String payload) { this.payload = payload; }
        String getPayload() { return payload; }
    }

    @GetMapping("/BenchmarkTest00105")
    public void BenchmarkTest00105(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        FormData payload = new FormData(uaValue);
        String data = payload.getPayload();
        byte[] dataKey = java.util.Base64.getDecoder().decode(System.getenv("DATA_ENC_KEY"));
        org.bouncycastle.crypto.paddings.PaddedBufferedBlockCipher blockMode = new org.bouncycastle.crypto.paddings.PaddedBufferedBlockCipher(org.bouncycastle.crypto.engines.AESEngine.newInstance());
        blockMode.init(true, new org.bouncycastle.crypto.params.KeyParameter(dataKey));
        byte[] plain = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] sealed = new byte[blockMode.getOutputSize(plain.length)];
        int sealedLen = blockMode.processBytes(plain, 0, plain.length, sealed, 0);
        sealedLen += blockMode.doFinal(sealed, sealedLen);
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(java.util.Arrays.copyOf(sealed, sealedLen)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
