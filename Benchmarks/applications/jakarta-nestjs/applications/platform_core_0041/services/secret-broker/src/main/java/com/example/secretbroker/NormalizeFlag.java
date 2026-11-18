// SPDX-License-Identifier: Apache-2.0
package com.example.secretbroker;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class NormalizeFlag {


    @GET
    @Path("/NormalizeFlag")
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeFlag(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = authorization != null ? authorization : "";
        String persona;
        if (passage.length() > 256) { persona = passage.substring(0, 256); }
        else { persona = passage; }
        byte[] serBytes = java.util.Base64.getDecoder().decode(persona);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
