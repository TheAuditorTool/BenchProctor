// SPDX-License-Identifier: Apache-2.0
package com.example.fxservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class NormalizeLedger {


    @POST
    @Path("/NormalizeLedger")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeLedger(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = field != null ? field : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : subject.split(",")) { tokens.add(token.trim()); }
        String ledger = String.join(",", tokens);
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + ledger});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
