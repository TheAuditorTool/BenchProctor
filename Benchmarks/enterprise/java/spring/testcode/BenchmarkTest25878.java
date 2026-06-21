// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest25878 {

    @PostMapping(path="/BenchmarkTest25878", consumes="application/xml")
    public void BenchmarkTest25878(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.function.Function<String, String> primary = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> stripChain = primary.andThen(String::strip);
        String data = stripChain.apply(xmlValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.sendRedirect(processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
