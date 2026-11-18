// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("retention-service")
export class SweepRetention {
  @Post("sweepRetention")
  async sweepRetention(@Req() req: Request): Promise<unknown> {
    const tagline = req.body.telemetry_payload || "";
    http.get(tagline);
    return { created: true };
  }
}
