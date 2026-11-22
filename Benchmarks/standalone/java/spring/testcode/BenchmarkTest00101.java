// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00101 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest00101", consumes="multipart/form-data")
    public void BenchmarkTest00101(@jakarta.validation.constraints.Size(max = 4096) @RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = normalize(multipartValue);
        javax.xml.stream.XMLInputFactory staxFactory = javax.xml.stream.XMLInputFactory.newInstance();
        staxFactory.setProperty(javax.xml.stream.XMLInputFactory.SUPPORT_DTD, false);
        staxFactory.setProperty(javax.xml.stream.XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
        javax.xml.stream.XMLStreamReader staxReader = staxFactory.createXMLStreamReader(new java.io.StringReader(data));
        StringBuilder xmlText = new StringBuilder();
        while (staxReader.hasNext()) { if (staxReader.next() == javax.xml.stream.XMLStreamConstants.CHARACTERS) { xmlText.append(staxReader.getText()); } }
        response.setHeader("X-Xml-Text-Length", String.valueOf(xmlText.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
