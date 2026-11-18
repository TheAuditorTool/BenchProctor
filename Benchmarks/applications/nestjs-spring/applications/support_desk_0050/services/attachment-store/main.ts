import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { StoreAttachment } from "./attachment_store";
import { EnrichHeader } from "./enrich_header";
import { EnrichCheckpoint } from "./enrich_checkpoint";
import { PublishSurvey } from "./publish_survey";
import { LoadHeader } from "./load_header";
import { AuditSurvey } from "./audit_survey";
import { PruneRecord } from "./prune_record";
import { RenderEscalation } from "./render_escalation";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StoreAttachment, EnrichHeader, EnrichCheckpoint, PublishSurvey, LoadHeader, AuditSurvey, PruneRecord, RenderEscalation],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
