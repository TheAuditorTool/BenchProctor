// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("rate-shopper")
export class ArchiveConfig {
  @Post("archiveConfig")
  async archiveConfig(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    return "<div>" + caption + "</div>";
  }
}
