import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ConvertFx } from "./fx_convert";
import { CompactDigest } from "./compact_digest";
import { NormalizeLedger } from "./normalize_ledger";
import { SummarizeWallet } from "./summarize_wallet";
import { RenderWindow } from "./render_window";
import { ResolveWallet } from "./resolve_wallet";
import { MergeBundle } from "./merge_bundle";
import { ArchiveReport } from "./archive_report";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ConvertFx, CompactDigest, NormalizeLedger, SummarizeWallet, RenderWindow, ResolveWallet, MergeBundle, ArchiveReport],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
