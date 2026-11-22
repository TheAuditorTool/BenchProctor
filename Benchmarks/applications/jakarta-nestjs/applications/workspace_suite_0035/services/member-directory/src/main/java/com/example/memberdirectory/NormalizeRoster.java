// SPDX-License-Identifier: Apache-2.0
package com.example.memberdirectory;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class NormalizeRoster {


    @POST
    @Path("/NormalizeRoster")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeRoster(@javax.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = xmlBody;
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> paragraph.replaceAll("[ ]{2,}", " ").strip())
            .thenApply(v -> v.strip().replaceAll("[ \\t]+", " "));
        String wording = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        org.apache.hc.client5.http.classic.methods.HttpGet fetchRequest = new org.apache.hc.client5.http.classic.methods.HttpGet(wording);
        try (org.apache.hc.client5.http.impl.classic.CloseableHttpClient fetchClient = org.apache.hc.client5.http.impl.classic.HttpClients.createDefault()) {
            int fetchStatus = fetchClient.execute(fetchRequest, fetchResponse -> fetchResponse.getCode());
            response.setHeader("X-Fetch-Status", String.valueOf(fetchStatus));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
