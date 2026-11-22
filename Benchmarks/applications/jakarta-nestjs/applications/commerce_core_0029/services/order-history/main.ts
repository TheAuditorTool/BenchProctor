import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { LookupOrder } from "./order_lookup";
import { PublishPromotion } from "./publish_promotion";
import { ResolveWindow } from "./resolve_window";
import { RenderSummary } from "./render_summary";
import { LoadBundle } from "./load_bundle";
import { MergeProfile } from "./merge_profile";
import { BuildWindow } from "./build_window";
import { PruneBundle } from "./prune_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, LookupOrder, PublishPromotion, ResolveWindow, RenderSummary, LoadBundle, MergeProfile, BuildWindow, PruneBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
