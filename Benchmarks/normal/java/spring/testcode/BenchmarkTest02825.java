// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02825 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @PostMapping(path="/BenchmarkTest02825", consumes="application/xml")
    public void BenchmarkTest02825(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        FormData payload = new FormData(xmlValue);
        String data = payload.payload;
        if (!data.isEmpty()) throw new Exception("processing error: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
