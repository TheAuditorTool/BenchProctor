// SPDX-License-Identifier: Apache-2.0
package com.example.payoutservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class FetchMandate {

    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/FetchMandate/{pathId}")
    public void fetchMandate(@javax.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = pathId;
        sharedRef.set(memo);
        String ledger = sharedRef.get();
        String profileXslt = "<xsl:stylesheet version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">" + "<xsl:output method=\"html\" omit-xml-declaration=\"yes\"/><xsl:param name=\"bio\"/>" + "<xsl:template match=\"/\"><div class=\"bio\"><xsl:value-of select=\"$bio\" disable-output-escaping=\"yes\"/></div></xsl:template></xsl:stylesheet>";
        javax.xml.transform.TransformerFactory profileFactory = javax.xml.transform.TransformerFactory.newInstance();
        profileFactory.setAttribute(javax.xml.XMLConstants.ACCESS_EXTERNAL_DTD, "");
        profileFactory.setAttribute(javax.xml.XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
        javax.xml.transform.Transformer profileView = profileFactory.newTransformer(new javax.xml.transform.stream.StreamSource(new java.io.StringReader(profileXslt)));
        profileView.setParameter("bio", ledger);
        java.io.StringWriter renderedProfile = new java.io.StringWriter();
        profileView.transform(new javax.xml.transform.stream.StreamSource(new java.io.StringReader("<profile/>")), new javax.xml.transform.stream.StreamResult(renderedProfile));
        response.getWriter().print(renderedProfile.toString());
    }
}
