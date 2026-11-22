import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { PullSupplierFeed } from "./supplier_feed";
import { LoadRecord } from "./load_record";
import { ReconcileIndex } from "./reconcile_index";
import { RotateProfile } from "./rotate_profile";
import { EnrichProfile } from "./enrich_profile";
import { ValidateReceipt } from "./validate_receipt";
import { ResolveBundle } from "./resolve_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PullSupplierFeed, LoadRecord, ReconcileIndex, RotateProfile, EnrichProfile, ValidateReceipt, ResolveBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
