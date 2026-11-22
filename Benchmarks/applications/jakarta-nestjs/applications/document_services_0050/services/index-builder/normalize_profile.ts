// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("index-builder")
export class NormalizeProfile {
  @Post("normalizeProfile")
  async normalizeProfile(@Req() req: Request): Promise<unknown> {
    const citation = (req.body?.field as string) || "";
    const parts: string[] = [];
    for (const token of String(citation).split(',')) { parts.push(token); }
    const dossier: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: dossier });
    return page;
  }
}
