import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { DispatchDelivery } from "./delivery_dispatch";
import { NormalizeSchedule } from "./normalize_schedule";
import { ResolveCheckpoint } from "./resolve_checkpoint";
import { PublishSummary } from "./publish_summary";
import { ArchiveCheckpoint } from "./archive_checkpoint";
import { NormalizeReceipt } from "./normalize_receipt";
import { NormalizeConfig } from "./normalize_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DispatchDelivery, NormalizeSchedule, ResolveCheckpoint, PublishSummary, ArchiveCheckpoint, NormalizeReceipt, NormalizeConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
