// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65604 {

    @GetMapping("/BenchmarkTest65604")
    public void BenchmarkTest65604(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(userId);
        String data = wrapper.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(processed)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
