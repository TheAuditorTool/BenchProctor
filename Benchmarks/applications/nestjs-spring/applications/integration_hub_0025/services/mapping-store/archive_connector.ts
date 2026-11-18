// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("mapping-store")
export class ArchiveConnector {
  @Post("archiveConnector")
  async archiveConnector(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(footnote);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { throw new BadRequestException({error:"invalid"}); }
    const blurb = handshake;
    return "<div>" + blurb + "</div>";
  }
}
