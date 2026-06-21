// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import javax.net.ssl.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07613 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @PostMapping(path="/BenchmarkTest07613", consumes="application/xml")
    public void BenchmarkTest07613(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = stripCRLF(xmlValue);
        javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) java.net.URI.create("https://api.svc.local/data?ref=" + java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8)).toURL().openConnection();
        conn.connect();
        conn.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
