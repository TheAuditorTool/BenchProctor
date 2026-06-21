// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52859 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @PostMapping(path="/BenchmarkTest52859", consumes="text/plain")
    public void BenchmarkTest52859(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = stripCRLF(rawData);
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
