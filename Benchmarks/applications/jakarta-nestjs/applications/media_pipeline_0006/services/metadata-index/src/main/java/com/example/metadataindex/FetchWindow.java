// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class FetchWindow {

    private static String escapeHtml(String s) {
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#39;");
    }

    @GET
    @Path("/FetchWindow/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response fetchWindow(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = pathId;
        java.util.function.Supplier<String> valueSupplier = () -> passage.strip();
        String montage = valueSupplier.get();
        return Response.ok(escapeHtml(montage), MediaType.TEXT_HTML).build();
    }
}
