// SPDX-License-Identifier: Apache-2.0
package com.example.trackingservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class EnrichWindow {


    @GET
    @Path("/EnrichWindow")
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichWindow(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = referer != null ? referer : "";
        String consignment = java.net.URLDecoder.decode(caption, java.nio.charset.StandardCharsets.UTF_8);
        String streamedHtml = "<div class=\"comment\">" + consignment + "</div>";
        jakarta.ws.rs.core.StreamingOutput htmlStream = htmlOut -> htmlOut.write(streamedHtml.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        return Response.ok(htmlStream, MediaType.TEXT_HTML).build();
    }
}
