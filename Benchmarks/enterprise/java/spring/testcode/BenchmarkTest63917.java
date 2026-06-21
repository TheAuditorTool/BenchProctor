// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import javax.net.ssl.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63917 {

    @PostMapping(path="/BenchmarkTest63917", consumes="text/plain")
    public void BenchmarkTest63917(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> rawData)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        java.security.KeyStore caStore = java.security.KeyStore.getInstance(java.security.KeyStore.getDefaultType());
        try (java.io.FileInputStream caIn = new java.io.FileInputStream(System.getProperty("java.home") + "/lib/security/cacerts")) {
            caStore.load(caIn, "changeit".toCharArray());
        }
        java.security.cert.PKIXBuilderParameters pkix = new java.security.cert.PKIXBuilderParameters(caStore, new java.security.cert.X509CertSelector());
        pkix.setRevocationEnabled(false);
        javax.net.ssl.TrustManagerFactory tmf = javax.net.ssl.TrustManagerFactory.getInstance("PKIX");
        tmf.init(new javax.net.ssl.CertPathTrustManagerParameters(pkix));
        javax.net.ssl.SSLContext sc = javax.net.ssl.SSLContext.getInstance("TLS");
        sc.init(null, tmf.getTrustManagers(), null);
        javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) java.net.URI.create(data.contains("://") ? data : "https://" + data).toURL().openConnection();
        conn.setSSLSocketFactory(sc.getSocketFactory());
        conn.connect();
        conn.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
