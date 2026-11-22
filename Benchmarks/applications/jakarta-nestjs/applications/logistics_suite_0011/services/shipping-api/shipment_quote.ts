// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("shipping-api")
export class QuoteShipment {
  @Post("quoteShipment")
  async quoteShipment(@Req() req: Request): Promise<unknown> {
    const caption = req.body.shipping_payload || "";
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: caption });
    return page;
  }
}
