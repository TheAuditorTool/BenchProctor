// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("customs-service")
export class AnnotateHeader {
  @Post("annotateHeader")
  async annotateHeader(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const parcel: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(parcel)) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    return "<div>" + consignment + "</div>";
  }
}
