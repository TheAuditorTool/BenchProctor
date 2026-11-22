// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("decision-log")
export class RenderPolicy {
  @Post("renderPolicy/:id")
  async renderPolicy(@Req() req: Request): Promise<unknown> {
    const memo = (req.params.id as string) || "";
    (globalThis as any).lastRequestValue = memo;
    const verdict: string = (globalThis as any).lastRequestValue;
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: verdict });
    return page;
  }
}
