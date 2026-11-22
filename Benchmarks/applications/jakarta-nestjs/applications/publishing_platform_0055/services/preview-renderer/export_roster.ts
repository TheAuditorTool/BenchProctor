// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("preview-renderer")
export class ExportRoster {
  @Post("exportRoster")
  async exportRoster(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body?.field as string) || "";
    const parts: string[] = [];
    for (const token of String(synopsis).split(',')) { parts.push(token); }
    const byline: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: byline });
    return page;
  }
}
