// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("preview-renderer")
export class LoadConfig {
  @Post("loadConfig/:id")
  async loadConfig(@Req() req: Request): Promise<unknown> {
    const remark = (req.params.id as string) || "";
    (globalThis as any).lastRequestValue = remark;
    const byline: string = (globalThis as any).lastRequestValue;
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: byline });
    return page;
  }
}
