// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.xml.parsers.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest18830 {

    @PostMapping(path="/BenchmarkTest18830", consumes="multipart/form-data")
    public void BenchmarkTest18830(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String prefix = uploadName.length() > 0 ? uploadName.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = uploadName.toLowerCase(); break;
            case "f": data = uploadName.toUpperCase(); break;
            default: data = uploadName.strip(); break;
        }
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
