// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("log-shipper")
export class ReconcileSchedule {
  @Post("reconcileSchedule")
  async reconcileSchedule(@Req() req: Request): Promise<unknown> {
    const note = (req.body.field as string) || "";
    const parts: string[] = [];
    for (const token of String(note).split(',')) { parts.push(token); }
    const cohort: string = parts.join(',');
    const page = nunjucks.renderString('<div class="bio">{{ bio }}</div>', { bio: cohort });
    return page;
  }
}
