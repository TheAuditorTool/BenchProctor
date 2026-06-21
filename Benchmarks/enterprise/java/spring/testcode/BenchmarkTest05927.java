// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import javax.net.ssl.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05927 {

    @GetMapping("/BenchmarkTest05927")
    public void BenchmarkTest05927(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(originValue.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        javax.net.ssl.TrustManager[] tm = new javax.net.ssl.TrustManager[]{new javax.net.ssl.X509TrustManager(){
            public void checkClientTrusted(java.security.cert.X509Certificate[] c, String a){}
            public void checkServerTrusted(java.security.cert.X509Certificate[] c, String a){}
            public java.security.cert.X509Certificate[] getAcceptedIssuers(){return new java.security.cert.X509Certificate[0];}
        }};
        javax.net.ssl.SSLContext sc = javax.net.ssl.SSLContext.getInstance("TLS");
        sc.init(null, tm, null);
        javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) java.net.URI.create(data.contains("://") ? data : "https://" + data).toURL().openConnection();
        conn.setSSLSocketFactory(sc.getSocketFactory());
        conn.setHostnameVerifier((_h, session) -> true);
        conn.connect();
        conn.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
