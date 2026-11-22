import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { StartCheckout } from "./checkout_session";
import { PublishSchedule } from "./publish_schedule";
import { CompactThreshold } from "./compact_threshold";
import { SummarizeLedger } from "./summarize_ledger";
import { SummarizeSchedule } from "./summarize_schedule";
import { ExportSchedule } from "./export_schedule";
import { ExportDigest } from "./export_digest";
import { FetchPromotion } from "./fetch_promotion";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StartCheckout, PublishSchedule, CompactThreshold, SummarizeLedger, SummarizeSchedule, ExportSchedule, ExportDigest, FetchPromotion],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
