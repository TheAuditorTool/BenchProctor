// SPDX-License-Identifier: Apache-2.0
package com.example.fxservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class CompactDigest {


    @GET
    @Path("/CompactDigest")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactDigest(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = origin != null ? origin : "";
        String prefix = subject.length() > 0 ? subject.substring(0, 1).toLowerCase() : "";
        String ledger;
        switch (prefix) {
            case "h": ledger = subject.toLowerCase(); break;
            case "f": ledger = subject.toUpperCase(); break;
            default: ledger = subject.strip(); break;
        }
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(ledger)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
