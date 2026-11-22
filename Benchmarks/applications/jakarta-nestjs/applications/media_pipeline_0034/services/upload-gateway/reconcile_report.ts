// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("upload-gateway")
export class ReconcileReport {
  @Post("reconcileReport")
  async reconcileReport(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body?.field as string) || "";
    const parts: string[] = [];
    for (const token of String(synopsis).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: rendition });
    return page;
  }
}
