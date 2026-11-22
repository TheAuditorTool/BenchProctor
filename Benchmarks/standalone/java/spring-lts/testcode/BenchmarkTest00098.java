// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00098 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00098", consumes="application/xml")
    public void BenchmarkTest00098(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data;
        try { data = String.valueOf(Integer.parseInt(xmlValue)); }
        catch (NumberFormatException e) { data = xmlValue; }
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
