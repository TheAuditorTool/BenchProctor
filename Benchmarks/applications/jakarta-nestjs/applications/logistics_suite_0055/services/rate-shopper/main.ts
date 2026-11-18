import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ShopRate } from "./rate_shop";
import { EnrichCheckpoint } from "./enrich_checkpoint";
import { ArchiveDigest } from "./archive_digest";
import { PublishWindow } from "./publish_window";
import { PublishSchedule } from "./publish_schedule";
import { PublishWaybill } from "./publish_waybill";
import { SummarizeLedger } from "./summarize_ledger";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ShopRate, EnrichCheckpoint, ArchiveDigest, PublishWindow, PublishSchedule, PublishWaybill, SummarizeLedger],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
