// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76542 {

    @PostMapping(path="/BenchmarkTest76542", consumes="application/xml")
    public void BenchmarkTest76542(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(xmlValue, "body");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        response.sendError(500, data);
    }
}
