import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { LookupSku } from "./sku_lookup";
import { CollectSchedule } from "./collect_schedule";
import { ExportDigest } from "./export_digest";
import { RotateThreshold } from "./rotate_threshold";
import { FetchSupplier } from "./fetch_supplier";
import { SummarizeReservation } from "./summarize_reservation";
import { FormatDigest } from "./format_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, LookupSku, CollectSchedule, ExportDigest, RotateThreshold, FetchSupplier, SummarizeReservation, FormatDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
