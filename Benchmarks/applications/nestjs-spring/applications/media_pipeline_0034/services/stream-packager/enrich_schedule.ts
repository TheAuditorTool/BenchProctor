// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("stream-packager")
export class EnrichSchedule {
  @Post("enrichSchedule/:id")
  async enrichSchedule(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.params.id as string) || "";
    (globalThis as any).lastRequestValue = synopsis;
    const rendition: string = (globalThis as any).lastRequestValue;
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: rendition });
    return page;
  }
}
