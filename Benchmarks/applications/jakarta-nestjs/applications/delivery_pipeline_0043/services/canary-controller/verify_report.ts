// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("canary-controller")
export class VerifyReport {
  @Post("verifyReport")
  async verifyReport(@Req() req: Request): Promise<unknown> {
    const remark = (req.body?.field as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const note: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: note });
    return page;
  }
}
