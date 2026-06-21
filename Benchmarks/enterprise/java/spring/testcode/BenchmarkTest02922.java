// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02922 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @PostMapping(path="/BenchmarkTest02922", consumes="application/xml")
    public void BenchmarkTest02922(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = toLowerCase(xmlValue);
        response.sendError(500, data);
    }
}
