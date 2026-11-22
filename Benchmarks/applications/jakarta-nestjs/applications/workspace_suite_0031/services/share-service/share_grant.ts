// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("share-service")
export class GrantShare {
  @Post("grantShare")
  async grantShare(@Req() req: Request): Promise<unknown> {
    const quotation = req.body.workspace_payload || "";
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: quotation });
    return page;
  }
}
