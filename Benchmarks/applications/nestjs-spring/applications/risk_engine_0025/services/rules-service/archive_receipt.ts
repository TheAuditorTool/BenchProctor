// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("rules-service")
export class ArchiveReceipt {
  @Post("archiveReceipt")
  async archiveReceipt(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["x-forwarded-for"] as string) || "";
    const verdict = excerpt != null ? excerpt : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(verdict)) { throw new BadRequestException({error:"invalid"}); }
    const grievance = verdict;
    return "<div>" + grievance + "</div>";
  }
}
