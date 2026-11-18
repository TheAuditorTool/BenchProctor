import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { DeclareCustoms } from "./customs_declare";
import { FetchConfig } from "./fetch_config";
import { CompactBundle } from "./compact_bundle";
import { AuditDigest } from "./audit_digest";
import { PruneManifest } from "./prune_manifest";
import { RotateThreshold } from "./rotate_threshold";
import { FetchCarrier } from "./fetch_carrier";
import { AnnotateHeader } from "./annotate_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DeclareCustoms, FetchConfig, CompactBundle, AuditDigest, PruneManifest, RotateThreshold, FetchCarrier, AnnotateHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
