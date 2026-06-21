// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38984 {

    @PostMapping(path="/BenchmarkTest38984", consumes="multipart/form-data")
    public void BenchmarkTest38984(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String prefix = multipartValue.length() > 0 ? multipartValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = multipartValue.toLowerCase(); break;
            case "f": data = multipartValue.toUpperCase(); break;
            default: data = multipartValue.strip(); break;
        }
        java.net.URL u = new java.net.URL("https://api.svc.local/lookup?q=" + data);
        java.net.HttpURLConnection hc = (java.net.HttpURLConnection) u.openConnection();
        hc.connect();
        hc.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
