import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SendSurvey } from "./survey_send";
import { EnrichPolicy } from "./enrich_policy";
import { AuditSnapshot } from "./audit_snapshot";
import { CompactRecord } from "./compact_record";
import { MergeBundle } from "./merge_bundle";
import { PruneManifest } from "./prune_manifest";
import { FetchHeader } from "./fetch_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SendSurvey, EnrichPolicy, AuditSnapshot, CompactRecord, MergeBundle, PruneManifest, FetchHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
