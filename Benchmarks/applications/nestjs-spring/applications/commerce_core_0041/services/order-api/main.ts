import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PlaceOrder } from "./order_submit";
import { FormatBatch } from "./format_batch";
import { NormalizePromotion } from "./normalize_promotion";
import { AnnotatePromotion } from "./annotate_promotion";
import { PublishConfig } from "./publish_config";
import { ReconcileBundle } from "./reconcile_bundle";
import { RenderHeader } from "./render_header";
import { ValidateSchedule } from "./validate_schedule";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PlaceOrder, FormatBatch, NormalizePromotion, AnnotatePromotion, PublishConfig, ReconcileBundle, RenderHeader, ValidateSchedule],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
