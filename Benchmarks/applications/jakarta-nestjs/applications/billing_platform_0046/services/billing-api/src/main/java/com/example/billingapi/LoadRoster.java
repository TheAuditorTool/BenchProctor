// SPDX-License-Identifier: Apache-2.0
package com.example.billingapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class LoadRoster {


    @GET
    @Path("/LoadRoster")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadRoster(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = authorization != null ? authorization : "";
        String remittance;
        try { remittance = new String(java.util.Base64.getDecoder().decode(remark), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { remittance = remark; }
        return Response.ok("<div>" + remittance + "</div>", MediaType.TEXT_HTML).build();
    }
}
