// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("customs-service")
export class ArchiveDigest {
  @Post("archiveDigest")
  async archiveDigest(@Req() req: Request): Promise<unknown> {
    const heading = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(heading).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(consignment)) { throw new BadRequestException({error:"invalid"}); }
    const parcel = consignment;
    return "<div>" + parcel + "</div>";
  }
}
