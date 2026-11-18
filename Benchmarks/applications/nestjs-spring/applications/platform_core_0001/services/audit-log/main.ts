import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { AppendAudit } from "./audit_append";
import { ExportRoster } from "./export_roster";
import { CompactHeader } from "./compact_header";
import { AnnotateSchedule } from "./annotate_schedule";
import { CollectDigest } from "./collect_digest";
import { BuildConfig } from "./build_config";
import { PruneRecord } from "./prune_record";
import { AuditManifest } from "./audit_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AppendAudit, ExportRoster, CompactHeader, AnnotateSchedule, CollectDigest, BuildConfig, PruneRecord, AuditManifest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
