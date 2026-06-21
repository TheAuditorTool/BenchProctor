// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37101 {

    @PostMapping(path="/BenchmarkTest37101", consumes="text/plain")
    public void BenchmarkTest37101(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + rawData.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
        URL url = java.net.URI.create("http://" + data).toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        try {
            conn.connect();
            conn.getInputStream().close();
        } finally { conn.disconnect(); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
