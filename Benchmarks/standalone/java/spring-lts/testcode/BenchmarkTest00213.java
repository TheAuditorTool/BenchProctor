// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00213 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00213", consumes="multipart/form-data")
    public void BenchmarkTest00213(@jakarta.validation.constraints.Size(max = 4096) @RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(multipartValue.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        byte[] dataKey = java.util.Base64.getDecoder().decode(System.getenv("DATA_ENC_KEY"));
        byte[] gcmNonce = new byte[12]; new java.security.SecureRandom().nextBytes(gcmNonce);
        org.bouncycastle.crypto.modes.GCMModeCipher blockMode = org.bouncycastle.crypto.modes.GCMBlockCipher.newInstance(org.bouncycastle.crypto.engines.AESEngine.newInstance());
        blockMode.init(true, new org.bouncycastle.crypto.params.AEADParameters(new org.bouncycastle.crypto.params.KeyParameter(dataKey), 128, gcmNonce));
        byte[] plain = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] sealed = new byte[blockMode.getOutputSize(plain.length)];
        int sealedLen = blockMode.processBytes(plain, 0, plain.length, sealed, 0);
        sealedLen += blockMode.doFinal(sealed, sealedLen);
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(java.util.Arrays.copyOf(sealed, sealedLen)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
