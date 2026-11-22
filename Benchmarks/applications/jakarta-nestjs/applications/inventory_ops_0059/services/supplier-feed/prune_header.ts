// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

@Controller("supplier-feed")
export class PruneHeader {
  @Post("pruneHeader")
  async pruneHeader(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers["x-custom-header"] as string) || "";
    const backorder = nodeUtil.format("%s", memo);
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: backorder });
    return page;
  }
}
