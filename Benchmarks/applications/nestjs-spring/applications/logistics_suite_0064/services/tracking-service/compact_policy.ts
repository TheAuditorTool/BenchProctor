// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("tracking-service")
export class CompactPolicy {
  @Post("compactPolicy")
  async compactPolicy(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const parcel: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(parcel)) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    return "<div>" + consignment + "</div>";
  }
}
