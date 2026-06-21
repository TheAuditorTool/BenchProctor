// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13474 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GetMapping("/BenchmarkTest13474/{pathId}")
    public void BenchmarkTest13474(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        FormData payload = new FormData(pathValue);
        String data = payload.payload;
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        java.net.URL u = new java.net.URL("https://api.svc.local/lookup?q=" + data);
        java.net.HttpURLConnection hc = (java.net.HttpURLConnection) u.openConnection();
        hc.connect();
        hc.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
