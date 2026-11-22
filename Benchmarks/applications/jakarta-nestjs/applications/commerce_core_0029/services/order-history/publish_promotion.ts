// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

@Controller("order-history")
export class PublishPromotion {
  @Post("publishPromotion")
  async publishPromotion(@Req() req: Request): Promise<unknown> {
    const notice = (req.query.id as string) || "";
    const backorder = nodeUtil.format("%s", notice);
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: backorder });
    return page;
  }
}
