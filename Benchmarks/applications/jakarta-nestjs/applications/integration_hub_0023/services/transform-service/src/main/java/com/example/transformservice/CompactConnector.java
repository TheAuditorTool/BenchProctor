// SPDX-License-Identifier: Apache-2.0
package com.example.transformservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class CompactConnector {


    @GET
    @Path("/CompactConnector")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactConnector(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = referer != null ? referer : "";
        String handshake = java.net.URLDecoder.decode(caption, java.nio.charset.StandardCharsets.UTF_8);
        String streamedHtml = "<div class=\"comment\">" + handshake + "</div>";
        javax.ws.rs.core.StreamingOutput htmlStream = htmlOut -> htmlOut.write(streamedHtml.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        return Response.ok(htmlStream, MediaType.TEXT_HTML).build();
    }
}
