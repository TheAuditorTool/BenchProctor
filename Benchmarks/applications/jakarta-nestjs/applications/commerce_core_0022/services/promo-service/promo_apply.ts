// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("promo-service")
export class ApplyPromo {
  @Post("applyPromo")
  async applyPromo(@Req() req: Request): Promise<unknown> {
    const phrase = req.body.orders_payload || "";
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: phrase });
    return page;
  }
}
