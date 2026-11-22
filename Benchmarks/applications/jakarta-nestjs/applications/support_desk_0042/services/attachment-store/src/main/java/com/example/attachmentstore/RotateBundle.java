// SPDX-License-Identifier: Apache-2.0
package com.example.attachmentstore;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class RotateBundle {


    @GET
    @Path("/RotateBundle")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateBundle(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String blurb = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : blurb.split(",")) { tokens.add(token.trim()); }
        String inquiry = String.join(",", tokens);
        String streamedHtml = "<div class=\"comment\">" + inquiry + "</div>";
        javax.ws.rs.core.StreamingOutput htmlStream = htmlOut -> htmlOut.write(streamedHtml.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        return Response.ok(htmlStream, MediaType.TEXT_HTML).build();
    }
}
