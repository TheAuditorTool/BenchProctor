import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { EnforceQuota } from "./quota_enforce";
import { ArchiveSummary } from "./archive_summary";
import { CollectHeader } from "./collect_header";
import { PublishThreshold } from "./publish_threshold";
import { ExportSchedule } from "./export_schedule";
import { SummarizeWindow } from "./summarize_window";
import { AuditSecret } from "./audit_secret";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, EnforceQuota, ArchiveSummary, CollectHeader, PublishThreshold, ExportSchedule, SummarizeWindow, AuditSecret],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
