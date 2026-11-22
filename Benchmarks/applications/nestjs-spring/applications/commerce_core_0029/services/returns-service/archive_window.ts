// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("returns-service")
export class ArchiveWindow {
  @Post("archiveWindow/:id")
  async archiveWindow(@Req() req: Request): Promise<unknown> {
    const notice = (req.params.id as string) || "";
    (globalThis as any).lastRequestValue = notice;
    const backorder: string = (globalThis as any).lastRequestValue;
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: backorder });
    return page;
  }
}
