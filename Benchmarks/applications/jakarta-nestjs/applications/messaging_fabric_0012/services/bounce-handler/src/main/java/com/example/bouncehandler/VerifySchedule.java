// SPDX-License-Identifier: Apache-2.0
package com.example.bouncehandler;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class VerifySchedule {

    private static String normalize(String v) { return v.strip(); }

    @POST
    @Path("/VerifySchedule/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifySchedule(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = java.util.Optional.ofNullable(commentText).orElse("");
        String bulletin = normalize(preface);
        org.apache.hc.client5.http.classic.methods.HttpGet fetchRequest = new org.apache.hc.client5.http.classic.methods.HttpGet(bulletin);
        try (org.apache.hc.client5.http.impl.classic.CloseableHttpClient fetchClient = org.apache.hc.client5.http.impl.classic.HttpClients.createDefault()) {
            int fetchStatus = fetchClient.execute(fetchRequest, fetchResponse -> fetchResponse.getCode());
            response.setHeader("X-Fetch-Status", String.valueOf(fetchStatus));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
