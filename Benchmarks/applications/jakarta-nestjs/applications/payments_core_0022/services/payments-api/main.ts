import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { AuthorizePayment } from "./payment_authorize";
import { AnnotateSnapshot } from "./annotate_snapshot";
import { EnrichSchedule } from "./enrich_schedule";
import { ArchivePolicy } from "./archive_policy";
import { AuditThreshold } from "./audit_threshold";
import { SummarizeThreshold } from "./summarize_threshold";
import { FetchRecord } from "./fetch_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AuthorizePayment, AnnotateSnapshot, EnrichSchedule, ArchivePolicy, AuditThreshold, SummarizeThreshold, FetchRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
