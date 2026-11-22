import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { UpdateCart } from "./cart_update";
import { RotateProfile } from "./rotate_profile";
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
  controllers: [HealthController, UpdateCart, RotateProfile, AnnotatePromotion, PublishConfig, ReconcileBundle, RenderHeader, ValidateSchedule],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
