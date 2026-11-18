// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
class EnrichWindow {


    @POST
    @Path("/EnrichWindow")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichWindow(@FormDataParam("file") org.glassfish.jersey.media.multipart.FormDataContentDisposition fileDetail, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = fileDetail.getFileName();
        String montage;
        try { montage = String.valueOf(Integer.parseInt(passage)); }
        catch (NumberFormatException e) { montage = passage; }
        byte[] serBytes = java.util.Base64.getDecoder().decode(montage);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
