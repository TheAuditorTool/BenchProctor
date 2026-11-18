import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ApplyRedaction } from "./redaction_apply";
import { PublishRoster } from "./publish_roster";
import { PublishLedger } from "./publish_ledger";
import { EnrichSnapshot } from "./enrich_snapshot";
import { AnnotateProfile } from "./annotate_profile";
import { PublishSignature } from "./publish_signature";
import { ReconcileAttachment } from "./reconcile_attachment";
import { SummarizeCheckpoint } from "./summarize_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ApplyRedaction, PublishRoster, PublishLedger, EnrichSnapshot, AnnotateProfile, PublishSignature, ReconcileAttachment, SummarizeCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
