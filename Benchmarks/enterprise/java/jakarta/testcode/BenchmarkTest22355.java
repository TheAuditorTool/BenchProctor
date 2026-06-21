// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;
import javax.net.ssl.*;

@Path("/")
public class BenchmarkTest22355 {

    @GET
    @Path("/BenchmarkTest22355")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest22355(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(headerValue);
        String data = normalizer.apply(headerValue);
        java.security.KeyStore caStore = java.security.KeyStore.getInstance(java.security.KeyStore.getDefaultType());
        try (java.io.FileInputStream caIn = new java.io.FileInputStream(System.getProperty("java.home") + "/lib/security/cacerts")) {
            caStore.load(caIn, "changeit".toCharArray());
        }
        java.security.cert.PKIXBuilderParameters pkix = new java.security.cert.PKIXBuilderParameters(caStore, new java.security.cert.X509CertSelector());
        pkix.setRevocationEnabled(true);
        System.setProperty("com.sun.net.ssl.checkRevocation", "true");
        javax.net.ssl.TrustManagerFactory tmf = javax.net.ssl.TrustManagerFactory.getInstance("PKIX");
        tmf.init(new javax.net.ssl.CertPathTrustManagerParameters(pkix));
        javax.net.ssl.SSLContext sc = javax.net.ssl.SSLContext.getInstance("TLS");
        sc.init(null, tmf.getTrustManagers(), null);
        javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) java.net.URI.create("https://api.svc.local/data?ref=" + java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8)).toURL().openConnection();
        conn.setSSLSocketFactory(sc.getSocketFactory());
        conn.connect();
        conn.getInputStream().close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
