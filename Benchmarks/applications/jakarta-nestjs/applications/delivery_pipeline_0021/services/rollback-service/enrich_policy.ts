// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";
import * as nunjucks from "nunjucks";

@Controller("rollback-service")
export class EnrichPolicy {
  @Post("enrichPolicy")
  async enrichPolicy(@Req() req: Request): Promise<unknown> {
    const summary = (req.query.id as string) || "";
    const phrase = nodeUtil.format("%s", summary);
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: phrase });
    return page;
  }
}
