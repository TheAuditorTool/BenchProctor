// SPDX-License-Identifier: Apache-2.0
package com.example.digestservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class CompactChannel {


    @GET
    @Path("/CompactChannel")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactChannel(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = userAgent != null ? userAgent : "";
        java.util.function.Supplier<String> valueSupplier = () -> footnote.strip();
        String bulletin = valueSupplier.get();
        return Response.ok("<div>" + bulletin + "</div>", MediaType.TEXT_HTML).build();
    }
}
