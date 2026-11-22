import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { DispatchCarrier } from "./carrier_dispatch";
import { SummarizeShipment } from "./summarize_shipment";
import { CompactSchedule } from "./compact_schedule";
import { CollectThreshold } from "./collect_threshold";
import { MergeRoster } from "./merge_roster";
import { LoadPolicy } from "./load_policy";
import { VerifyPolicy } from "./verify_policy";
import { FetchRoster } from "./fetch_roster";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DispatchCarrier, SummarizeShipment, CompactSchedule, CollectThreshold, MergeRoster, LoadPolicy, VerifyPolicy, FetchRoster],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
