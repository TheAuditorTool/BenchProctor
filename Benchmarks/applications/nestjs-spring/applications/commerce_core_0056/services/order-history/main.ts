import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { LookupOrder } from "./order_lookup";
import { VerifyWindow } from "./verify_window";
import { ArchivePolicy } from "./archive_policy";
import { ResolveBundle } from "./resolve_bundle";
import { EnrichReport } from "./enrich_report";
import { ValidateThreshold } from "./validate_threshold";
import { CompactRoster } from "./compact_roster";
import { VerifyOrder } from "./verify_order";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, LookupOrder, VerifyWindow, ArchivePolicy, ResolveBundle, EnrichReport, ValidateThreshold, CompactRoster, VerifyOrder],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
