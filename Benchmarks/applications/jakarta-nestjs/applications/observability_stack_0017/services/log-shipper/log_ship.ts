// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("log-shipper")
export class ShipLog {
  @Post("shipLog")
  async shipLog(@Req() req: Request): Promise<unknown> {
    const summary = req.body.telemetry_payload || "";
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: summary });
    return page;
  }
}
