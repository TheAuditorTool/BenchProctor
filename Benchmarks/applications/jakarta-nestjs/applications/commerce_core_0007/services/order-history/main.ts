import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { LookupOrder } from "./order_lookup";
import { NormalizeFulfillment } from "./normalize_fulfillment";
import { FetchRoster } from "./fetch_roster";
import { AnnotateSchedule } from "./annotate_schedule";
import { ResolveRoster } from "./resolve_roster";
import { CompactRoster } from "./compact_roster";
import { CompactCart } from "./compact_cart";
import { PruneReceipt } from "./prune_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, LookupOrder, NormalizeFulfillment, FetchRoster, AnnotateSchedule, ResolveRoster, CompactRoster, CompactCart, PruneReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
