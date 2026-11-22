// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("preview-renderer")
export class PublishHeader {
  @Post("publishHeader")
  async publishHeader(@Req() req: Request): Promise<unknown> {
    const heading = (req.body.field as string) || "";
    const parts: string[] = [];
    for (const token of String(heading).split(',')) { parts.push(token); }
    const addendum: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: addendum });
    return page;
  }
}
