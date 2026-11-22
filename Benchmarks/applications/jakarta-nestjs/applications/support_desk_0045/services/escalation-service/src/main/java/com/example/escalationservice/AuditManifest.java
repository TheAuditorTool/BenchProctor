// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class AuditManifest {


    @GET
    @Path("/AuditManifest")
    @Produces(MediaType.APPLICATION_JSON)
    public Response auditManifest(@javax.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = userAgent != null ? userAgent : "";
        java.util.function.Supplier<String> valueSupplier = () -> remark.strip();
        String inquiry = valueSupplier.get();
        return Response.ok("<div>" + inquiry + "</div>", MediaType.TEXT_HTML).build();
    }
}
