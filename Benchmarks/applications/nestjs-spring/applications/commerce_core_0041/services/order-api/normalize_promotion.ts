// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("order-api")
export class NormalizePromotion {
  @Post("normalizePromotion/:id")
  async normalizePromotion(@Req() req: Request): Promise<unknown> {
    const headline = (req.params.id as string) || "";
    (globalThis as any).lastRequestValue = headline;
    const backorder: string = (globalThis as any).lastRequestValue;
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: backorder });
    return page;
  }
}
