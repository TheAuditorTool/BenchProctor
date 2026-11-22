// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class ReconcileDispute {

    static final class FormData {
        private final String payload;
        FormData(String payload) { this.payload = payload; }
        String getPayload() { return payload; }
    }

    @GET
    @Path("/ReconcileDispute")
    @Produces(MediaType.APPLICATION_JSON)
    public Response reconcileDispute(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = referer != null ? referer : "";
        FormData payload = new FormData(footnote);
        String remittance = payload.getPayload();
        if (!remittance.matches("^[a-zA-Z0-9 _.#~\\-]+$")) { return Response.status(400).build(); }
        Files.write(Paths.get("/var/uploads/" + remittance), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
