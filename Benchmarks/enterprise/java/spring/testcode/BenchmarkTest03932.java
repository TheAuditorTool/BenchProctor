// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03932 {

    @PostMapping(path="/BenchmarkTest03932", consumes="application/xml")
    public void BenchmarkTest03932(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        new java.io.File(xmlValue).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
