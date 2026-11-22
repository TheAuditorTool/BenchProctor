// SPDX-License-Identifier: Apache-2.0
package com.example.mandateregistry;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
public class MergeThreshold {


    @POST
    @Path("/MergeThreshold/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response mergeThreshold(@javax.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = java.util.Optional.ofNullable(commentText).orElse("");
        String disbursement;
        if (headline.length() > 256) { disbursement = headline.substring(0, 256); }
        else { disbursement = headline; }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = objectMapper.readValue(disbursement.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
