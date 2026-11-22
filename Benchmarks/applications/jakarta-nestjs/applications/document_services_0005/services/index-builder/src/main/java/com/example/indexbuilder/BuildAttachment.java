// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BuildAttachment {


    @POST
    @Path("/BuildAttachment")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildAttachment(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = rawBody != null ? rawBody : "";
        String addendum;
        if (footnote.length() > 256) { addendum = footnote.substring(0, 256); }
        else { addendum = footnote; }
        Files.write(Paths.get("/var/uploads/" + addendum), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
