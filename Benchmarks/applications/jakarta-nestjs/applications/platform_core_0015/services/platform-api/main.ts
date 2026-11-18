import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ProvisionTenant } from "./tenant_provision";
import { CompactFlag } from "./compact_flag";
import { VerifyDigest } from "./verify_digest";
import { EnrichDigest } from "./enrich_digest";
import { ValidateBundle } from "./validate_bundle";
import { ArchiveSchedule } from "./archive_schedule";
import { FetchBatch } from "./fetch_batch";
import { AnnotateProfile } from "./annotate_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ProvisionTenant, CompactFlag, VerifyDigest, EnrichDigest, ValidateBundle, ArchiveSchedule, FetchBatch, AnnotateProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
