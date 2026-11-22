// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("bounce-handler")
export class ArchiveIndex {
  @Post("archiveIndex")
  async archiveIndex(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-forwarded-for"] as string) || "";
    const bulletin = preface != null ? preface : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(bulletin)) { throw new BadRequestException({error:"invalid"}); }
    const citation = bulletin;
    return "<div>" + citation + "</div>";
  }
}
