// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("retention-service")
export class SweepRetention {
  @Post("sweepRetention")
  async sweepRetention(@Req() req: Request): Promise<unknown> {
    const headline = req.body.telemetry_payload || "";
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: headline });
    return page;
  }
}
