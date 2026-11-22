// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

@Controller("escalation-service")
export class LoadBundle {
  @Post("loadBundle")
  async loadBundle(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["x-custom-header"] as string) || "";
    const inquiry = nodeUtil.format("%s", remark);
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: inquiry });
    return page;
  }
}
