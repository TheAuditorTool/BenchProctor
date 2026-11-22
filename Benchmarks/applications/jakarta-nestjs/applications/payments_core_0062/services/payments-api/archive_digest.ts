// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("payments-api")
export class ArchiveDigest {
  @Post("archiveDigest")
  async archiveDigest(@Req() req: Request): Promise<unknown> {
    const headline = (req.body.field as string) || "";
    const parts: string[] = [];
    for (const token of String(headline).split(',')) { parts.push(token); }
    const disbursement: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: disbursement });
    return page;
  }
}
