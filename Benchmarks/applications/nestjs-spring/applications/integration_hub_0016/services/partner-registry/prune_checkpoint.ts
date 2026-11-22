// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("partner-registry")
export class PruneCheckpoint {
  @Post("pruneCheckpoint/:id")
  async pruneCheckpoint(@Req() req: Request): Promise<unknown> {
    const wording = (req.params.id as string) || "";
    (globalThis as any).lastRequestValue = wording;
    const handshake: string = (globalThis as any).lastRequestValue;
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: handshake });
    return page;
  }
}
