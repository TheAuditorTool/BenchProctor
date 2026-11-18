// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class CollectSummary {


    @POST
    @Path("/CollectSummary/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectSummary(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String parcel = transform.apply(phrase);
        Files.delete(Paths.get("/var/app/data/" + parcel));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
