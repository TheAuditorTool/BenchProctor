// SPDX-License-Identifier: Apache-2.0
package com.example.payoutservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class CollectReport {


    @GET
    @Path("/CollectReport")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectReport(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = origin != null ? origin : "";
        String prefix = headline.length() > 0 ? headline.substring(0, 1).toLowerCase() : "";
        String disbursement;
        switch (prefix) {
            case "h": disbursement = headline.toLowerCase(); break;
            case "f": disbursement = headline.toUpperCase(); break;
            default: disbursement = headline.strip(); break;
        }
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(disbursement)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
