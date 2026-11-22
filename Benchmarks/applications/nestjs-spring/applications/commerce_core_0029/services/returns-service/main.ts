import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RequestReturn } from "./return_request";
import { ArchiveWindow } from "./archive_window";
import { NormalizeCheckpoint } from "./normalize_checkpoint";
import { ValidateHeader } from "./validate_header";
import { CollectFulfillment } from "./collect_fulfillment";
import { RotateFulfillment } from "./rotate_fulfillment";
import { EnrichProfile } from "./enrich_profile";
import { FormatHeader } from "./format_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RequestReturn, ArchiveWindow, NormalizeCheckpoint, ValidateHeader, CollectFulfillment, RotateFulfillment, EnrichProfile, FormatHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
