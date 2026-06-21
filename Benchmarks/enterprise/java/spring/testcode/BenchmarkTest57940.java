// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57940 {

    private static String trimEnds(String v) { return v.trim(); }

    @PostMapping(path="/BenchmarkTest57940", consumes="application/xml")
    public void BenchmarkTest57940(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = trimEnds(xmlValue);
        if (!new java.io.File("/var/app/data", new java.io.File(data).getName()).delete()) { response.sendError(500, "delete failed"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
