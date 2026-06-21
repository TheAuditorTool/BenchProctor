// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38371 {

    @PostMapping(path="/BenchmarkTest38371", consumes="application/xml")
    public void BenchmarkTest38371(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(xmlValue, "query");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
