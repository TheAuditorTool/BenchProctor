// SPDX-License-Identifier: Apache-2.0
package com.example.memberdirectory;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;

@Path("/")
public class AnnotateSummary {

    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @POST
    @Path("/AnnotateSummary")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateSummary(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = req.payload;
        String wording;
        if (paragraph.length() > 256) { wording = paragraph.substring(0, 256); }
        else { wording = paragraph; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + wording}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
