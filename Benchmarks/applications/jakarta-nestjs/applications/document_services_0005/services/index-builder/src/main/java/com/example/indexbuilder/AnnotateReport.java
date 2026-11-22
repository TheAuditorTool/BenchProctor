// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
public class AnnotateReport {

    static final class FormData {
        private final String payload;
        FormData(String payload) { this.payload = payload; }
        String getPayload() { return payload; }
    }

    @POST
    @Path("/AnnotateReport")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateReport(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = rawBody != null ? rawBody : "";
        FormData payload = new FormData(footnote);
        String addendum = payload.getPayload();
        byte[] serBytes = java.util.Base64.getDecoder().decode(addendum);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
