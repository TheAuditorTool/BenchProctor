import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ScheduleJob } from "./job_schedule";
import { AuditCheckpoint } from "./audit_checkpoint";
import { CompactProfile } from "./compact_profile";
import { RenderQuota } from "./render_quota";
import { CollectCheckpoint } from "./collect_checkpoint";
import { EnrichRoster } from "./enrich_roster";
import { ArchiveReport } from "./archive_report";
import { CompactQuota } from "./compact_quota";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ScheduleJob, AuditCheckpoint, CompactProfile, RenderQuota, CollectCheckpoint, EnrichRoster, ArchiveReport, CompactQuota],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
