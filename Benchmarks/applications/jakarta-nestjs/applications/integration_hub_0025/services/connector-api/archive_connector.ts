// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("connector-api")
export class ArchiveConnector {
  @Post("archiveConnector/:id")
  async archiveConnector(@Req() req: Request): Promise<unknown> {
    const footnote = (req.params.id as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(footnote);
    return "<div>" + handshake + "</div>";
  }
}
