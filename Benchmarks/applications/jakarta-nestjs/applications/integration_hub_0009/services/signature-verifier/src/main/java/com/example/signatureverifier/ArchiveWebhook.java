// SPDX-License-Identifier: Apache-2.0
package com.example.signatureverifier;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class ArchiveWebhook {


    @GET
    @Path("/ArchiveWebhook")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveWebhook(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String heading = referer != null ? referer : "";
        String handshake = java.net.URLDecoder.decode(heading, java.nio.charset.StandardCharsets.UTF_8);
        String streamedHtml = "<div class=\"comment\">" + handshake + "</div>";
        jakarta.ws.rs.core.StreamingOutput htmlStream = htmlOut -> htmlOut.write(streamedHtml.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        return Response.ok(htmlStream, MediaType.TEXT_HTML).build();
    }
}
