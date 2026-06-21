// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest79760 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @PostMapping("/BenchmarkTest79760")
    public void BenchmarkTest79760(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = expandTabs(fieldValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
