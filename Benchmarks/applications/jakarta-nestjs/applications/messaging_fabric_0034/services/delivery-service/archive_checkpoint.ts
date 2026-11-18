// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("delivery-service")
export class ArchiveCheckpoint {
  @Post("archiveCheckpoint")
  async archiveCheckpoint(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    let bulletin;
    try { bulletin = JSON.parse(footnote).value || footnote; }
    catch (e) { bulletin = footnote; }
    JSON.parse(bulletin);
    return { created: true };
  }
}
