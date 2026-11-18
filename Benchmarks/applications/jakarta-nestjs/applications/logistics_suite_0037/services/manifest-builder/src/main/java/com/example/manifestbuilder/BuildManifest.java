// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class BuildManifest {


    @GET
    @Path("/BuildManifest")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildManifest(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/var/app/data.txt")))).orElse("");
        java.util.function.Supplier<String> valueSupplier = () -> footnote.strip();
        String consignment = valueSupplier.get();
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://label-service:3000/label-service/createLabel").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"shipping_payload\": \"" + consignment + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
