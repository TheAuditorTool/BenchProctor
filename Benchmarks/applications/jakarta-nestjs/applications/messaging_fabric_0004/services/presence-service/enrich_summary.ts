// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("presence-service")
export class EnrichSummary {
  @Post("enrichSummary")
  async enrichSummary(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body as string) || "";
    const bulletin = String(paragraph).split(/[ \t]+/).join(" ");
    http.get(bulletin);
    return { created: true };
  }
}
