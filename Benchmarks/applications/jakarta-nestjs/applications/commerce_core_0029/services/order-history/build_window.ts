// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("order-history")
export class BuildWindow {
  @Post("buildWindow")
  async buildWindow(@Req() req: Request): Promise<unknown> {
    const notice = (req.body?.field as string) || "";
    const parts: string[] = [];
    for (const token of String(notice).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: backorder });
    return page;
  }
}
