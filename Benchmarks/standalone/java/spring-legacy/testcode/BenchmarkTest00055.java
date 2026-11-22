// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00055 {
    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping("/BenchmarkTest00055")
    public void BenchmarkTest00055(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String data = transform.apply(jsonValue);
        StringBuilder xmlText = new StringBuilder();
        javax.xml.parsers.SAXParserFactory saxFactory = javax.xml.parsers.SAXParserFactory.newInstance();
        saxFactory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
        javax.xml.parsers.SAXParser saxParser = saxFactory.newSAXParser();
        saxParser.parse(new org.xml.sax.InputSource(new java.io.StringReader(data)), new org.xml.sax.helpers.DefaultHandler() { @Override public void characters(char[] ch, int start, int length) { xmlText.append(ch, start, length); } });
        response.setHeader("X-Xml-Text-Length", String.valueOf(xmlText.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
