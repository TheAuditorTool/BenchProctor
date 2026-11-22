// SPDX-License-Identifier: Apache-2.0
package com.example.recoveryservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class AuditReport {


    @GET
    @Path("/AuditReport")
    @Produces(MediaType.APPLICATION_JSON)
    public Response auditReport(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> remark.strip();
        String persona = valueSupplier.get();
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + persona});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
