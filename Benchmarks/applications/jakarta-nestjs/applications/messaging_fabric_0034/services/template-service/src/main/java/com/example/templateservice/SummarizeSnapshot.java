// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class SummarizeSnapshot {


    @POST
    @Path("/SummarizeSnapshot")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response summarizeSnapshot(@jakarta.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = xmlBody;
        request.setAttribute("wrapper", footnote);
        String bulletin = String.valueOf(request.getAttribute("wrapper"));
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(bulletin)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
