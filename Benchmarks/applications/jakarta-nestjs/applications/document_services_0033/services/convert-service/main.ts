import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { RunConversion } from "./convert_job";
import { AuditSummary } from "./audit_summary";
import { PublishSchedule } from "./publish_schedule";
import { EnrichReceipt } from "./enrich_receipt";
import { FetchRecord } from "./fetch_record";
import { RenderThreshold } from "./render_threshold";
import { FormatProfile } from "./format_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunConversion, AuditSummary, PublishSchedule, EnrichReceipt, FetchRecord, RenderThreshold, FormatProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
