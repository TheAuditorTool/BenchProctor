// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02937 {

    @PostMapping(path="/BenchmarkTest02937", consumes="application/xml")
    public void BenchmarkTest02937(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(xmlValue, "json");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
    }
}
