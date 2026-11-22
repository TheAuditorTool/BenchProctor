// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("tracking-service")
export class ArchiveReport {
  @Post("archiveReport")
  async archiveReport(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers["x-custom-header"] as string) || "";
    const _raw = caption;
    const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
    return "<div>" + consignment + "</div>";
  }
}
