// SPDX-License-Identifier: Apache-2.0
package com.example.trackingservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class BuildRecord {


    @GET
    @Path("/BuildRecord")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildRecord(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = authorization != null ? authorization : "";
        String parcel;
        if (transcript.length() > 256) { parcel = transcript.substring(0, 256); }
        else { parcel = transcript; }
        byte[] serBytes = java.util.Base64.getDecoder().decode(parcel);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
