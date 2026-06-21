// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73850 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest73850", consumes="application/xml")
    public void BenchmarkTest73850(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = normalize(xmlValue);
        response.getWriter().print(String.valueOf(data));
    }
}
