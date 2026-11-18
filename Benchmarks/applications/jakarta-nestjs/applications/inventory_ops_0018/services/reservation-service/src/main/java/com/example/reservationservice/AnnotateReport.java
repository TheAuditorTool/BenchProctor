// SPDX-License-Identifier: Apache-2.0
package com.example.reservationservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
class AnnotateReport {


    @POST
    @Path("/AnnotateReport")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateReport(@FormDataParam("file") org.glassfish.jersey.media.multipart.FormDataContentDisposition fileDetail, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = fileDetail.getFileName();
        String backorder;
        try { backorder = String.valueOf(Integer.parseInt(transcript)); }
        catch (NumberFormatException e) { backorder = transcript; }
        byte[] serBytes = java.util.Base64.getDecoder().decode(backorder);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
