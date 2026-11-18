// SPDX-License-Identifier: Apache-2.0
package com.example.releaseapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import jakarta.validation.Valid;

@Path("/")
class BuildPolicy {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @POST
    @Path("/BuildPolicy")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildPolicy(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = req.payload;
        java.util.function.Supplier<String> valueSupplier = () -> footnote.strip();
        String wording = valueSupplier.get();
        byte[] serBytes = java.util.Base64.getDecoder().decode(wording);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
