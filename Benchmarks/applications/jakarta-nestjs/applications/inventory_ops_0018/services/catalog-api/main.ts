import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { LookupSku } from "./sku_lookup";
import { ArchiveProfile } from "./archive_profile";
import { EnrichIndex } from "./enrich_index";
import { CompactIndex } from "./compact_index";
import { ValidateBatch } from "./validate_batch";
import { ValidateRoster } from "./validate_roster";
import { ReconcileRecord } from "./reconcile_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, LookupSku, ArchiveProfile, EnrichIndex, CompactIndex, ValidateBatch, ValidateRoster, ReconcileRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
