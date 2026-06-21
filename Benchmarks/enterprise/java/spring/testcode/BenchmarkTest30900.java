// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import javax.net.ssl.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest30900 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/BenchmarkTest30900", consumes="application/json")
    public void BenchmarkTest30900(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties holder = new java.util.Properties();
        holder.load(new java.io.StringReader("rawValue=" + graphqlVar.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", holder.getProperty("format", "plain"));
        String data = holder.getProperty("rawValue", "");
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
