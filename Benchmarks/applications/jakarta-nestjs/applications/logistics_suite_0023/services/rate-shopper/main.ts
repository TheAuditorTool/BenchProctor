import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ShopRate } from "./rate_shop";
import { ArchiveConfig } from "./archive_config";
import { CollectLabel } from "./collect_label";
import { LoadHeader } from "./load_header";
import { PruneShipment } from "./prune_shipment";
import { BuildSnapshot } from "./build_snapshot";
import { ArchiveSnapshot } from "./archive_snapshot";
import { EnrichCarrier } from "./enrich_carrier";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ShopRate, ArchiveConfig, CollectLabel, LoadHeader, PruneShipment, BuildSnapshot, ArchiveSnapshot, EnrichCarrier],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
