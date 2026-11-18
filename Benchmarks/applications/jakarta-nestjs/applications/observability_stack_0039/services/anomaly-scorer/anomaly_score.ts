// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("anomaly-scorer")
export class ScoreAnomaly {
  @Post("scoreAnomaly")
  async scoreAnomaly(@Req() req: Request): Promise<unknown> {
    const citation = req.body.telemetry_payload || "";
    http.get(citation);
    return { created: true };
  }
}
