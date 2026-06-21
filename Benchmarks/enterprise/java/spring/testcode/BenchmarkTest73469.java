// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73469 {

    @PostMapping(path="/BenchmarkTest73469", consumes="text/plain")
    public void BenchmarkTest73469(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.function.Function<String, String> initialFn = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::trim);
        String data = transformed.apply(rawData);
        if (!data.matches("^[\\w\\s./\\\\:<>=_'\\\"!\\[\\]-]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
