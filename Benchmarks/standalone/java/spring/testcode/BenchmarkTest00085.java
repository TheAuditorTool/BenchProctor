// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00085 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00085", consumes="application/json")
    public void BenchmarkTest00085(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String data = graphqlVar.replace("\u0000", "");
        byte[] dataKey = java.util.Base64.getDecoder().decode(System.getenv("DATA_ENC_KEY"));
        byte[] streamNonce = new byte[12]; new java.security.SecureRandom().nextBytes(streamNonce);
        org.bouncycastle.crypto.modes.ChaCha20Poly1305 aead = new org.bouncycastle.crypto.modes.ChaCha20Poly1305();
        aead.init(true, new org.bouncycastle.crypto.params.ParametersWithIV(new org.bouncycastle.crypto.params.KeyParameter(dataKey), streamNonce));
        byte[] plain = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] sealed = new byte[aead.getOutputSize(plain.length)];
        int sealedLen = aead.processBytes(plain, 0, plain.length, sealed, 0);
        aead.doFinal(sealed, sealedLen);
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(sealed));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
