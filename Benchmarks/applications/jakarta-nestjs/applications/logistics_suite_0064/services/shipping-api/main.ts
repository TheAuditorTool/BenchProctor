import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { QuoteShipment } from "./shipment_quote";
import { RenderThreshold } from "./render_threshold";
import { ExportIndex } from "./export_index";
import { FetchBatch } from "./fetch_batch";
import { MergeSnapshot } from "./merge_snapshot";
import { ReconcileRoster } from "./reconcile_roster";
import { NormalizeBatch } from "./normalize_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QuoteShipment, RenderThreshold, ExportIndex, FetchBatch, MergeSnapshot, ReconcileRoster, NormalizeBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
