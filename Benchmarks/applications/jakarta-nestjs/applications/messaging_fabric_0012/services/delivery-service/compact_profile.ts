// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("delivery-service")
export class CompactProfile {
  @Post("compactProfile")
  async compactProfile(@Req() req: Request): Promise<unknown> {
    const preface = (req.body?.field as string) || "";
    const parts: string[] = [];
    for (const token of String(preface).split(',')) { parts.push(token); }
    const bulletin: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: bulletin });
    return page;
  }
}
