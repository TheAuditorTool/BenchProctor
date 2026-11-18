// SPDX-License-Identifier: Apache-2.0
package com.example.attachmentstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class EnrichHeader {


    @POST
    @Path("/EnrichHeader")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichHeader(@jakarta.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = xmlBody;
        request.setAttribute("carrier", remark);
        String inquiry = String.valueOf(request.getAttribute("carrier"));
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(inquiry)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
