// SPDX-License-Identifier: Apache-2.0
package com.example.canarycontroller;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactPolicy {


    @GetMapping("/CompactPolicy")
    public void compactPolicy(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = sessionToken != null ? sessionToken : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(remark, "query");
        String note = kv.getKey();
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String phrase = policy.sanitize(note);
        String profileXslt = "<xsl:stylesheet version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">" + "<xsl:output method=\"html\" omit-xml-declaration=\"yes\"/><xsl:param name=\"bio\"/>" + "<xsl:template match=\"/\"><div class=\"bio\"><xsl:value-of select=\"$bio\" disable-output-escaping=\"yes\"/></div></xsl:template></xsl:stylesheet>";
        javax.xml.transform.TransformerFactory profileFactory = javax.xml.transform.TransformerFactory.newInstance();
        profileFactory.setAttribute(javax.xml.XMLConstants.ACCESS_EXTERNAL_DTD, "");
        profileFactory.setAttribute(javax.xml.XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
        javax.xml.transform.Transformer profileView = profileFactory.newTransformer(new javax.xml.transform.stream.StreamSource(new java.io.StringReader(profileXslt)));
        profileView.setParameter("bio", phrase);
        java.io.StringWriter renderedProfile = new java.io.StringWriter();
        profileView.transform(new javax.xml.transform.stream.StreamSource(new java.io.StringReader("<profile/>")), new javax.xml.transform.stream.StreamResult(renderedProfile));
        response.getWriter().print(renderedProfile.toString());
    }
}
