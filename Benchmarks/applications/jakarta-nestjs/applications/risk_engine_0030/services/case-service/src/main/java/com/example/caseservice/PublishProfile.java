// SPDX-License-Identifier: Apache-2.0
package com.example.caseservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class PublishProfile {

    private static String escapeHtml(String s) {
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#39;");
    }

    @GET
    @Path("/PublishProfile/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishProfile(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = pathId;
        java.util.function.Supplier<String> valueSupplier = () -> summary.strip();
        String grievance = valueSupplier.get();
        return Response.ok(escapeHtml(grievance), MediaType.TEXT_HTML).build();
    }
}
