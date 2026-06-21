// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest26343 {

    @PostMapping(path="/BenchmarkTest26343", consumes="application/xml")
    public void BenchmarkTest26343(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Properties box = new java.util.Properties();
        box.load(new java.io.StringReader("rawValue=" + xmlValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", box.getProperty("format", "plain"));
        String data = box.getProperty("rawValue", "");
        response.setHeader("Refresh", "0; url=" + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
