// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("tracking-service")
export class PollTracking {
  @Post("pollTracking")
  async pollTracking(@Req() req: Request): Promise<unknown> {
    const memo = req.body.shipping_payload || "";
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: memo });
    return page;
  }
}
