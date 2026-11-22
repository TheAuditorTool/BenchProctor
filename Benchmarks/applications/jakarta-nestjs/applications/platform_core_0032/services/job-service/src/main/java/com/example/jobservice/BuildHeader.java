// SPDX-License-Identifier: Apache-2.0
package com.example.jobservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class BuildHeader {


    @GET
    @Path("/BuildHeader")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildHeader(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = userAgent != null ? userAgent : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String persona = transform.apply(remark);
        String streamedHtml = "<div class=\"comment\">" + persona + "</div>";
        jakarta.ws.rs.core.StreamingOutput htmlStream = htmlOut -> htmlOut.write(streamedHtml.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        return Response.ok(htmlStream, MediaType.TEXT_HTML).build();
    }
}
