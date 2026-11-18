// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("billing-api")
export class ArchiveRecord {
  @Post("archiveRecord")
  async archiveRecord(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const [remittance] = String(remark).split(',');
    return "<div>" + remittance + "</div>";
  }
}
