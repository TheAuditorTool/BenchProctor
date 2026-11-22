// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("caption-service")
export class BuildIndex {
  @Post("buildIndex")
  async buildIndex(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body.field as string) || "";
    const parts: string[] = [];
    for (const token of String(snippet).split(',')) { parts.push(token); }
    const montage: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: montage });
    return page;
  }
}
