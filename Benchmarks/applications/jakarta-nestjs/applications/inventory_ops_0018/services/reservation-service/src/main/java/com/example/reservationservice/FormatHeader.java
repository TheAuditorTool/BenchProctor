// SPDX-License-Identifier: Apache-2.0
package com.example.reservationservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import jakarta.validation.Valid;

@Path("/")
class FormatHeader {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @POST
    @Path("/FormatHeader")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response formatHeader(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : transcript.split(",")) { tokens.add(token.trim()); }
        String backorder = String.join(",", tokens);
        Files.delete(Paths.get("/var/app/data/" + backorder));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
