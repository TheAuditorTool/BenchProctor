// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00110 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00110", consumes="application/xml")
    public void BenchmarkTest00110(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", xmlValue);
        String data = holder.getProperty("value", "");
        org.bouncycastle.crypto.Digest contentDigest = new org.bouncycastle.crypto.digests.SHA256Digest();
        byte[] digestInput = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        contentDigest.update(digestInput, 0, digestInput.length);
        byte[] digest = new byte[contentDigest.getDigestSize()];
        contentDigest.doFinal(digest, 0);
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
