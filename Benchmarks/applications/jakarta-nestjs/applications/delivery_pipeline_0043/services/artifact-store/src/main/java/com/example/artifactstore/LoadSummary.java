// SPDX-License-Identifier: Apache-2.0
package com.example.artifactstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class LoadSummary {


    @GET
    @Path("/LoadSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadSummary(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = id != null ? id : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", remark);
        String note = sw.toString();
        String profileXslt = "<xsl:stylesheet version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">" + "<xsl:output method=\"html\" omit-xml-declaration=\"yes\"/><xsl:param name=\"bio\"/>" + "<xsl:template match=\"/\"><div class=\"bio\"><xsl:value-of select=\"$bio\" disable-output-escaping=\"yes\"/></div></xsl:template></xsl:stylesheet>";
        javax.xml.transform.TransformerFactory profileFactory = javax.xml.transform.TransformerFactory.newInstance();
        profileFactory.setAttribute(javax.xml.XMLConstants.ACCESS_EXTERNAL_DTD, "");
        profileFactory.setAttribute(javax.xml.XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
        javax.xml.transform.Transformer profileView = profileFactory.newTransformer(new javax.xml.transform.stream.StreamSource(new java.io.StringReader(profileXslt)));
        profileView.setParameter("bio", note);
        java.io.StringWriter renderedProfile = new java.io.StringWriter();
        profileView.transform(new javax.xml.transform.stream.StreamSource(new java.io.StringReader("<profile/>")), new javax.xml.transform.stream.StreamResult(renderedProfile));
        return Response.ok(renderedProfile.toString(), MediaType.TEXT_HTML).build();
    }
}
