// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest69972 {

    @PostMapping(path="/BenchmarkTest69972", consumes="application/xml")
    public void BenchmarkTest69972(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + xmlValue + "\">");
    }
}
