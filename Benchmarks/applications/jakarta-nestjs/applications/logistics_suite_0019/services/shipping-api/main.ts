import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { QuoteShipment } from "./shipment_quote";
import { RenderRoster } from "./render_roster";
import { FetchWindow } from "./fetch_window";
import { CompactConfig } from "./compact_config";
import { CollectReport } from "./collect_report";
import { CollectLedger } from "./collect_ledger";
import { NormalizeDigest } from "./normalize_digest";
import { BuildCheckpoint } from "./build_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QuoteShipment, RenderRoster, FetchWindow, CompactConfig, CollectReport, CollectLedger, NormalizeDigest, BuildCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
