import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { CreateLabel } from "./label_create";
import { VerifyProfile } from "./verify_profile";
import { PublishReceipt } from "./publish_receipt";
import { ReconcileCheckpoint } from "./reconcile_checkpoint";
import { ValidateProfile } from "./validate_profile";
import { BuildHeader } from "./build_header";
import { ArchiveThreshold } from "./archive_threshold";
import { ResolveSummary } from "./resolve_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CreateLabel, VerifyProfile, PublishReceipt, ReconcileCheckpoint, ValidateProfile, BuildHeader, ArchiveThreshold, ResolveSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
