// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("escalation-service")
export class PublishBatch {
  @Post("publishBatch")
  async publishBatch(@Req() req: Request): Promise<unknown> {
    const preface = (req.body?.field as string) || "";
    const parts: string[] = [];
    for (const token of String(preface).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: grievance });
    return page;
  }
}
