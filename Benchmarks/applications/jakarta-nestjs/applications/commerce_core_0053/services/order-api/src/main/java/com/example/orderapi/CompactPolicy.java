// SPDX-License-Identifier: Apache-2.0
package com.example.orderapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CompactPolicy {


    @POST
    @Path("/CompactPolicy/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactPolicy(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String memo = java.util.Optional.ofNullable(commentText).orElse("");
        String voucher;
        if (memo.length() > 256) { voucher = memo.substring(0, 256); }
        else { voucher = memo; }
        if (!voucher.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + voucher + "</div>", MediaType.TEXT_HTML).build();
    }
}
