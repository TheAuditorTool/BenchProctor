// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest30288 {

    @GetMapping("/BenchmarkTest30288")
    public void BenchmarkTest30288(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "default_config_label";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{secretValue});
        if (data == null) throw new IllegalArgumentException("input required");
        java.security.KeyStore ks = java.security.KeyStore.getInstance("PKCS12");
        ks.load(new java.io.FileInputStream("/etc/app/keystore.p12"), "changeit".toCharArray());
        java.security.Key keystoreKey = ks.getKey("api_key", "changeit".toCharArray());
        if (keystoreKey == null) throw new IllegalStateException("api_key not found in keystore");
        String storeCred = java.util.Base64.getEncoder().encodeToString(keystoreKey.getEncoded());
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", storeCred)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
