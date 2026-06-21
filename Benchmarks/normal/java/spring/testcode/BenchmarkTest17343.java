// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import javax.net.ssl.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17343 {

    @GetMapping("/BenchmarkTest17343")
    public void BenchmarkTest17343(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String prefix = refererValue.length() > 0 ? refererValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = refererValue.toLowerCase(); break;
            case "f": data = refererValue.toUpperCase(); break;
            default: data = refererValue.strip(); break;
        }
        javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) java.net.URI.create("https://api.svc.local/data?ref=" + java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8)).toURL().openConnection();
        conn.connect();
        conn.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
