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
public class BenchmarkTest48984 {

    @GET
    @Path("/BenchmarkTest48984")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest48984(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + originValue;
        String data = valueSupplier.get();
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
