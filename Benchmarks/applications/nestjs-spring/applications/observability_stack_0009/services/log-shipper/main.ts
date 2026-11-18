import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ShipLog } from "./log_ship";
import { ValidateReceipt } from "./validate_receipt";
import { ValidateBundle } from "./validate_bundle";
import { LoadSummary } from "./load_summary";
import { CompactThreshold } from "./compact_threshold";
import { FetchIndex } from "./fetch_index";
import { EnrichRecord } from "./enrich_record";
import { NormalizeSchedule } from "./normalize_schedule";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ShipLog, ValidateReceipt, ValidateBundle, LoadSummary, CompactThreshold, FetchIndex, EnrichRecord, NormalizeSchedule],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
