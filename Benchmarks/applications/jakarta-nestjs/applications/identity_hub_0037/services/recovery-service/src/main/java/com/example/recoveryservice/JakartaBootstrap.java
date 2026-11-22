package com.example.recoveryservice;

public class JakartaBootstrap {

    @javax.ws.rs.Path("/health")
    public static class HealthResource {
        @javax.ws.rs.GET
        public javax.ws.rs.core.Response health() {
            return javax.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.recoveryservice.JakartaBootstrap$HealthResource,com.example.recoveryservice.AuditDigest,com.example.recoveryservice.AuditReport,com.example.recoveryservice.EnrichConfig,com.example.recoveryservice.PrunePolicy,com.example.recoveryservice.StartRecovery,com.example.recoveryservice.SummarizeSchedule,com.example.recoveryservice.ValidateManifest,com.example.recoveryservice.VerifyBatch,org.glassfish.jersey.media.multipart.MultiPartFeature");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
