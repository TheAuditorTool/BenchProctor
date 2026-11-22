// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class BuildDispute {


    @POST
    @Path("/BuildDispute")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildDispute(@javax.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = field != null ? field : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : footnote.split(",")) { tokens.add(token.trim()); }
        String remittance = String.join(",", tokens);
        String profileXslt = "<xsl:stylesheet version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">" + "<xsl:output method=\"html\" omit-xml-declaration=\"yes\"/><xsl:param name=\"bio\"/>" + "<xsl:template match=\"/\"><div class=\"bio\"><xsl:value-of select=\"$bio\"/></div></xsl:template></xsl:stylesheet>";
        javax.xml.transform.TransformerFactory profileFactory = javax.xml.transform.TransformerFactory.newInstance();
        profileFactory.setAttribute(javax.xml.XMLConstants.ACCESS_EXTERNAL_DTD, "");
        profileFactory.setAttribute(javax.xml.XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
        javax.xml.transform.Transformer profileView = profileFactory.newTransformer(new javax.xml.transform.stream.StreamSource(new java.io.StringReader(profileXslt)));
        profileView.setParameter("bio", remittance);
        java.io.StringWriter renderedProfile = new java.io.StringWriter();
        profileView.transform(new javax.xml.transform.stream.StreamSource(new java.io.StringReader("<profile/>")), new javax.xml.transform.stream.StreamResult(renderedProfile));
        return Response.ok(renderedProfile.toString(), MediaType.TEXT_HTML).build();
    }
}
