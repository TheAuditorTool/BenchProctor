// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08580 {

    @PostMapping(path="/BenchmarkTest08580", consumes="application/xml")
    public void BenchmarkTest08580(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.List<String> tokens = java.util.Arrays.asList(xmlValue.split(","));
        String data = String.join(",", tokens);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
